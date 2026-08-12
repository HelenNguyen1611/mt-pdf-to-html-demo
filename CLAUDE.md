# Mutual Trust PDF-to-HTML Demo

## Goal

Convert the source PDF into a high-quality responsive webpage for client demonstration.

## Commands

### `build html`

When the user says `build html`, execute the following workflow immediately:

1. Find the source PDF in `./pdf/`.
2. If there is exactly one PDF, use it automatically.
3. Inspect and read the entire PDF before building.
4. Convert it into `./website/index.html`.
5. Preserve all content accurately — do not omit, shorten, rewrite or invent content.
6. Match the PDF as closely as practical:
   - colors
   - typography
   - imagery
   - hierarchy
   - spacing
   - layout/composition
   - tables, charts, quotes and callouts
7. Keep one shared content column so logo, hero text, body, program blocks and footer share the same left (and right) edge. Do not let header/hero/footer use a different max-width or padding than the article.
8. Match PDF desktop type scale for article body and section headings as closely as practical. Prefer the PDF’s point sizes scaled consistently over oversized web defaults.
9. Make the hero more prominent for web: enlarge the hero heading (“Perspective from…”) and the Mutual Trust logo versus a strict PDF 1:1 scale so they read clearly on desktop.
10. Favour readable spacing — use a more open line-height and comfortable paragraph gaps so body copy is easy to read; do not pack text as tightly as print if it hurts readability.
11. Adapt the layout only where necessary to make it responsive.
12. Ensure Desktop and Mobile both work correctly.
13. For any block/section that places text and image on one row on desktop: on tablet and mobile, flexibly reorder to `image → text` or `text → image` based on reading flow and neighbouring sections. Prefer the stack order that keeps the page coherent (e.g. avoid two images stacking back-to-back, or burying a key visual after a long text block). Use CSS order/flex/grid — do not duplicate content.
14. If phone numbers appear in the content, wrap them in `tel:` links automatically (keep the visible dialling text unchanged).
15. Default link style must have no underline; do not rely on browser underline defaults. Hover/focus may add underline only if needed for clarity.
16. Always include this favicon in the output HTML:
    `<link rel="icon" href="https://mt.wootech.com.au/wp-content/uploads/2024/10/favicon.png" type="image/png" />`
17. Keep all CSS inside `<style>` in `index.html`.
18. Store extracted/reused assets in `./website/assets/`.
19. Check the finished page for missing content, clipping, overflow, broken assets, misalignment, hero logo/heading prominence, and sensible text/image stack order on tablet/mobile.
20. Do not deploy.

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
   - Output to `website/<pdf-slug>/index.html` and assets under `website/<pdf-slug>/assets/`
   - Derive `<pdf-slug>` with the Output naming rules below
5. After content + responsive checks pass → mark `completed` in `.pdf-state.json`. On failure → mark `failed` and continue to the next PDF.
6. Do not deploy.

`build new` means execute the workflow above, not explain it.

## Success Criteria

- Achieve like-for-like visual fidelity with the source PDF.
- Preserve all content accurately.
- Preserve source colors, typography, imagery, hierarchy, spacing and overall visual character.
- Do not omit, shorten, rewrite or invent content.
- Use actual PDF assets wherever possible.
- Logo, hero text, article content and footer must stay on one vertical alignment grid.
- Hero logo and hero heading should be larger and clearer than a strict print scale; body line-height/spacing should stay open enough for easy reading.
- Adapt only what is necessary for responsive web behavior.
- Side-by-side text+image blocks reorder thoughtfully on tablet/mobile for adjacent-section flow.
- Phone numbers are linked with `tel:`; links are not underlined by default.
- Desktop and mobile must both work well.
- No clipped, hidden, overflowing or missing content.

## Quality Requirements

Before considering the HTML complete:

1. Compare the finished HTML against the entire source PDF.
2. Verify that no source copy has been dropped.
3. Preserve all headings, paragraphs, quotes, captions, lists, tables, contact details, footnotes and disclaimers.
4. Preserve the source brand styling as closely as practical; avoid arbitrary styling decisions.
5. For imagery and hero sections, maintain sufficient clearspace and text/background contrast.
6. Preserve footer and disclaimer content, but keep the HTML structure easy to refine when integrated into the existing website.
7. Check desktop and mobile for missing, clipped, hidden or overflowing content.

Content completeness is a hard requirement. Never silently omit PDF content.

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

### Paths

- `build html` → `website/index.html` and `website/assets/`
- `build new` → `website/<pdf-slug>/index.html` and `website/<pdf-slug>/assets/`

Keep all CSS inside `<style>` in `index.html`. Do not create separate CSS files.
The HTML entry file is always named `index.html` inside its output folder.

## Scope

PDF → responsive HTML → visual/content check → Vercel Preview

Do not use Paper.
Do not build hashing, scheduling, folder watching, PR automation or production deployment.
Simple `.pdf-state.json` tracking for `build new` only is allowed.
