# Mutual Trust PDF-to-HTML Demo

## Goal

Convert the source PDF into a high-quality responsive webpage for client demonstration.

## Commands

### `build html`

When the user says `build html`, execute the following workflow immediately:

1. Find the source PDF in `./pdf/`.
2. If there is exactly one PDF, use it automatically.
3. Inspect and read the entire PDF before building.
4. Convert it into `./website/<html-filename>` using the Output naming rules (PDF-based name, not `index.html`; add a timestamp when needed).
5. Preserve all content accurately — do not omit, shorten, rewrite, invent or duplicate content. Each PDF phrase/block must appear once unless the PDF itself repeats it.
6. Match the PDF as closely as practical — take colors, backgrounds, typography, imagery, hierarchy, spacing, layout/composition, tables, charts, quotes, callouts and footer treatment from the source. Do not invent alternate themes (e.g. light footer when the PDF footer is dark).
7. Do not invent or alter styles that are not in the PDF. Do not add backgrounds, tinted panels, callout boxes, borders, shadows, or decorative wrappers unless the source shows them. Do not restyle sections with arbitrary web defaults when the PDF has a clear treatment.
8. Links must match the PDF: use the same link color and underline treatment as the source. Do not strip color or underline if the PDF shows them; do not invent browser-default underlines or unstyled “inherit only” links when the PDF links are colored/underlined. Hover/focus may strengthen affordance slightly, but base style stays faithful to the source.
8b. **Link destinations:** Every PDF hyperlink must become a real `<a href="…">` with the URI from the PDF link annotation — not styling only. Never use `href="#"`, empty href, or unresolved template comments (`<!-- OUTLOOK_URL -->`, etc.) in finished HTML. Resolve all template placeholders before delivery. If a URI cannot be read from the PDF after inspection, note it in the report and use a sensible Mutual Trust URL for that CTA (never `#`).
9. Keep one shared content column so logo, hero text, body, program blocks and footer share the same left (and right) edge. Do not let header/hero/footer use a different max-width or padding than the article.
10. Match PDF desktop type scale for article body and section headings as closely as practical. Prefer the PDF’s point sizes scaled consistently over oversized web defaults.
11. Preserve inline and block text styles from the PDF exactly — font family (serif vs sans), italics/oblique, bold/semibold, underline, small caps, letter-spacing, and mixed roman+italic runs. Inspect span-level font names and flags in the PDF; wrap italic phrases in `<em>` (or equivalent) and bold in `<strong>` only when the source is actually italic/bold. Never flatten italic copy to plain roman, and never invent emphasis or italic styling the source does not use.
12. List/bullet alignment must match the PDF. Measure marker and text x-positions against the body column: if bullets sit flush with paragraphs, do not indent; if the PDF indents markers or hanging text, reproduce that indent (and hanging indent for wrapped lines). Do not rely on browser default `ul`/`ol` padding — tune `padding-left`, `list-style-position`, and marker offset so bullets line up like the source.
13. Hero banner follows the source PDF: include the Mutual Trust logo on the hero only if the PDF shows it there; omit it when the PDF does not. When present, make the hero heading and logo clear/readable on desktop (may be slightly larger than strict print scale).
14. Ensure sufficient contrast for any text (and logo) placed on images or photo backgrounds — especially hero titles, dates and overlays. Match the PDF’s treatment first (gradient, scrim, text color/weight/shadow if present). If the web crop or scaling reduces legibility versus the PDF, strengthen contrast just enough for readable text (e.g. a subtle darkening gradient) without inventing a new visual theme or obscuring the image. Verify desktop and mobile.
15. Favour readable spacing — use a more open line-height and comfortable paragraph gaps so body copy is easy to read; do not pack text as tightly as print if it hurts readability.
16. Spacing between the hero banner and main content, and between main content and the footer, must be generous and consistent — measure from the source PDF and match that clearspace. Do not crowd the article against the hero or footer with tight web defaults; use the same vertical rhythm at both junctions unless the PDF clearly differs.
17. Adapt the layout only where necessary to make it responsive.
18. Ensure Desktop and Mobile both work correctly.
19. For any block/section that places text and image on one row on desktop: on tablet and mobile, flexibly reorder to `image → text` or `text → image` based on reading flow and neighbouring sections. Prefer the stack order that keeps the page coherent (e.g. avoid two images stacking back-to-back, or burying a key visual after a long text block). Use CSS order/flex/grid — do not duplicate content.
20. When the PDF shows a multi-panel image grid (e.g. several charts in one figure), split into separate images — one per panel — and lay them out with CSS grid/flex. Keep the desktop arrangement close to the PDF (usually 2 columns). On tablet/mobile, stack panels so each image is full content-width and readable; do not ship one giant composite that shrinks to unreadability on small screens.
21. If phone numbers appear in the content, wrap them in `tel:` links automatically (keep the visible dialling text unchanged).
22. Always include this favicon in the output HTML:
    `<link rel="icon" href="https://mt.wootech.com.au/wp-content/uploads/2024/10/favicon.png" type="image/png" />`
