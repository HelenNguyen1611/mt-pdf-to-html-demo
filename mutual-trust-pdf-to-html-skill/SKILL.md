---
name: mutual-trust-pdf-to-html
description: Convert Mutual Trust Insight PDFs into responsive HTML using the approved Mutual Trust design framework and document-family templates.
---

# Mutual Trust PDF → HTML

## Purpose

Convert a supplied Mutual Trust PDF into production-ready responsive HTML.

## Required workflow

Before generating HTML:

1. Read `references/Mutual-Trust-Design-Analysis-Framework.md`.
2. Analyse the supplied PDF.
3. Determine its document family:
   - market-review
   - quarterly-outlook
   - perspective
   - white-paper
4. Load the corresponding template from `assets/`.
5. Preserve the PDF's content and hierarchy.
6. Adapt the document into a continuous responsive web experience.
7. Follow the typography, colour, spacing, component and legal/footer rules defined in the design framework.

## Template mapping

- market-review → `assets/template-market-review.html`
- quarterly-outlook → `assets/template-quarterly-outlook.html`
- perspective → `assets/template-perspective.html`
- white-paper → `assets/template-white-paper.html`

## Important

Do not re-derive Mutual Trust brand rules from scratch.

`references/Mutual-Trust-Design-Analysis-Framework.md` is the source of truth for the design system.

Use the HTML templates as structural references rather than inventing a new design system.

---

## When to apply

Apply immediately when the user asks to convert a Mutual Trust PDF, run `build html` / `build new`, or produce Insight HTML from a document-family template. Do not explain the workflow first — execute it.

If the current repository has `website/template-<family>.html`, prefer that live catalog over this skill's `assets/` copy so newly added components are not lost. After adding a component, update both the repo template and this skill's `assets/` file.

## Family classification

Classify from the PDF's purpose and structure (framework **B.0**), not the filename alone:

| Family | Signals |
| --- | --- |
| **market-review** | Periodic market report; dense bullets; **Global Markets heat table**; **6-chart grid**; title overlay on hero; usually ~3 pages |
| **quarterly-outlook** | Longer strategy piece; stacked `MT-Logo.svg` + "Quarterly Outlook" kicker on hero; H1 **below** the image; dark A4 back cover |
| **perspective** | Short insight article (~3 pages); small logo on hero; H1 below image; author sign-off; **white** legal footer (no black back cover) |
| **white-paper** | Long research report; often co-branded; cover + purpose band + TOC; many section openers / stat / table / infographic panels |

If more than one family could fit, inspect cover + first inner spread + footer before choosing.

## Execute

Do not ask for confirmation unless no PDF exists, or more than one PDF exists and the source cannot be determined.

### 1. Locate the PDF

- `build html` → `./pdf/` (exactly one PDF: use it)
- `build new` → every `*.pdf` in `./pdf/`, skipping `completed` entries in `.pdf-state.json`
- Otherwise use the PDF the user named (including `white_paper/` or `demo-pdf/`)

### 2. Read the design framework

Read [references/Mutual-Trust-Design-Analysis-Framework.md](references/Mutual-Trust-Design-Analysis-Framework.md) before writing HTML. Follow **C.4** and **C.6**. Do not invent tokens, type scale, or footer treatment.

### 3. Inspect the entire PDF

Before any HTML/CSS, extract and record (framework **C.6.2**):

- page count, page W/H → `--page-max`
- text, fonts, italic/oblique (from render, not font name alone)
- link **annotations / URIs**
- images / vectors / charts (split multi-panel figures)
- hero W×H, crop, scrim, logo variant and placement
- content column x0/x1, list marker x, heading hierarchy
- footer / contacts / legal (framework **B.5**)

Write inspect dumps under `website/assets/<slug>/inspect/`. Family-specific inspect extra: **C.6.2**.

### 4. Copy the family template

