"""CLI: python -m tools.mt_pdf <inspect|render|images|qa> ..."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from tools.mt_pdf.schemas import SCHEMA_VERSION, asset_out_dir


def _pdf(path: str) -> Path:
    p = Path(path)
    if not p.is_file():
        raise SystemExit(f"PDF not found: {p}")
    return p


def _parse_rect(spec: str) -> tuple[float, float, float, float]:
    parts = [p.strip() for p in spec.replace(" ", ",").split(",") if p.strip()]
    if len(parts) != 4:
        raise SystemExit("--rect must be x0,y0,x1,y1")
    return tuple(float(p) for p in parts)  # type: ignore[return-value]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m tools.mt_pdf",
        description=(
            "Deterministic PDF extractors. AI maps artifacts to the family template; "
            "these commands do not generate HTML."
        ),
    )
    parser.add_argument(
        "--version",
        action="version",
        version=SCHEMA_VERSION,
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    inspect_p = sub.add_parser(
        "inspect",
        help="Dump text, typography, filled rects, links, meta, manifest (no PNGs)",
    )
    inspect_p.add_argument("pdf")
    inspect_p.add_argument("--out", help="Asset folder (default website/assets/<slug>)")
    inspect_p.add_argument("--pages", help="0-based range, e.g. 20-25 or all")
    inspect_p.add_argument(
        "--all-drawings",
        action="store_true",
        help="Dump every drawing, including strokes and tiny paths",
    )

    render_p = sub.add_parser(
        "render",
        help="Write inspect/preview PNGs for visual QA (not HTML src)",
    )
    render_p.add_argument("pdf")
    render_p.add_argument("--out")
    render_p.add_argument("--pages")
    render_p.add_argument("--zoom", type=float, default=2.0)
    render_p.add_argument(
        "--split-halves",
        action="store_true",
        help="Always clip left/right halves",
    )
    render_p.add_argument(
        "--no-split-halves",
        action="store_true",
        help="Never clip halves, even on landscape spreads",
    )

    img = sub.add_parser("images", help="Extract XObjects or clip a rectangle")
    img_sub = img.add_subparsers(dest="images_cmd", required=True)

    ext = img_sub.add_parser("extract", help="Inventory + extract embedded images")
    ext.add_argument("pdf")
    ext.add_argument("--out")
    ext.add_argument("--pages")
    ext.add_argument("--method", choices=("extract", "render"), default="extract")
    ext.add_argument("--zoom", type=float, default=2.0)

    clip = img_sub.add_parser(
        "clip",
        help="Clip a page rect (default render — avoids extract_image black fills)",
    )
    clip.add_argument("pdf")
    clip.add_argument("--out")
    clip.add_argument("--page", type=int, required=True, help="0-based page index")
    clip.add_argument("--rect", required=True, help="x0,y0,x1,y1 in PDF points")
    clip.add_argument("--name", required=True)
    clip.add_argument("--method", choices=("extract", "render"), default="render")
    clip.add_argument("--zoom", type=float, default=2.0)

    qa_p = sub.add_parser(
        "qa",
        help="Machine HTML checks. Does not replace visual C.6.8.",
    )
    qa_p.add_argument("html")
    qa_p.add_argument("--inspect", help="inspect/ folder with page-N.txt")
    qa_p.add_argument("--json-out")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.cmd == "inspect":
        from tools.mt_pdf.inspect import inspect_pdf

        pdf = _pdf(args.pdf)
        out = asset_out_dir(pdf, args.out)
        result = inspect_pdf(
            pdf, out, pages=args.pages, all_drawings=args.all_drawings
        )
        print(json.dumps({"ok": True, "manifest": result["inspect_dir"]}, indent=2))
        return 0

    if args.cmd == "render":
        from tools.mt_pdf.render import render_pages

        pdf = _pdf(args.pdf)
        out = asset_out_dir(pdf, args.out)
        split: bool | None
        if args.split_halves:
            split = True
        elif args.no_split_halves:
            split = False
        else:
            split = None
        result = render_pages(
            pdf, out, pages=args.pages, zoom=args.zoom, split_halves=split
        )
        print(json.dumps({"ok": True, "pages": len(result["pages"])}, indent=2))
        return 0

    if args.cmd == "images":
        pdf = _pdf(args.pdf)
        out = asset_out_dir(pdf, args.out)
        if args.images_cmd == "extract":
            from tools.mt_pdf.images import extract_images

            result = extract_images(
                pdf,
                out,
                pages=args.pages,
                method=args.method,
                zoom=args.zoom,
            )
            print(json.dumps({"ok": True, "count": len(result["images"])}, indent=2))
            return 0
        from tools.mt_pdf.images import clip_region

        result = clip_region(
            pdf,
            out,
            page_index=args.page,
            rect=_parse_rect(args.rect),
            name=args.name,
            method=args.method,
            zoom=args.zoom,
        )
        print(json.dumps({"ok": True, "path": result["path"]}, indent=2))
        return 0

    if args.cmd == "qa":
        from tools.mt_pdf.qa import qa_html

        html = Path(args.html)
        if not html.is_file():
            raise SystemExit(f"HTML not found: {html}")
        inspect_dir = Path(args.inspect) if args.inspect else None
        json_out = Path(args.json_out) if args.json_out else None
        report = qa_html(html, inspect_dir=inspect_dir, json_out=json_out)
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 0 if report["ok"] else 1

    return 2


if __name__ == "__main__":
    sys.exit(main())
