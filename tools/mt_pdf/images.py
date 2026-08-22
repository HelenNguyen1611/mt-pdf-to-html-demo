"""Extract embedded images and clip regions. Clip defaults to render (not extract_image)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from tools.mt_pdf.schemas import (
    dump_json,
    parse_pages,
    require_fitz,
    round_pt,
    unique_path,
)


def _transform_flipped(transform) -> bool:
    if not transform:
        return False
    try:
        return float(transform[0]) < 0
    except (TypeError, IndexError, ValueError):
        return False


def _flip_file(path: Path) -> bool:
    """Horizontal flip. Returns True if flipped on disk."""
    try:
        from PIL import Image
    except ImportError:
        return False
    img = Image.open(path)
    img.transpose(Image.FLIP_LEFT_RIGHT).save(path)
    return True


def extract_images(
    pdf: Path,
    out_dir: Path,
    pages: str | None = None,
    method: str = "extract",
    zoom: float = 2.0,
) -> dict[str, Any]:
    fitz = require_fitz()
    if method not in {"extract", "render"}:
        raise SystemExit("--method must be extract or render")
    doc = fitz.open(pdf)
    try:
        indexes = parse_pages(pages, doc.page_count)
        img_dir = out_dir / "images" / "extracted"
        img_dir.mkdir(parents=True, exist_ok=True)
        mat = fitz.Matrix(zoom, zoom)
        records: list[dict[str, Any]] = []
        xref_path: dict[int, str] = {}

        for i in indexes:
            page = doc[i]
            infos = page.get_image_info(xrefs=True)
            for n, info in enumerate(infos):
                xref = int(info.get("xref") or 0)
                bbox = info.get("bbox")
                if bbox is None:
                    continue
                box = [
                    round_pt(bbox[0]),
                    round_pt(bbox[1]),
                    round_pt(bbox[2]),
                    round_pt(bbox[3]),
                ]
                flipped = _transform_flipped(info.get("transform"))
                w = int(info.get("width") or 0)
                h = int(info.get("height") or 0)
                stem = f"p{i}-img-{n}-xref{xref}"
                used = method
                rel: str | None = None

                if method == "render":
                    path = unique_path(img_dir, stem, ".png")
                    clip = fitz.Rect(bbox)
                    pix = page.get_pixmap(matrix=mat, clip=clip, alpha=True)
                    pix.save(path)
                    rel = str(path.relative_to(out_dir))
                elif xref and xref in xref_path:
                    used = "extract-dup"
                    rel = xref_path[xref]
                else:
                    extracted = None
                    if xref:
                        try:
                            extracted = doc.extract_image(xref)
                        except Exception:
                            extracted = None
                    if extracted and extracted.get("image"):
                        ext = extracted.get("ext") or "png"
                        path = unique_path(img_dir, stem, f".{ext}")
                        path.write_bytes(extracted["image"])
                        if flipped:
                            _flip_file(path)
                        rel = str(path.relative_to(out_dir))
                        xref_path[xref] = rel
                    else:
                        path = unique_path(img_dir, stem, ".png")
                        clip = fitz.Rect(bbox)
                        pix = page.get_pixmap(matrix=mat, clip=clip, alpha=True)
                        pix.save(path)
                        used = "render-fallback"
                        rel = str(path.relative_to(out_dir))

                records.append(
                    {
                        "page": i,
                        "xref": xref,
                        "bbox": box,
                        "width": w,
                        "height": h,
                        "flipped": flipped,
                        "method": used,
                        "path": rel,
                        "name": stem,
                    }
                )

        index = {
            "pdf": str(pdf),
            "method": method,
            "images": records,
        }
        dump_json(img_dir / "images.json", index)
        return index
    finally:
        doc.close()


def clip_region(
    pdf: Path,
    out_dir: Path,
    page_index: int,
    rect: tuple[float, float, float, float],
    name: str,
    method: str = "render",
    zoom: float = 2.0,
) -> dict[str, Any]:
    """Clip a page rectangle. Default method is render (avoids extract_image black fills)."""
    fitz = require_fitz()
    if method not in {"extract", "render"}:
        raise SystemExit("--method must be extract or render")
    doc = fitz.open(pdf)
    try:
        if page_index < 0 or page_index >= doc.page_count:
            raise SystemExit(f"Page {page_index} out of range")
        page = doc[page_index]
        clip = fitz.Rect(*rect)
        img_dir = out_dir / "images" / "clipped"
        img_dir.mkdir(parents=True, exist_ok=True)
        used = method
        path = unique_path(img_dir, name, ".png")

        if method == "extract":
            saved = False
            for info in page.get_image_info(xrefs=True):
                bbox = info.get("bbox")
                if bbox is None or not info.get("xref"):
                    continue
                if not fitz.Rect(bbox).intersects(clip):
                    continue
                extracted = doc.extract_image(int(info["xref"]))
                if not extracted or not extracted.get("image"):
                    continue
                ext = extracted.get("ext") or "png"
                path = unique_path(img_dir, name, f".{ext}")
                path.write_bytes(extracted["image"])
                if _transform_flipped(info.get("transform")):
                    _flip_file(path)
                saved = True
                break
            if not saved:
                used = "render-fallback"
                mat = fitz.Matrix(zoom, zoom)
                page.get_pixmap(matrix=mat, clip=clip, alpha=True).save(path)
        else:
            mat = fitz.Matrix(zoom, zoom)
            page.get_pixmap(matrix=mat, clip=clip, alpha=True).save(path)

        record = {
            "page": page_index,
            "rect": [round_pt(v) for v in rect],
            "method": used,
            "path": str(path.relative_to(out_dir)),
            "name": name,
        }
        dump_json(img_dir / f"{path.stem}.json", record)
        return record
    finally:
        doc.close()
