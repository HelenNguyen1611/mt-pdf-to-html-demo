"""Dump text, typography, drawings, and links. Does not render pixmaps."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

from tools.mt_pdf.schemas import (
    SCHEMA_VERSION,
    drawing_to_rect_dump,
    dump_json,
    format_detail_line,
    iter_text_lines,
    page_meta,
    parse_pages,
    require_fitz,
    write_text,
)


def inspect_pdf(
    pdf: Path,
    out_dir: Path,
    pages: str | None = None,
    all_drawings: bool = False,
) -> dict[str, Any]:
    fitz = require_fitz()
    doc = fitz.open(pdf)
    try:
        indexes = parse_pages(pages, doc.page_count)
        inspect_dir = out_dir / "inspect"
        inspect_dir.mkdir(parents=True, exist_ok=True)

        page_entries: list[dict[str, Any]] = []
        all_links: list[dict[str, Any]] = []
        type_scale: Counter[tuple] = Counter()
        meta_pages: list[dict[str, Any]] = []

        for i in indexes:
            page = doc[i]
            rect = page.rect
            meta = page_meta(i, rect.width, rect.height)
            meta_pages.append(meta)

            lines = list(iter_text_lines(page))
            plain = "\n".join(rec["text"] for rec in lines)
            detail = "\n".join(format_detail_line(rec) for rec in lines)
            write_text(inspect_dir / f"page-{i}.txt", plain)
            write_text(inspect_dir / f"page-{i}-detail.txt", detail)

            rects = []
            for drawing in page.get_drawings():
                dump = drawing_to_rect_dump(drawing, all_drawings=all_drawings)
                if dump is not None:
                    rects.append(dump)
            dump_json(inspect_dir / f"page-{i}-rects.json", rects)

            for link in page.get_links():
                box = link.get("from")
                from_rect = None
                if box is not None:
                    from_rect = [
                        round(float(box.x0), 1),
                        round(float(box.y0), 1),
                        round(float(box.x1), 1),
                        round(float(box.y1), 1),
                    ]
                all_links.append(
                    {
                        "page": i,
                        "kind": int(link.get("kind") or 0),
                        "uri": link.get("uri"),
                        "from": from_rect,
                    }
                )

            for rec in lines:
                key = (
                    rec["fonts"][0] if rec["fonts"] else "",
                    rec["sizes"][0] if rec["sizes"] else 0,
                    rec["italic"],
                    rec["color"],
                )
                type_scale[key] += 1

            page_entries.append(
                {
                    "index": i,
                    "width": meta["width"],
                    "height": meta["height"],
                    "landscape": meta["landscape"],
                    "mid_x": meta["mid_x"],
                    "page_max_px": meta["page_max_px"],
                    "text": f"page-{i}.txt",
                    "detail": f"page-{i}-detail.txt",
                    "rects": f"page-{i}-rects.json",
                    "line_count": len(lines),
                    "rect_count": len(rects),
                }
            )

        dump_json(inspect_dir / "links.json", all_links)

        first = meta_pages[0] if meta_pages else None
        meta_doc = {
            "schema": SCHEMA_VERSION,
            "pdf": str(pdf),
            "page_count": doc.page_count,
            "inspected_pages": indexes,
            "page_max_px": first["page_max_px"] if first else None,
            "spread": bool(first["landscape"]) if first else False,
            "pages": meta_pages,
            "type_scale": [
                {
                    "font": font,
                    "size": size,
                    "italic": italic,
                    "color": color,
                    "lines": count,
                }
                for (font, size, italic, color), count in type_scale.most_common(40)
            ],
        }
        dump_json(inspect_dir / "meta.json", meta_doc)

        manifest = {
            "schema": SCHEMA_VERSION,
            "pdf": str(pdf),
            "slug": out_dir.name,
            "page_count": doc.page_count,
            "inspect_dir": str(inspect_dir),
            "links": "links.json",
            "meta": "meta.json",
            "pages": page_entries,
        }
        dump_json(inspect_dir / "manifest.json", manifest)
        return manifest
    finally:
        doc.close()
