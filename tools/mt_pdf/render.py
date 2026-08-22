"""Raster page previews for visual QA. Not HTML assets."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from tools.mt_pdf.schemas import (
    dump_json,
    is_landscape,
    parse_pages,
    require_fitz,
    round_pt,
)


def render_pages(
    pdf: Path,
    out_dir: Path,
    pages: str | None = None,
    zoom: float = 2.0,
    split_halves: bool | None = None,
) -> dict[str, Any]:
    fitz = require_fitz()
    doc = fitz.open(pdf)
    try:
        indexes = parse_pages(pages, doc.page_count)
        preview_dir = out_dir / "inspect" / "preview"
        preview_dir.mkdir(parents=True, exist_ok=True)
        mat = fitz.Matrix(zoom, zoom)
        written: list[dict[str, Any]] = []

        for i in indexes:
            page = doc[i]
            rect = page.rect
            land = is_landscape(rect.width, rect.height)
            do_split = land if split_halves is None else split_halves

            full_path = preview_dir / f"p{i}-full.png"
            pix = page.get_pixmap(matrix=mat, alpha=False)
            pix.save(full_path)
            entry: dict[str, Any] = {
                "page": i,
                "full": str(full_path.relative_to(out_dir)),
                "width_pt": round_pt(rect.width),
                "height_pt": round_pt(rect.height),
            }

            if do_split:
                mid = rect.width / 2
                left = fitz.Rect(0, 0, mid, rect.height)
                right = fitz.Rect(mid, 0, rect.width, rect.height)
                left_path = preview_dir / f"p{i}-left.png"
                right_path = preview_dir / f"p{i}-right.png"
                page.get_pixmap(matrix=mat, clip=left, alpha=False).save(left_path)
                page.get_pixmap(matrix=mat, clip=right, alpha=False).save(right_path)
                entry["left"] = str(left_path.relative_to(out_dir))
                entry["right"] = str(right_path.relative_to(out_dir))

            written.append(entry)

        index = {
            "pdf": str(pdf),
            "zoom": zoom,
            "pages": written,
        }
        dump_json(preview_dir / "index.json", index)
        return index
    finally:
        doc.close()
