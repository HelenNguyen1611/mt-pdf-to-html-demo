"""Machine checks on finished HTML. Does not replace visual C.6.8 comparison."""

from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

from tools.mt_pdf.schemas import dump_json

PLACEHOLDER_RE = re.compile(r"<!--\s*([A-Z][A-Z0-9_]{2,})\s*-->")
HREF_RE = re.compile(r"""href\s*=\s*["']([^"']*)["']""", re.I)
CSS_2022_RE = re.compile(r"""content\s*:\s*['"]\\?2022['"]""")
PHONE_RE = re.compile(r"\+61[\d\s().-]{8,}")


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._parts: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in {"script", "style"}:
            self._skip += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self._skip:
            self._skip -= 1

    def handle_data(self, data: str) -> None:
        if not self._skip:
            self._parts.append(data)

    def text(self) -> str:
        return " ".join(self._parts)


def _normalize(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = text.replace("•", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _fold(text: str) -> str:
    for dash in ("\u2010", "\u2011", "\u2012", "\u2013", "\u2014", "\u2212"):
        text = text.replace(dash, "-")
    return _normalize(text).casefold()


def _html_text(html: str) -> str:
    parser = _TextExtractor()
    parser.feed(html)
    return _normalize(parser.text())


def _inspect_lines(inspect_dir: Path) -> list[str]:
    lines: list[str] = []
    for path in sorted(inspect_dir.glob("page-*.txt")):
        if path.name.endswith("-detail.txt"):
            continue
        if re.fullmatch(r"page-\d+\.txt", path.name):
            for raw in path.read_text(encoding="utf-8").splitlines():
                line = _normalize(raw)
                if len(line) < 50 or line.isdigit():
                    continue
                if re.match(r"x=\s", line) or " sz=" in line or line.startswith("fonts="):
                    continue
                if re.match(r"^\[(?:L|R)\]", line) or " | '" in line:
                    continue
                if "flags=" in line or line.startswith("ProximaNova"):
                    continue
                lines.append(line)
    return lines


def qa_html(
    html_path: Path,
    inspect_dir: Path | None = None,
    json_out: Path | None = None,
) -> dict[str, Any]:
    html = html_path.read_text(encoding="utf-8")
    issues: list[dict[str, Any]] = []

    for match in HREF_RE.finditer(html):
        href = match.group(1).strip()
        if href in {"", "#"}:
            issues.append({"code": "dead_href", "href": href})

    for match in PLACEHOLDER_RE.finditer(html):
        issues.append({"code": "placeholder", "token": match.group(1)})

    if CSS_2022_RE.search(html):
        issues.append(
            {
                "code": "css_bullet_escape",
                "detail": "Use content: '•'; never content: '\\2022'",
            }
        )

    for phone in PHONE_RE.findall(html):
        # skip if this occurrence sits inside a tel: href nearby
        idx = html.find(phone)
        window = html[max(0, idx - 80) : idx + len(phone) + 10]
        if "tel:" not in window.lower():
            issues.append({"code": "phone_not_tel", "text": _normalize(phone)})

    warnings: list[dict[str, Any]] = []
    if inspect_dir and inspect_dir.is_dir():
        body = _fold(_html_text(html))
        candidates = _inspect_lines(inspect_dir)
        repeats: dict[str, int] = {}
        for line in candidates:
            repeats[line] = repeats.get(line, 0) + 1
        missing: list[str] = []
        for line in candidates:
            if repeats[line] >= 3:
                continue  # running header / footer
            needle = _fold(line[:72] if len(line) > 72 else line)
            if needle and needle not in body:
                missing.append(line[:120])
        if missing:
            warnings.append(
                {
                    "code": "missing_copy",
                    "count": len(missing),
                    "samples": missing[:25],
                }
            )

    report = {
        "html": str(html_path),
        "inspect_dir": str(inspect_dir) if inspect_dir else None,
        "ok": not issues,
        "issue_count": len(issues),
        "issues": issues,
        "warning_count": len(warnings),
        "warnings": warnings,
        "note": "Machine checks only. Visual like-for-like remains framework C.6.8. missing_copy is a warning.",
    }
    if json_out:
        dump_json(json_out, report)
    return report