23. Keep all CSS inside `<style>` in the output HTML file.
24. Store extracted/reused assets under `./website/assets/<pdf-slug>/` (or `./website/assets/<pdf-slug>-<timestamp>/` when the HTML filename includes a timestamp).
25. Check the finished page for missing or duplicated content, invented copy, wrong colors/styles vs PDF (including invented backgrounds, incorrect link color/underline, dead links (`href="#"`), unresolved link placeholders, lost or invented italics/bold, and quote blocks restyled with the wrong font or forced italic), clipping, overflow, broken assets, misalignment (including bullet indent vs body column), correct hero logo presence, text/logo contrast on image backgrounds, generous consistent hero↔content↔footer spacing vs PDF, readable split chart grids on mobile, and sensible text/image stack order on tablet/mobile.
26. Do not deploy.

Do not ask for confirmation before starting unless:

- no PDF exists, or
- more than one PDF exists and the intended source cannot be determined.

`build html` means execute the workflow above, not explain it.

### `build new`

When the user says `build new`, process multiple PDFs immediately:

1. Scan all `*.pdf` files in `./pdf/`.
2. Load `./.pdf-state.json` (create `{}` if missing). Track each PDF by filename with status `completed` or `failed`.
3. For each PDF:
   - `completed` → skip
   - new file or `failed` → build (retry failed)
4. Build with the same rules as `build html` (do not restate them). Differences only:
   - Output HTML to `website/<html-filename>` (PDF-based name, not `index.html`) and assets under `website/assets/<asset-slug>/` per Output naming rules
   - Derive `<pdf-slug>`, `<html-filename>`, and asset folder with the Output naming rules below
5. After content + responsive checks pass → mark `completed` in `.pdf-state.json` (store the output HTML path). On failure → mark `failed` and continue to the next PDF.
6. Do not deploy.

`build new` means execute the workflow above, not explain it.

## Success Criteria

- Achieve like-for-like visual fidelity with the source PDF.
- Preserve all content accurately — no omissions, inventions or duplicates.
- Preserve source colors, typography, imagery, hierarchy, spacing, footer style and overall visual character.
- Preserve original text emphasis — italics, bold, and mixed-style runs must match the PDF; do not drop italic styling, and do not invent italic on roman quotes.
- Pull quotes and block quotes keep the PDF’s font (e.g. upright Baskerville/serif when the source is roman serif) — do not swap in body sans or default `font-style: italic` on quotes.
- Do not invent backgrounds, panels, or other styles absent from the PDF; do not arbitrarily restyle content.
- Links match the PDF (color, underline, and destination URI), not browser defaults or unstyled inherit-only treatment. No `href="#"` or unresolved link placeholders in finished HTML.
- Use actual PDF assets wherever possible.
- Multi-panel chart/figure grids are split into separate images and stack readably on mobile.
- Logo, hero text, article content and footer must stay on one vertical alignment grid.
- Bullet/list markers and list text align like the PDF (flush with the body column or indented to the measured offset — not browser-default list indent).
- Hero logo only when the PDF has it; hero heading readable on desktop; body spacing open enough for easy reading.
- Text and logos on image backgrounds keep strong, readable contrast (follow the PDF scrim/overlay; adjust only as needed for legibility).
- Hero-to-content and content-to-footer gaps are generous, mutually consistent, and matched to the source PDF clearspace.
- Adapt only what is necessary for responsive web behavior.
- Side-by-side text+image blocks reorder thoughtfully on tablet/mobile for adjacent-section flow.
- Phone numbers are linked with `tel:`.
- Desktop and mobile must both work well.
- No clipped, hidden, overflowing or missing content.

## Quality Requirements

Before considering the HTML complete:

1. Compare the finished HTML against the entire source PDF.
2. Verify that no source copy has been dropped, duplicated or invented (including CTAs, chart captions and disclaimers).
3. Preserve all headings, paragraphs, quotes, captions, lists, tables, contact details, footnotes and disclaimers.
4. Preserve text emphasis from the PDF (italic/oblique, bold, underline, mixed runs). Confirm quoted phrases, titles, and stressed words still render italic only where the source is italic — and remain roman/upright when the PDF quote is not italic.
5. Verify list/bullet horizontal position against the PDF body column (indent amount, marker alignment, hanging wraps).
6. Preserve the source brand styling as closely as practical — including hero/footer background colors, link color/underline, and the absence of decorative backgrounds where the PDF has none — and avoid arbitrary styling decisions.
7. For imagery and hero sections, maintain sufficient clearspace and text/background contrast so titles, dates and logos remain easy to read on the photo; hero logo presence must match the PDF. Prefer the PDF’s overlay/scrim; add only minimal contrast support if the web crop would otherwise fail readability.
8. Verify hero↔main and main↔footer spacing against the PDF — wider, even gaps; not cramped against either edge.
9. Multi-panel grids (charts and similar) must be split into individual assets and remain readable on mobile (stacked), not one tiny composite.
10. Preserve footer and disclaimer content, but keep the HTML structure easy to refine when integrated into the existing website.
11. Check desktop and mobile for missing, clipped, hidden or overflowing content.

Content completeness is a hard requirement. Never silently omit, invent or duplicate PDF content.

## Quotes & Pull Quotes

Quotes are a frequent fidelity failure — treat them as an explicit check against the PDF:

1. Match the quote’s typeface to the source (serif vs sans, size, weight). Do not restyle a PDF serif quote in the body sans stack, or vice versa.
2. Match slant exactly: if the PDF quote is upright/roman, keep it upright — do **not** apply `font-style: italic`, `<em>`, or “quote looks nicer in italic” defaults. Only italicize when the PDF font flags/face are actually italic/oblique.
3. Preserve attribution styling and alignment separately from the quote (e.g. sans attribution under a serif quote; right-aligned attribution when the PDF shows that).
4. Source/podcast/link lines near quotes follow the PDF link color and underline rules — do not inherit invented quote italic.

## Content Width & Overflow Control

Treat this as a required stage after layout/content is in place (desktop and mobile):

1. Keep the main content width under control — shared column/`max-width`/gutters must prevent the page from growing wider than the viewport.
2. No horizontal page scroll on desktop or mobile (`document`/`body` scrollWidth must not exceed the viewport). Wide elements (tables, chart grids, images, preformatted blocks, absolute/negative offsets) must stay within the content column or use an intentional local overflow (e.g. `overflow-x: auto` on a table wrapper only) without forcing the whole page to scroll sideways.
3. Images and media: `max-width: 100%`; avoid fixed widths that exceed the shell on small screens.
4. Verify at typical desktop and mobile widths before marking the build complete.

## Output

### Naming

Derive `<pdf-slug>` from the source PDF filename (without `.pdf`):

1. Lowercase
2. Replace spaces and underscores with `-`
3. Remove characters other than `a-z`, `0-9`, and `-`
4. Collapse repeated `-` and trim leading/trailing `-`

Examples:

- `July-2026_Perspective-From_Rituals-Over-Rules.pdf` → `july-2026-perspective-from-rituals-over-rules`
- `Family Enterprise Governance.pdf` → `family-enterprise-governance`

HTML filename is based on the PDF slug — **not** `index.html`:

- Default: `<pdf-slug>.html`
- Add a timestamp when needed to avoid overwriting a previous build, or when rebuilding the same PDF while keeping the prior file: `<pdf-slug>-YYYYMMDD-HHMMSS.html` (local time, 24h)
- Timestamp format example: `20260812-113845`

Asset folder slug matches the HTML basename (without `.html`):

- Default: `assets/<pdf-slug>/`
- With timestamp: `assets/<pdf-slug>-YYYYMMDD-HHMMSS/`

### Paths

- `build html` → `website/<html-filename>` and `website/assets/<asset-slug>/`
- `build new` → same pattern under `website/` for each PDF (`website/<html-filename>`, `website/assets/<asset-slug>/`)

Examples:

- `website/july-2026-perspective-from-rituals-over-rules.html`
- `website/july-2026-perspective-from-rituals-over-rules-20260812-113845.html` (when timestamped)
- Assets: `website/assets/july-2026-perspective-from-rituals-over-rules/` (or matching timestamped folder)

Keep all CSS inside `<style>` in the output HTML file. Do not create separate CSS files.
Point asset `src`/`href` paths relative to the HTML file (e.g. `assets/<asset-slug>/images/...`).

## Scope

PDF → responsive HTML → visual/content check → Vercel Preview

Do not use Paper.
Do not build hashing, scheduling, folder watching, PR automation or production deployment.
Simple `.pdf-state.json` tracking for `build new` only is allowed.