Copy the mapped template from this skill's `assets/` to `website/<html-filename>`. Fill slots. Override `:root` tokens from PDF measurements. Keep all CSS in a single `<style>` block.

If the PDF has a repeating panel with **no catalog class**: add the component to the template first (tokens + BEM + skeleton + one lookup row in the framework), then use it. Do not invent one-off markup only on the article page.

### 5. Convert to a continuous webpage

PDF is the visual source of truth for composition, type, imagery, spacing, and components. HTML must **not** recreate print pagination:

- no A4 `.document-page` shells for body flow
- no page numbers or running headers/footers
- no blank space added to fake a page break

Page boundaries are **QA checkpoints** only (framework **C.6.9**).

### 6. Assets and output

Derive `<pdf-slug>` from the PDF filename (no `.pdf`): lowercase; spaces/underscores → `-`; keep `a-z`, `0-9`, `-`; collapse/trim `-`.

- HTML: `website/<pdf-slug>.html` (not `index.html`)
- Timestamp when needed: `website/<pdf-slug>-YYYYMMDD-HHMMSS.html`
- Assets: `website/assets/<asset-slug>/` matching the HTML basename
- Fonts: `website/assets/fonts/` (Baskerville + Proxima Nova) — do not substitute
- Official logos: framework **A.5** — do not crop a logo from the PDF if the SVG exists
- Favicon (required): `https://mt.wootech.com.au/wp-content/uploads/2024/10/favicon.png`
- Image `src` paths relative to the HTML file

Long PDFs (**>10 pages**, typically white-paper): chunk via `.pdf-chunks.json` (max ~10 PDF pages per chunk). Do not rebuild `completed` chunks unless asked to retry.

### 7. Desktop fidelity, then responsive

Achieve desktop like-for-like first (framework **C.6.8**, max 3 correction loops). Then adapt for tablet/mobile (**C.6.10**): stack columns, local table scroll, split chart grids, thoughtful image/text order. Do not ship one unreadably small composite figure.

### 8. Quality gate

Compare the finished HTML against the **entire** PDF. Mark complete only when framework **C.6.11** is met. Do not deploy.

## Hard rules

- Preserve all content: no omit, shorten, rewrite, invent, or duplicate.
- Do not invent backgrounds, tinted panels, callouts, borders, shadows, or wrappers the PDF does not show.
- Links: PDF colour + underline treatment **and** real `href` from the PDF URI. Never `href="#"`. Resolve every template placeholder.
- Wrap phone numbers in `tel:` (visible text unchanged).
- Italics/bold only where the PDF is actually italic/bold. Quotes keep the PDF typeface and slant (do not default italic).
- One shared content column: logo, hero, body, and footer share the same left/right edge inside `--page-max`.
- List markers: measure against the body column (Flush / Outdent / Inset) — not browser-default `ul` padding.
- CSS `content` bullets: write the literal character `content: '•';`. Never `content: '\2022'` — JSON/YAML skill packaging strips the backslash and leaves `2022`.
- Hero logo only if the PDF has it there. Keep overlay/scrim when the PDF needs contrast.
- `document`/`body` must not scroll horizontally. `max-width: 100%` on images.
- Do not use Paper. Do not add hashing, scheduling, watchers, or production deploy.

## Commands

**`build html`** — convert the source PDF in `./pdf/` now (single-PDF auto-select).

**`build new`** — convert every new or `failed` PDF in `./pdf/`; skip `completed`; write `.pdf-state.json`. Continue after a failure.

## Additional resources

- Design system (read first): [references/Mutual-Trust-Design-Analysis-Framework.md](references/Mutual-Trust-Design-Analysis-Framework.md)
- Templates: [assets/template-market-review.html](assets/template-market-review.html), [assets/template-quarterly-outlook.html](assets/template-quarterly-outlook.html), [assets/template-perspective.html](assets/template-perspective.html), [assets/template-white-paper.html](assets/template-white-paper.html)
