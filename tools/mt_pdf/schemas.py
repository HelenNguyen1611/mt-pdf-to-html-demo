"""Shared contracts, encoding helpers, and page-range parsing."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterable, Sequence, TypedDict

SCHEMA_VERSION = "mt-pdf-inspect-v1"
PT_DPI = 96.0
PT_TO_PX = PT_DPI / 72.0

# PyMuPDF text flag: bit 1 = italic
FLAG_ITALIC = 2

# Filled panels / photo bands, not icon doodles (~7–36pt). Override with --all-drawings.
MIN_FILL_AREA_PT = 200.0
MIN_FILL_SIDE_PT = 18.0
MIN_FILL_MAX_SIDE_PT = 40.0


class RectDump(TypedDict):
    rect: list[float]
    fill: list[float] | None
    color: list[float] | None
    width: float
    height: float


class PageMeta(TypedDict):
    index: int
    width: float
    height: float
    landscape: bool
    mid_x: float
    page_max_px: float
    half_max_px: float


class ImageRecord(TypedDict, total=False):
    page: int
    xref: int
    bbox: list[float]
    width: int
    height: int
    flipped: bool
    method: str
    path: str
    name: str


def require_fitz():
    try:
        import pymupdf as fitz  # type: ignore
    except ImportError:
        try:
            import fitz  # type: ignore
        except ImportError as exc:
            raise SystemExit(
                "PyMuPDF is required. Install with: pip install pymupdf"
            ) from exc
    return fitz


def slugify_pdf(path: str | Path) -> str:
    name = Path(path).stem.lower()
    name = re.sub(r"[\s_]+", "-", name)
    name = re.sub(r"[^a-z0-9-]", "", name)
    name = re.sub(r"-{2,}", "-", name).strip("-")
    return name or "pdf"


def parse_pages(spec: str | None, page_count: int) -> list[int]:
    """Parse 'all', '20', '20-25', or '20-25,31' as 0-based indexes."""
    if spec is None or spec.strip().lower() in {"", "all", "*"}:
        return list(range(page_count))
    indexes: list[int] = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            start, end = int(a.strip()), int(b.strip())
            if start > end:
                start, end = end, start
            indexes.extend(range(start, end + 1))
        else:
            indexes.append(int(part))
    out: list[int] = []
    seen: set[int] = set()
    for i in indexes:
        if i < 0 or i >= page_count:
            raise SystemExit(f"Page index {i} out of range 0..{page_count - 1}")
        if i not in seen:
            seen.add(i)
            out.append(i)
    return out


def round_pt(value: float, digits: int = 1) -> float:
    return round(float(value), digits)


def page_max_px(width_pt: float) -> float:
    return round(width_pt * PT_TO_PX, 1)


def is_landscape(width: float, height: float) -> bool:
    return width > height * 1.15


def color_int_hex(value: int) -> str:
    """Match existing inspect dumps: 0x0 for black, else 0xrrggbb."""
    return f"0x{int(value):x}"


def fill_to_hex(fill: Sequence[float] | None) -> str | None:
    if not fill or len(fill) < 3:
        return None
    r, g, b = fill[:3]
    if max(r, g, b) <= 1.01:
        r, g, b = r * 255, g * 255, b * 255
    return f"#{int(round(r)):02x}{int(round(g)):02x}{int(round(b)):02x}"


def span_italic(span: dict[str, Any]) -> bool:
    flags = int(span.get("flags") or 0)
    if flags & FLAG_ITALIC:
        return True
    font = str(span.get("font") or "")
    lowered = font.lower()
    return bool(
        re.search(r"(italic|oblique|regularit)", lowered)
        or font.endswith("It")
        or font.split("-")[-1].endswith("It")
    )


def dump_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if text and not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")


def asset_out_dir(pdf: Path, out: str | None) -> Path:
    if out:
        return Path(out)
    return Path("website") / "assets" / slugify_pdf(pdf)


def unique_path(directory: Path, stem: str, suffix: str) -> Path:
    candidate = directory / f"{stem}{suffix}"
    n = 2
    while candidate.exists():
        candidate = directory / f"{stem}-{n}{suffix}"
        n += 1
    return candidate


def iter_text_lines(page) -> Iterable[dict[str, Any]]:
    """Yield one record per text line from get_text('dict')."""
    for block in page.get_text("dict").get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            spans = line.get("spans") or []
            if not spans:
                continue
            text = "".join(str(s.get("text") or "") for s in spans)
            if text == "":
                continue
            fonts = list(dict.fromkeys(str(s.get("font") or "") for s in spans))
            sizes = list(
                dict.fromkeys(round_pt(float(s.get("size") or 0), 1) for s in spans)
            )
            first = spans[0]
            # Top-left of the line box (not baseline origin) — matches existing dumps.
            lb = line.get("bbox") or first.get("bbox") or [0, 0, 0, 0]
            yield {
                "text": text,
                "fonts": fonts,
                "sizes": sizes,
                "italic": any(span_italic(s) for s in spans),
                "color": int(first.get("color") or 0),
                "x": round_pt(float(lb[0])),
                "y": round_pt(float(lb[1])),
                "bbox": [round_pt(v) for v in lb],
            }


def format_detail_line(rec: dict[str, Any]) -> str:
    fonts = rec["fonts"]
    sizes = rec["sizes"]
    return (
        f"{rec['text']}\n"
        f"  fonts={fonts} sizes={sizes} italic={rec['italic']} "
        f"color={color_int_hex(rec['color'])} x={rec['x']} y={rec['y']}"
    )


def drawing_to_rect_dump(drawing: dict[str, Any], *, all_drawings: bool) -> RectDump | None:
    raw = drawing.get("rect")
    if raw is None:
        return None
    x0, y0, x1, y1 = (float(raw[0]), float(raw[1]), float(raw[2]), float(raw[3]))
    width = round_pt(abs(x1 - x0))
    height = round_pt(abs(y1 - y0))
    fill = drawing.get("fill")
    color = drawing.get("color")
    if fill is not None:
        fill = [float(c) for c in fill[:4]]
    if color is not None:
        color = [float(c) for c in color[:4]]
    area = width * height
    if not all_drawings:
        if fill is None:
            return None
        if area < MIN_FILL_AREA_PT:
            return None
        if min(width, height) < MIN_FILL_SIDE_PT:
            return None
        if max(width, height) < MIN_FILL_MAX_SIDE_PT:
            return None
    return {
        "rect": [round_pt(x0), round_pt(y0), round_pt(x1), round_pt(y1)],
        "fill": fill,
        "color": color,
        "width": width,
        "height": height,
    }


def page_meta(index: int, width: float, height: float) -> PageMeta:
    w = round_pt(width)
    h = round_pt(height)
    land = is_landscape(w, h)
    return {
        "index": index,
        "width": w,
        "height": h,
        "landscape": land,
        "mid_x": round_pt(w / 2),
        "page_max_px": page_max_px(w if not land else w / 2),
        "half_max_px": page_max_px(w / 2),
    }
