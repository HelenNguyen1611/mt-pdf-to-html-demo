# Operational workflow

Companion to `SKILL.md`. Design tokens, components, and visual rules live in `references/Mutual-Trust-Design-Analysis-Framework.md` — do not re-derive them here.

## `build html`

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
15. Favour readable spacing — use a more open line-height and comfortable paragraph gaps so body copy is easy to read; do not pack text as tightly as print if it hurts readability. Family-specific rhythm still wins (Market Review and Outlook stay dense; do not apply Perspective `--space-5` to them).
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

`build html` means execute the workflow above, not explain it.

## `build new`

1. Scan all `*.pdf` files in `./pdf/`.
2. Load `./.pdf-state.json` (create `{}` if missing). Track each PDF by filename with status `completed` or `failed`.
3. For each PDF:
   - `completed` → skip
   - new file or `failed` → build (retry failed)
4. Build with the same rules as `build html`. Output to `website/<html-filename>` and `website/assets/<asset-slug>/`.
5. After content + responsive checks pass → mark `completed` in `.pdf-state.json` (store the output HTML path). On failure → mark `failed` and continue to the next PDF.
6. Do not deploy.

`build new` means execute the workflow above, not explain it.

## Output naming

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
- Timestamp when needed: `<pdf-slug>-YYYYMMDD-HHMMSS.html` (local time, 24h), e.g. `20260812-113845`

Asset folder slug matches the HTML basename (without `.html`):

- Default: `website/assets/<pdf-slug>/`
- With timestamp: `website/assets/<pdf-slug>-YYYYMMDD-HHMMSS/`

Point asset `src`/`href` paths relative to the HTML file (e.g. `assets/<asset-slug>/images/...`).

## Chunked builds (PDFs >10 pages)

Used for white papers and other long reports. State file: `.pdf-chunks.json`.

- Split into chunks of at most ~10 PDF pages, grouped by natural sections.
- Each chunk: `pending` | `in_progress` | `completed` | `failed`.
- Extract images for that chunk into `website/assets/<slug>/images/chunk-NN/`.
- Append HTML before a marker such as `<!-- wp-chunk:N pending -->`.
- Do not rebuild a `completed` chunk unless the user explicitly retries it.
- Keep one continuous document — chunks are a work strategy, not page breaks.

## Inspect dumps

Write under `website/assets/<slug>/inspect/`:

- `page-N.txt` — extracted text per PDF page (0-based)
- `links.json` — link annotations / URIs when present
- optional crops for bullets, hero, charts

Inspect **before** writing HTML. Family-specific extra fields are in framework **C.6.2**.

## Quotes and pull quotes

1. Match the quote’s typeface to the source (serif vs sans, size, weight).
2. Match slant exactly: upright PDF quotes stay upright — do not apply `font-style: italic` or `<em>` by default.
3. Preserve attribution styling and alignment separately from the quote.
4. Nearby source/podcast/link lines follow PDF link colour and underline rules.

## Content width and overflow

Required after layout is in place (desktop and mobile):

1. Shared column / `max-width` / gutters must keep the page within the viewport.
2. No horizontal page scroll (`document`/`body` `scrollWidth` must not exceed the viewport). Wide tables may use local `overflow-x: auto` only.
3. Images: `max-width: 100%`.
4. Verify at typical desktop and mobile widths before marking complete.

## Quality checklist

Before considering the HTML complete:

1. Compare the finished HTML against the entire source PDF.
2. No source copy dropped, duplicated, or invented (including CTAs, chart captions, disclaimers).
3. All headings, paragraphs, quotes, captions, lists, tables, contacts, footnotes, disclaimers preserved.
4. Emphasis matches the PDF (italic/oblique, bold, underline, mixed runs).
5. List/bullet horizontal position matches the PDF body column.
6. Brand styling matches the source (hero/footer colours, link treatment, no invented panels).
7. Hero imagery: clearspace + contrast; logo presence matches the PDF; keep the PDF scrim.
8. Hero↔main and main↔footer gaps match the source, not cramped web defaults.
9. Multi-panel grids split into individual assets and stack readably on mobile.
10. Footer/disclaimer content preserved; structure easy to refine for the existing website.
11. Desktop and mobile: no clipped, hidden, overflowing, or missing content.

Definition of Done: framework **C.6.11**. Visual comparison loop: **C.6.8** (max 3 correction rounds). Desktop fidelity before responsive: **C.6.10**.

## Scope

PDF → responsive HTML → visual/content check. Do not use Paper. Do not build hashing, scheduling, folder watching, PR automation, or production deployment. Simple `.pdf-state.json` tracking for `build new` only is allowed.
