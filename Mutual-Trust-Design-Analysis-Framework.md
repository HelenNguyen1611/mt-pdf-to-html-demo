# Mutual Trust — Design Analysis & Base Framework

_Phạm vi: phân tích 7 file PDF trong `demo-pdf` + đối chiếu Official Style Guide trên Figma. Mục tiêu convert: **PDF → responsive HTML** có độ trung thực thị giác cao — **không** mô phỏng trang A4 trong browser. Tài liệu phân tích / đề xuất — chưa build HTML trừ khi được yêu cầu._

## Cách đọc tài liệu này

Hai nguồn thông tin được tách rõ — **không trộn giá trị suy đoán từ PDF vào design token chính thức**:

| Nguồn                                  | Vai trò                                                               | Áp dụng cho                                                                                  |
| -------------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **A. Official MT Style Guide** (Figma) | **Source of truth cho token** (tên font, HEX brand, hệ type/UI chuẩn) | Font family, colour HEX, tên style (H1–H6, Text large…)                                      |
| **B. Phân tích 7 PDF**                 | **Source of truth cho bản convert cụ thể**                            | Composition, typography thực tế, hierarchy, imagery, spacing, components, biến thể theo file |

### Nguyên tắc PDF → Web

PDF là **source of truth** về:

- composition, typography thực tế, hierarchy
- imagery, logo, màu sắc
- content width, spacing, bullet/list, component styling

Nhưng HTML **không** giữ các đặc tính chỉ thuộc print:

- page break / khung trang A4 cố định
- số trang
- repeated running footer / running header chỉ để đánh dấu trang
- khoảng trắng cuối trang do pagination

HTML phải là **responsive webpage liên tục** (continuous document flow). Ranh giới trang PDF chỉ dùng làm **checkpoint visual QA** (xem C.6), không tái tạo thành `.document-page` trên web.

### Layout mới → component trong template (bắt buộc)

Khi PDF có **khối lặp hoặc panel chưa có class** (quote box, bảng, lưới card, chart+legend, stat, case study, contributor…):

1. **Đối chiếu catalog** family đó (`template-white-paper.html` / `-perspective` / `-market-review` / `-quarterly-outlook`). Khớp → **copy markup**, chỉ điền copy/SVG/màu đo PDF.
2. **Không khớp** → **không** viết HTML one-off trong file bài. Trước hết **chuẩn hóa thành component** trên template:
   - Token `--*-*` (màu, size đo PDF)
   - CSS class BEM trên template
   - Skeleton HTML (comment catalog cuối `<main>` hoặc khối mẫu)
   - Một dòng lookup **PDF pattern → class** trong mục family tương ứng của tài liệu này
3. Sau đó mới build trang bài **base theo component** vừa thêm.
4. Modifier (`--accent`, `--offset`, `--stack`) khi cùng pattern, khác màu/cột — **không** class mới nếu chỉ khác copy.

Nhóm D: catalog + quy trình chi tiết ở **B.7 Nhóm D — Component catalog**.

### Nguyên tắc ưu tiên khi convert PDF → HTML

**Mục tiêu hàng đầu: like-for-like thị giác với PDF nguồn trên desktop**, trong một trang web liên tục. Style Guide không được làm trang “đúng brand token nhưng lệch bản PDF”. Chi tiết quy trình so sánh: **C.6**.

| Ưu tiên      | Cái gì                                                                       | Ai thắng khi xung đột                                                                  |
| ------------ | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| 1 (cao nhất) | Nội dung, bố cục, placement, hierarchy, imagery, spacing giữa các khối       | **PDF**                                                                                |
| 2            | Cỡ chữ, line-height, độ đậm/nghiêng, indent list, khoảng hero↔content↔footer | **PDF** (đo từ nguồn; Style Guide chỉ là điểm xuất phát)                               |
| 3            | Font _family_ và mã màu brand (Black / White / Light Grey / Grey / Ochre)    | **Style Guide** — map lệch export **nhẹ, cùng tông** về HEX chuẩn. Nếu mắt thấy khác (heading đồng `#D17B19` vs Ochre vàng `#CB962E`) → **giữ HEX PDF** |
| 4            | Semantic / one-off trong PDF (bảng dương–âm, H1 lệch màu một bài…)           | **PDF** — giữ và ghi chú PDF-specific                                                  |

**Quy tắc vận hành**

1. Style Guide cung cấp **tên token đúng** (Baskerville, Proxima Nova, Ochre `#CB962E`…) — tránh invent font/màu sai. **Ngoại lệ heading/accent:** nếu HEX PDF khác rõ so với token Style Guide (không chỉ lệch export), ưu tiên màu PDF trên token component (`--qo-section-color`, lede, link của bài đó).
2. Khi type scale Style Guide (ví dụ H1 70px) **khác** cỡ trên PDF → **override theo PDF**. Không phóng cover lên 70px chỉ vì Style Guide ghi vậy.
3. Spacing Style Guide (`--space-*`) là baseline web; **rhythm thật theo PDF** (không theo khoảng trống do page break).
4. Chỉ nới leading/body size so với bản in khi cần đọc trên màn hình — và chỉ vừa đủ; vẫn giữ cảm giác mật độ/hierarchy của PDF.
5. Không thay layout PDF bằng layout “chuẩn web” của Style Guide nếu làm lệch composition nguồn.
6. Không tái tạo pagination PDF (A4 artboard, số trang, running header/footer chỉ để đánh số trang).

**Nguồn Style Guide**

- [Desktop Typography](https://www.figma.com/design/Gg76pDgGhJgQcPuh3Jigjd/Mutual-Trust-%E2%80%93-AI-Template?node-id=2-611) — node `2:611`
- [Colour](https://www.figma.com/design/Gg76pDgGhJgQcPuh3Jigjd/Mutual-Trust-%E2%80%93-AI-Template?node-id=2-466) — node `2:466`

---

# A. Official MT Style Guide (source of truth)

## A.1 Typefaces

| Vai trò          | Font                            | Ghi chú Style Guide            |
| ---------------- | ------------------------------- | ------------------------------ |
| Headings (H1–H6) | **Baskerville** Regular         | Serif display / section titles |
| Body / UI text   | **Proxima Nova** Regular + Bold | Sans — text large → small      |

_(Proxima Nova là font thương mại — cần xác nhận license khi build web công khai.)_

## A.2 Desktop Typography system

Nguồn: Figma _Desktop Typography_ (`2:611`). Line-height lấy từ style/computed trong file.

### Headings — Baskerville

| Style             | Size     | Line-height  | Letter-spacing |
| ----------------- | -------- | ------------ | -------------- |
| Desktop Heading 1 | **70px** | 72px (~1.03) | 0              |
| Desktop Heading 2 | **48px** | 1.2          | 0              |
| Desktop Heading 3 | **40px** | 1.1          | 0              |
| Desktop Heading 4 | **32px** | 1.3          | 0              |
| Desktop Heading 5 | **24px** | 1.4          | 0              |
| Desktop Heading 6 | **16px** | 1.4          | 0              |

### Text styles — Proxima Nova

| Style        | Size     | Weight                | Line-height  |
| ------------ | -------- | --------------------- | ------------ |
| Text large   | **20px** | Regular (Normal)      | 1.5          |
| Text medium  | **18px** | Regular (Normal)      | 24px (≈1.33) |
| Text regular | **16px** | Regular **hoặc** Bold | 1.5          |
| Text small   | **14px** | Regular **hoặc** Bold | 1.5          |

> **Convert rule:** bảng trên = token/style name chính thức. Khi build một PDF cụ thể, **size / line-height / spacing / placement lấy theo PDF** (xem B.2); chỉ giữ font family + colour HEX từ Style Guide. Không ép trang PDF vào đúng scale Desktop Typography nếu làm lệch bản gốc.

## A.3 Colour palette

Nguồn: Figma _Colour_ (`2:466`).

| Tên (Style Guide) | HEX       | Vai trò UI                                                    |
| ----------------- | --------- | ------------------------------------------------------------- |
| **Black**         | `#000000` | Text chính, mực chữ, nền tối khi cần đen tuyền                |
| **White**         | `#FFFFFF` | Nền trang, chữ trên ảnh/nền tối                               |
| **Light Grey**    | `#F4F4F4` | Nền callout / pull-quote / surface phụ                        |
| **Grey**          | `#767676` | Text phụ, caption, chú thích                                  |
| **Ochre**         | `#CB962E` | Accent — hyperlink, số thứ tự section, tiêu đề nhấn, viền box |

### Design tokens (chính thức)

```
/* Typefaces */
--font-serif: "Baskerville", Georgia, serif;
--font-sans:  "Proxima Nova", "Helvetica Neue", Arial, sans-serif;

/* Colours — Style Guide */
--color-black:      #000000;
--color-white:      #FFFFFF;
--color-light-grey: #F4F4F4;
--color-grey:       #767676;
--color-ochre:      #CB962E;

/* Role aliases */
--color-ink:          var(--color-black);
--color-ink-muted:    var(--color-grey);
--color-accent:       var(--color-ochre);
--color-surface-tint: var(--color-light-grey);
--color-surface-dark: var(--color-black);

/* Type scale — Desktop (Style Guide baseline) */
--text-h1: 70px;   /* Baskerville, lh ~72px */
--text-h2: 48px;   /* Baskerville, lh 1.2 */
--text-h3: 40px;   /* Baskerville, lh 1.1 */
--text-h4: 32px;   /* Baskerville, lh 1.3 */
--text-h5: 24px;   /* Baskerville, lh 1.4 */
--text-h6: 16px;   /* Baskerville, lh 1.4 */
--text-large:  20px;  /* Proxima Nova, lh 1.5 */
--text-medium: 18px;  /* Proxima Nova, lh 24px */
--text-regular: 16px; /* Proxima Nova Regular/Bold, lh 1.5 */
--text-small:  14px;  /* Proxima Nova Regular/Bold, lh 1.5 */
```

## A.4 UI styling rules (từ Style Guide)

Áp dụng mặc định khi dựng HTML/framework:

- Text chính: Black `#000000` trên White `#FFFFFF`
- Text phụ / meta: Grey `#767676`
- Accent / link / nhấn: Ochre `#CB962E` — **màu + underline theo PDF nguồn** (nhiều Perspective/Insight PDF chỉ tô màu, **không** gạch chân; không mặc định `text-decoration: underline` kiểu browser)
- Surface phụ (callout, quote box): Light Grey `#F4F4F4` — **không** invent panel xám-xanh khác trừ khi PDF cụ thể bắt buộc match và đã ghi nhận ở mục B
- Heading: Baskerville; body/UI: Proxima Nova
- Không dùng màu ngoài 5 mã Style Guide cho brand UI; semantic data colours (nếu cần) nằm ở mục B.6

## A.5 Logo assets (URL chính thức — dùng cho mọi template)

**Không** extract/crop logo từ PDF khi convert HTML trừ khi URL dưới không khớp biến thể trên PDF. Mọi template (`template.html`, `template-perspective.html`, `template-market-review.html`, `template-quarterly-outlook.html`, `template-white-paper.html`) dùng một trong các asset sau — **chọn theo loại logo mà PDF gốc đang dùng**:

| File              | URL                                                                                       | Hình dạng                                                                    | Dùng khi PDF có…                                                                                   |
| ----------------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **`logo-m.svg`**  | `https://www.mutualtrust.com.au/wp-content/themes/mutual_trust/assets/images/logo-m.svg`  | Ngang: icon mái vòm **bên trái** + wordmark `MUTUAL TRUST` (viewBox ~238×27) | Logo ngang trên hero (góc trên-trái — nhóm C Perspective); footer/legal khi PDF dùng bản ngang     |
| **`MT-Logo.svg`** | `https://www.mutualtrust.com.au/wp-content/themes/mutual_trust/assets/images/MT-Logo.svg` | Xếp chồng: icon **phía trên**, wordmark phía dưới (viewBox ~194×51)          | Logo căn giữa trên hero / back cover (nhóm B Quarterly Outlook), hoặc mọi chỗ PDF dùng bản stacked |
| **`MT-Monogram.svg`** | `website/assets/MT-Monogram.svg` (local)                                              | Icon mái vòm lớn, không wordmark — watermark purpose band                    | Nhóm D White Paper p1 — **`fill: #000c1d`**; render qua `background-image` trên `.wp-purpose` |

**Gợi ý map theo family (vẫn phải đối chiếu PDF từng file):**

| Family                    | Hero / cover                                  | Web HTML (không lặp theo trang)                                                              |
| ------------------------- | --------------------------------------------- | -------------------------------------------------------------------------------------------- |
| A — Market Review         | Thường **không** logo trên hero               | Footer/legal một lần: `logo-m.svg` nếu PDF có logo ở vùng đó                                 |
| B — Quarterly Outlook     | Hero căn giữa → **`MT-Logo.svg`** (stacked)   | Back-cover/legal cuối: **`MT-Logo.svg`** khi PDF có; **không** lặp running header từng trang |
| C — Perspective / Insight | Hero góc trên-trái → **`logo-m.svg`** (ngang) | Logo hero một lần; **không** lặp logo đầu mỗi “trang” PDF chỉ để đánh dấu pagination         |
| D — White Paper           | Cover footer co-brand — logo MT + Uni Adelaide (PNG từ PDF → `assets/<slug>/`) | Purpose p1: **`MT-Monogram.svg`** watermark góc dưới-phải; **không** logo hero trên cover    |

**Styling**

- Cả hai SVG mặc định **fill trắng** — đặt trực tiếp trên ảnh hero / nền tối.
- Trên nền trắng / Light Grey: đảo sang mực tối (CSS `filter`, `currentColor` + chỉnh SVG, hoặc lớp tương đương) để khớp logo đen/xám trên PDF — **không** để logo trắng trên nền trắng.
- Giữ tỷ lệ gốc; width theo đo PDF (không méo). Placement (top-left / center / hidden) theo PDF, không theo thói quen web.
- **Nhóm B hero:** stacked `MT-Logo.svg` rộng **½** chuỗi kicker *"Quarterly Outlook"* (`.qo-hero__brand` + `.qo-hero__logo { width: 50% }`) — không cố định 360px. Footer stacked: `--qo-footer-logo-width` (~200px), tách khỏi hero.

**Favicon** (riêng, không thay logo): `https://www.mutualtrust.com.au/wp-content/uploads/2024/10/favicon.png`

---

# B. Phân tích từ 7 PDF (layout & patterns)

_Phần này giữ nguyên giá trị phân tích thực tế từ PDF. Không dùng làm source of truth cho font/colour tokens — chỉ để layout, placement, spacing quan sát, families và component._

## B.0 Danh sách tài liệu & phân nhóm

Sau khi đọc toàn bộ 7 PDF, chúng chia thành 3 nhóm rõ rệt theo mục đích và cấu trúc trình bày, không phải 7 thiết kế khác nhau:

**Nhóm A — Market Review** (báo cáo thị trường định kỳ, **nhiều số liệu**: bullet + **heat table** + **lưới chart**)

- `June_2026_Quarterly_Market_Review.pdf` (3 trang)
- `October2025MonthlyMarketReview.pdf` (3 trang)
- `April_2026_Monthly_Market_Review.pdf` (3 trang) — cùng pattern table + 6 chart; tham chiếu build `website/april-2026-monthly-market-review.html`

**Nhóm B — Quarterly Outlook** (bài phân tích chiến lược dài, nhiều phần)

- `MutualTrustQuarterlyOutlookJune2026.pdf` (9 trang)
- `March-2026-Quarterly-Outlook-Equities-the-tug-of-war.pdf` (7 trang)

**Nhóm C — Perspective / Insight Article** (bài viết ngắn, 1 chủ đề, 3 trang)

- `MutualTrustProtectingintergenerationalwealththroughtimesofchangeJuly2026.pdf`
- `Perspective_from_Brendan_Henderson_Double_Death_Tax_Trap.pdf`
- `Strengtheningfarmsafety–nowandforfuture-generations (1).pdf`

Cả 3 nhóm dùng chung hệ nhận diện (font family + palette brand khớp Style Guide) nhưng khác nhau ở bố cục trang bìa, mật độ nội dung và một số component đặc thù.

## B.1 Font usage quan sát trong PDF (đối chiếu Style Guide)

| Quan sát PDF                                                                                                | Khớp Style Guide?                                                                                                             |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Heading / display / pull-quote → Baskerville                                                                | Có — dùng `--font-serif`                                                                                                      |
| Body, bảng, caption, disclaimer → Proxima Nova (PDF còn thấy Light; Style Guide Desktop ghi Regular + Bold) | Có family; weight Light là biến thể PDF — khi build ưu tiên Regular/Bold theo Style Guide trừ khi PDF bắt buộc Light để match |
| Bullet glyph ArialMT / SymbolMT / Wingdings2                                                                | Artefact Word export — **không** phải Style Guide; thay bằng bullet CSS                                                       |

## B.2 Type size & leading đo từ PDF _(override candidates)_

Các số đo dưới đây là **quan sát bản in**, không thay thế type scale Style Guide. Khi convert PDF → HTML: bắt đầu từ tokens mục A.2, rồi override size/line-height nếu cần fidelity.

| Vai trò trong PDF        | Cỡ quan sát (pt) | Gợi ý map Style Guide (baseline)                         | Khi nào override                                                       |
| ------------------------ | ---------------- | -------------------------------------------------------- | ---------------------------------------------------------------------- |
| Tiêu đề bìa              | 28–40pt          | H2–H3 (48 / 40px) hoặc nhỏ hơn H1 70px                   | Hầu hết cover PDF nhỏ hơn H1 70px — **thường cần override xuống**      |
| H2 section (Baskerville) | 16–22pt          | H5–H6 (24 / 16px)                                        | Override nhẹ theo file                                                 |
| Thân bài                 | 9.5–11pt         | Text small / regular (14 / 16px) làm baseline web dễ đọc | Có thể giữ 14–16px web; nhóm A dày hơn có thể dùng `--text-small`      |
| Caption / disclaimer     | 6–8pt            | Text small 14px (floor web)                              | PDF nhỏ hơn nhiều — web không nên xuống dưới ~11–12px vì accessibility |

**Line-height PDF:** ≈ **1.2×** cỡ chữ thân bài (leading in ấn chặt). Style Guide body dùng **1.5** — baseline web theo Style Guide; khi match PDF có thể siết về ~1.2–1.35 nếu cần cảm giác “đặc” của bản gốc.

Đoạn văn PDF: không thụt đầu dòng, ngăn cách bằng khoảng trắng dòng.

## B.3 Khổ trang, lề & content width

_Phần đo geometry trang PDF — hữu ích cho visual QA / content width. **Không** yêu cầu HTML giữ khung A4 hay page break._

- Khổ trang PDF gốc: **A4 – 595 × 842pt (210 × 297mm)**, nhất quán cả 7 file (đặc tính print).
- Layout mặc định: **1 cột**; content width chừa lề đối xứng, không có cột lề trang trí.
- Lề trái/phải đo được dao động theo nhóm:
  - Nhóm A/C ≈ **54–58pt** (~19–20mm)
  - Nhóm B ≈ **72pt** (~25mm)
- Khi lên web: lấy **content width** từ đo PDF làm tham chiếu (~**700–760px**; nhóm B hẹp hơn khi chia 2 cột) — **không** giữ khổ A4 cố định, không tạo artboard từng trang.
- PDF có **running footer** (tên tài liệu + số trang) trên mọi trang — đây là artefact pagination. Trên HTML: **không** tái tạo số trang / footer lặp theo trang; giữ một footer/legal duy nhất ở cuối document (nội dung pháp lý + contacts theo B.5).

## B.4 Hình ảnh & placement

- **Page shell max-width = khổ PDF (rule chung — bắt buộc):** HTML **không** để hero/content tràn full viewport browser. Shell `.document` (hoặc tương đương) đặt `max-width` = **chiều rộng trang PDF** quy đổi @ 96dpi (`pt × 4/3`). Ví dụ A4 portrait **595.32 pt → ~794px** (`--page-max`). Trang căn giữa; nền ngoài shell có thể trắng/neutral. Bên trong shell vẫn continuous flow (không giả lập nhiều trang A4 / page-break).
- **Ảnh bìa (hero) full-bleed trong page shell** — tràn hết bề ngang **của shell PDF**, không tràn hết cửa sổ browser; ảnh thiên nhiên/đời sống tông ấm.
- **Hero aspect ratio + chiều cao — desktop (bắt buộc):** đo **W trang × H dải hero** trên PDF (pt) → CSS `aspect-ratio: W / H` trên hero **bên trong** `--page-max`. Khi shell = đúng khổ PDF, chiều cao hero web = chiều cao hero PDF quy đổi (vd. **224.2 pt → ~299px** trên shell ~794px). **Không** stretch hero full-viewport (sẽ phóng H quá lớn). Ví dụ _Protecting Intergenerational Wealth_: `595.32 / 224.2`; _Double Death Tax Trap_: `595.32 / 211`. Ảnh extract khớp vùng nhìn thấy; `background-position` tinh chỉnh sau khi shell + ratio + orientation đúng.
- **Hero trên mobile/tablet (bắt buộc — khác desktop):** giữ **cùng asset + hướng subject + scrim**, nhưng **không** bắt buộc giữ đúng `aspect-ratio` PDF nếu band quá dẹt làm `background-size: cover` cắt mất chủ thể hoặc **logo / kicker / title overlay bị chồng lên hoa, tràn mép, chữ cắt**. Được phép:
  1. nới hero cao hơn (vd. `--perspective-hero-aspect-mobile: 3 / 2` hoặc `min-height` hợp lý ~200–280px theo viewport);
  2. giảm logo / kicker size + padding trong hero;
  3. đặt overlay bằng flex (logo trên, kicker dưới với `margin-top: auto` + padding) để **toàn bộ chữ nằm trong khung**, clearspace tối thiểu tới mép;
  4. tinh chỉnh `background-position` mobile nếu cần — vẫn ưu tiên subject phía PDF (trái/phải), không “zoom” cắt mất cụm chính.
  **Không** để hero mobile chỉ ~130–150px cao (shell hẹp × ratio PDF ~2.8) rồi chữ đè ảnh. **Không** full-bleed viewport ngoài `--page-max` chỉ để “làm hero to”.
- **Hero image orientation / mirror (bắt buộc kiểm tra):** trước khi dùng ảnh extract làm `background-image`, đọc **transform matrix** của XObject trên trang (`get_image_info` / tương đương). Nếu `scaleX` **âm** (PDF lật ngang ảnh), asset raw sẽ **ngược** so với bản in — phải `FLIP_LEFT_RIGHT` file ảnh (hoặc tương đương) rồi mới calibrate `background-position`. Ví dụ _Double Death Tax Trap_: hoa lệch **phải** trên PDF nhưng raw JPEG lệch trái cho đến khi flip. **Không** chỉ đẩy `background-position` để “che” lỗi mirror. Sau khi đúng hướng, mới tinh chỉnh position/% để subject khớp crop PDF.
- **Hero overlay / scrim (rule chung — bắt buộc kiểm tra):** khi PDF đặt **logo trắng hoặc chữ trắng** lên ảnh, nguồn thường có lớp tối (flat opacity hoặc gradient). Ví dụ _Protecting Intergenerational Wealth_: fill đen phủ toàn hero, **opacity ≈ 0.25**. HTML **phải** tái tạo overlay tương đương — **không** dùng ảnh crop trần nếu logo/chữ trên HTML kém tương phản hơn PDF. Chỉ bỏ overlay khi PDF thật sự không có _và_ contrast vẫn đạt. Kiểm tra lại contrast trên **mobile** sau khi đổi tỉ lệ hero.
- **Logo Mutual Trust** — URL chính thức ở **A.5**; chọn `logo-m.svg` (ngang) hoặc `MT-Logo.svg` (stacked) đúng như PDF. SVG mặc định trắng (hero/nền tối); trên nền trắng đảo sang mực tối.
- Biểu đồ nhóm A: xem **B.6.2** (heat table) và **B.7 / B.7.2** (lưới chart) — không gộp 6 panel thành một ảnh lớn.

## B.5 Footer / Disclaimer (recurring — mọi PDF)

Khối **một lần** ở cuối document (không lặp theo trang). Dùng markup + CSS dưới đây làm **nền tái sử dụng**, rồi **đo PDF nguồn** để override copy, số cột, type scale, clearspace và variant nền (trắng vs tối).

### B.5.1 Nội dung pháp lý (3 tầng — hầu hết PDF)

Thứ tự / gộp đoạn có thể lệch nhẹ theo file — **copy đúng PDF**, không invent:

1. **Liability** — thường mở đầu: *"Liability limited by a scheme approved under Professional Standards Legislation…"*
2. **Disclaimer tài chính** — forward-looking / general nature / seek advice / FSG… (có thể gộp chung đoạn 1 trên Perspective ngắn)
3. **Acknowledgement of Country** — đoạn riêng phía dưới

### B.5.2 Markup chuẩn (nền tái sử dụng)

**Nhóm C (Perspective) — contacts → legal trên nền trắng** (không back-cover đen; không số trang / running tagline PDF):

```html
<section class="perspective-legal" aria-label="Contacts and disclaimer">
  <div class="perspective-contacts" aria-label="Office contacts">
    <!-- Col 1: HQ / Melbourne — địa chỉ đầy đủ -->
    <p class="perspective-contacts__office">
      <strong>Melbourne</strong>
      Level 32<br />
      360 Collins Street<br />
      Melbourne VIC 3000<br />
      T <a href="tel:+61396059500">+61 3 9605 9500</a>
    </p>

    <!-- Col 2–3: cặp city + phone (stack dọc trong cột) -->
    <div class="perspective-contacts__col">
      <p class="perspective-contacts__stack">
        <strong>Sydney</strong>
        <a href="tel:+61292247600">+61 2 9224 7600</a>
      </p>
      <p class="perspective-contacts__stack">
        <strong>Brisbane</strong>
        <a href="tel:+61721151100">+61 7 2115 1100</a>
      </p>
    </div>
    <div class="perspective-contacts__col">
      <p class="perspective-contacts__stack">
        <strong>Adelaide</strong>
        <a href="tel:+61870823900">+61 8 7082 3900</a>
      </p>
      <p class="perspective-contacts__stack">
        <strong>Perth</strong>
        <a href="tel:+61892307788">+61 8 9230 7788</a>
      </p>
    </div>

    <!-- Col 4: meta — email, web, ABN/AFSL, © -->
    <div class="perspective-contacts__meta">
      <p><a href="mailto:info@mutualtrust.com.au">info@mutualtrust.com.au</a></p>
      <p><a href="https://www.mutualtrust.com.au/">www.mutualtrust.com.au</a></p>
      <p>ABN: 71 004 285 330&nbsp;&nbsp;AFSL: 234590</p>
      <p>© <!-- YEAR --> Mutual Trust Pty Ltd.</p>
    </div>
  </div>

  <!-- Chỉ các <p> con trực tiếp của .perspective-legal = disclaimer -->
  <p><!-- LIABILITY (+ disclaimer body nếu PDF gộp) --></p>
  <p><!-- ACKNOWLEDGEMENT_OF_COUNTRY --></p>
</section>
```

**Class roles (ổn định — AI giữ tên class, chỉ đổi nội dung / CSS token):**

| Class | Vai trò |
| --- | --- |
| `.perspective-legal` | Wrapper cuối bài: type scale legal + (tuỳ PDF) border-top |
| `.perspective-contacts` | Grid văn phòng + meta |
| `.perspective-contacts__office` | Cột HQ (city serif + địa chỉ nhiều dòng) |
| `.perspective-contacts__col` | Nhóm 2 city xếp chồng (Syd/BNE, Adel/Perth…) |
| `.perspective-contacts__stack` | Một city + phone |
| `.perspective-contacts__meta` | Email / web / ABN·AFSL / © |
| `.perspective-legal > p` | **Chỉ** đoạn Liability / disclaimer / Acknowledgement |

Template tham chiếu:

- Nhóm C (Perspective): `website/template-perspective.html` — khối `.perspective-legal` (nền trắng)
- Nhóm A (Market Review): `website/template-market-review.html` — khối `.mr-footer` (nền tối) + cùng class `.perspective-contacts` (B.5)
- Nhóm B (Quarterly Outlook): `website/template-quarterly-outlook.html` — khối `.qo-footer` (back cover tối, logo stacked `MT-Logo.svg` + tagline) + `.perspective-contacts` (B.5)

### B.5.3 CSS nền + quy tắc spacing (tránh lỗi hay gặp)

```css
.perspective-legal {
  /* type: Proxima; size/lh đo từ PDF (thường ~6–8pt → web calibrate, đừng để 12px mặc định nếu PDF nhỏ) */
  border-top: var(--perspective-legal-border); /* none nếu PDF không có rule */
}

/* Disclaimer ONLY — không để margin “rò” vào contact <p> */
.perspective-legal > p { margin: 0 0 /* gap giữa 2 đoạn legal — đo PDF */; }
.perspective-legal .perspective-contacts p { margin: 0; }

/* Clearspace contacts → dòng “Liability…” — đo PDF (thường ~6–10pt ≈ 8–13px @ 96dpi) */
.perspective-contacts + p { margin-top: /* đo */; }

.perspective-contacts {
  display: grid;
  align-items: start; /* không stretch cột ngắn */
  /* mobile (mặc định): **2 cột** → khoảng 2 hàng (HQ|stack / stack|meta) — không stack 1 cột dài */
  grid-template-columns: repeat(2, minmax(0, 1fr));
  /* desktop ≥600–700px: thường 4 cột — HQ | stack | stack | meta; tỉ lệ đo từ PDF */
}
@media (max-width: 768px) {
  .perspective-contacts__meta {
    grid-column: 1 / -1; /* email/web full width dưới 2 cột city */
    padding-top: 0;
  }
}

/* City label: Baskerville, màu xám nhạt (vd. #99999b), size ~9pt */
.perspective-contacts__office strong,
.perspective-contacts__stack strong {
  display: block;
  font-family: var(--font-serif);
  font-weight: 400;
  color: var(--perspective-contact-label-color);
  /* margin-bottom: PDF thường gần flush với dòng detail — đo, đừng mặc định 8–16px */
}

/* Meta: trên nhiều Perspective, dòng đầu (email) canh hàng detail dưới city label — không canh đỉnh chữ “Melbourne” */
.perspective-contacts__meta { /* padding-top / blank row trước ABN nếu PDF có */ }

.perspective-contacts a { color: inherit; text-decoration: none; } /* trừ khi PDF link hoá khác */
```

**Cấm / bỏ khỏi HTML web (artefact pagination PDF):**

- Số trang (`3`, `Page X`…)
- Running footer lặp: tên bài + tagline đáy trang (vd. *"Protecting intergenerational wealth…"* chỉ để chạy trang)
- Nhân bản disclaimer trên mọi “trang”

### B.5.4 Checklist calibrate theo PDF nguồn (bắt buộc trước khi chốt)

1. **Copy** — Liability / disclaimer / Acknowledgement / contacts / © year đúng từng chữ; SĐT bọc `tel:`.
2. **Thứ tự khối** — contacts trước hay sau legal; logo trên footer tối (A/B) có/không.
3. **Grid** — số cột, cặp city nào chung cột, Melb có địa chỉ đủ dòng không.
4. **Type** — size/lh legal vs contact detail vs city label (serif); màu city label.
5. **Clearspace** — đo pt→px:
   - đáy cột cao nhất (thường dòng ©) → đỉnh “Liability…”
   - khoảng giữa đoạn Liability và Acknowledgement
   - Melb phone thường **cao hơn** ©; đừng để Melb thành cột cao nhất rồi dồn Liability sát đáy (margin rò từ `.perspective-legal p` là nguyên nhân hay gặp).
6. **Meta rhythm** — PDF thường: email → web → (khoảng trống / hàng city thứ 2) → ABN·AFSL → ©.
7. **Nền** — trắng cuối bài (C) vs dải/back-cover tối + logo/tagline (A/B) — xem B.7; không invent panel/border nếu PDF không có.
8. **QA** — không horizontal scroll; **mobile contacts = lưới 2 cột** (không stack 1 cột); meta có thể full-width hàng dưới; không số trang.

### B.5.5 Biến thể theo nhóm (sau khi có nền B.5.2)

| Nhóm | Footer web |
| --- | --- |
| **C — Perspective** | Markup B.5.2; nền trắng; disclaimer ngắn; không back cover đen |
| **A — Market Review** | Dải nền tối (`.mr-footer`); contacts B.5; **email/www thường có gạch chân trắng** (hairline PDF) — xem B.5.6; city Baskerville; body/legal Proxima Regular trắng; logo chỉ khi PDF có |
| **B — Outlook** | Back cover tối = **một khối cao bằng A4** trong `--page-max` (`.qo-footer` `min-height` = page H PDF). Logo stacked + tagline; **khoảng trống lớn trước logo (~297pt) và sau tagline (~246pt)**; byline PDF đưa vào article, không chạy footer |

Số điện thoại / địa chỉ / ABN·AFSL lấy từ **PDF đang convert** (bảng trên chỉ là skeleton — luôn đối chiếu nguồn).

### B.5.6 Footer links — type Market Review (dark band)

Đo PDF (April 2026 MMR và cùng family): trên nền đen, cột meta:

| Phần | Font | Size (PDF) | Underline |
| ---- | ---- | ---------- | --------- |
| City labels (Melbourne…) | Baskerville | ~9pt | Không |
| Địa chỉ / SĐT (`tel:`) | Proxima Nova Regular | ~6pt | **Không** |
| `info@…` / `www.…` | Proxima Nova Regular | ~6pt | **Có** — hairline trắng dưới chữ (drawing fill trắng) |
| ABN / AFSL | Proxima Nova Regular | ~6pt | Không |
| Legal / AoC | Proxima Nova Regular | ~6pt | Không (thường **trắng đầy đủ**, không xám mờ) |

**CSS (`template-market-review.html`):**

```css
.mr-footer .perspective-contacts a { text-decoration: none; /* tel + default */ }
.mr-footer .perspective-contacts__meta a {
  text-decoration: underline;
  text-decoration-color: #fff;
  text-decoration-thickness: 1px;
  text-underline-offset: 0.18em;
  font-family: var(--font-sans);
  font-weight: 400;
}
```

**Không:** bỏ underline email/www trên footer tối MMR; dùng bold/sans cho city khi PDF là Baskerville; để `a:hover` là lý do duy nhất có underline (base phải đã underline nếu PDF có).

**Cảnh báo:** rule toàn cục `p { font-size: var(--mr-body-size) }` sẽ làm email/www/ABN phình cỡ body — phải ` .mr-footer .perspective-contacts p { font-size: inherit; }`.

Perspective (nhóm C) footer trắng vẫn thường **không** underline meta — đừng copy rule MMR sang Perspective.

## B.6 Màu quan sát trong PDF (không thuộc Style Guide palette)

PDF export từng lệch quanh Ochre (`#D17B19`, `#D17A18`, `#CBA020`, `#C99329`…) và vài tông xám/đen phụ (`#1B1B1F`, `#8D8D90`, `#E0E4EB`…).

**Map về Style Guide chỉ khi cùng tông và mắt không phân biệt** (vd. `#CBA020` / `#C99329` → Ochre `#CB962E`). **Không** map heading đồng/đỏ-cam `#D17B19` về `#CB962E` — khoảng cách G/B lớn, HTML sẽ vàng hơn PDF. Đo span heading; gán HEX PDF lên `--qo-section-color` / `--qo-section-lede-color` (và link cùng bài nếu PDF cùng mã).

### B.6.1 Semantic colours — chỉ bảng Market Review (nhóm A)

Giữ khi build data table — PDF-specific, không có trong Figma Colour:

| Vai trò       | HEX quan sát | Ghi chú                                                             |
| ------------- | ------------ | ------------------------------------------------------------------- |
| Dữ liệu dương | `#00675A`    | Xanh rêu — nền cell + chữ trắng                                     |
| Dữ liệu âm    | `#822333`    | Đỏ mận — nền cell + chữ trắng                                       |
| Link / title  | `#D17B19`    | Thường dùng cho tiêu đề bảng "Global Markets…", nhãn Equities/Bonds/Currency, CTA `click here` — map Ochre Style Guide nếu gần |

```
/* PDF-specific semantic — chỉ data table Market Review */
--color-positive: #00675A;
--color-negative: #822333;
```

Hầu hết file nhóm A chỉ dùng **hai** fill phẳng (không gradient intensity theo độ lớn %). Sample fill dưới từng ô % trên PDF trước khi gán class — đừng suy đoán từ số nếu PDF để ô trắng.

### B.6.2 Heat table "Global Markets" — type Market Review (bắt buộc nhóm A)

Đặc trưng **type market-review** (`family-market-review` / `website/template-market-review.html`): bảng hiệu suất rộng — thường **7 cột** (tên chỉ số + CYTD / 1 Month / 3 Months / 1 Year / 3 Years (p.a.) / 5 Years (p.a.)), section **Equities → Bonds → Currency**.

Tham chiếu visual đã chốt (PDF April 2026 MMR + cùng family QMR/MMR): **lưới đen đầy đủ**, ô heat **khít tới border** — không khoảng trắng / “pill” giữa các ô màu (đây là lỗi HTML hay gặp khi `border: none` + `border-top` mờ + cột bị `width: 100%` giãn).

#### Quy tắc desktop (khớp PDF)

| Yếu tố | Quy tắc |
| ------ | ------- |
| Markup | `.mr-table-block` > title + `.mr-table-wrap` > `table.mr-table` + `<colgroup>` |
| Tiêu đề bảng | Sans (Proxima), Ochre/`#D17B19` (vd. `Global Markets – 30 April 2026`) — **không** Baskerville trừ khi PDF dùng serif |
| Section | `Equities` = `th.mr-table__group` ở thead cột 1; `Bonds` / `Currency` = `tr.mr-table__section` với **đủ 7 `<td>`** (ô số để trống, vẫn có border). **Cấm** `colspan="7"` (phá lưới) |
| Grid | Mọi `th`/`td`: `border: 1px solid #000`; table: `border-collapse: collapse; border-spacing: 0`. PDF vẽ hairline đen ngang + dọc quanh mọi ô |
| Heat | Class trên **`<td>`**: `.is-positive` (`#00675A` + chữ trắng), `.is-negative` (`#822333` + chữ trắng). Background phủ **cả ô tới mép border**; padding ~**2–4px**; text-align center |
| 0.0% | Theo fill PDF — April 2026: teal + trắng (`.is-positive`). Chỉ `.is-neutral` (nền trắng, chữ đen) khi PDF thật sự không tô |
| Cột | `table-layout: fixed`; `col.mr-table__col-label` ~**38%**; `col.mr-table__col-num` ~**10.333%** mỗi cột (PDF ≈ 188pt label + 6× ~50–57pt). Tránh cột tên ~50% làm khối số “lỏng” / trông như có gutter |
| Tên chỉ số | Cột 1: trái, nền trắng, mực đen; `white-space: nowrap` khi desktop cho phép |
| Source | `.mr-table-block__source` dưới bảng; `font-style: italic` khi PDF italic |
| Độ rộng | `width: 100%` + `min-width: ~640px` trong wrap — desktop đủ 7 cột như PDF |

**Không:** zebra, sticky header giả, shadow/card, `border-spacing > 0`, chỉ `border-top` xám nhạt, nền heat trên `<span>` bên trong ô, đổi sang xanh lá/đỏ dashboard.

#### Markup chuẩn (template)

```html
<section class="mr-table-block" aria-label="Global Markets">
  <h3 class="mr-table-block__title">Global Markets – <!-- date --></h3>
  <div class="mr-table-wrap">
    <table class="mr-table">
      <colgroup>
        <col class="mr-table__col-label" />
        <col class="mr-table__col-num" /><!-- ×6 -->
      </colgroup>
      <thead>
        <tr>
          <th scope="col" class="mr-table__group">Equities</th>
          <th scope="col">CYTD</th>
          <th scope="col">1 Month</th>
          <th scope="col">3 Months</th>
          <th scope="col">1 Year</th>
          <th scope="col">3 Years<br />(p.a.)</th>
          <th scope="col">5 Years<br />(p.a.)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><!-- Index --></td>
          <td class="is-positive">0.5%</td>
          <td class="is-negative">-1.2%</td>
          <!-- … -->
        </tr>
        <tr class="mr-table__section">
          <td>Bonds</td>
          <td></td><td></td><td></td><td></td><td></td><td></td>
        </tr>
        <!-- Currency section: same 7-cell pattern -->
      </tbody>
    </table>
  </div>
  <p class="mr-table-block__source">Source: Bloomberg <!-- … --></p>
</section>
```

#### CSS chuẩn (rút từ `template-market-review.html` — giữ đồng bộ khi sửa template)

```css
.mr-table {
  width: 100%;
  min-width: 640px;
  border-collapse: collapse;
  border-spacing: 0;
  table-layout: fixed;
  font-family: var(--font-sans);
  font-size: var(--mr-table-cell-size);
  line-height: 1.25;
  background: #fff;
}
.mr-table col.mr-table__col-label { width: 38%; }
.mr-table col.mr-table__col-num { width: 10.333%; }
.mr-table th,
.mr-table td {
  padding: 2px 4px;
  text-align: center;
  vertical-align: middle;
  border: 1px solid #000; /* full grid — cells abut */
  background: #fff;
  box-sizing: border-box;
}
.mr-table th:first-child,
.mr-table td:first-child {
  text-align: left;
  padding-left: 6px;
  white-space: nowrap;
}
.mr-table thead th.mr-table__group {
  color: var(--mr-table-title-color, #d17b19);
  text-align: left;
}
.mr-table .is-positive {
  background: var(--color-positive); /* #00675A */
  color: #fff;
  text-align: center;
}
.mr-table .is-negative {
  background: var(--color-negative); /* #822333 */
  color: #fff;
  text-align: center;
}
.mr-table .is-neutral {
  background: #fff;
  color: #000;
  text-align: center;
}
.mr-table tr.mr-table__section td {
  background: #fff;
  color: var(--mr-table-title-color, #d17b19);
  text-align: left;
  padding: 4px 6px;
  border: 1px solid #000;
}
.mr-table-block__source {
  margin: 6px 0 0;
  font-size: var(--mr-caption-size);
  font-style: italic; /* when PDF italic */
}
```

#### Sai lệch đã sửa (đừng tái phạm)

| HTML sai | PDF đúng |
| -------- | -------- |
| `border: none` + `border-top: 1px solid rgba(0,0,0,.06)` | Lưới đen đủ cạnh mọi ô |
| Ô heat trông như khối rời / gutter trắng | Nền màu sát border; `border-spacing: 0` |
| `colspan="7"` cho Bonds/Currency | 7 ô riêng, giữ cột dọc |
| Cột tên quá rộng (~half table) | ~38% / ~10.3% qua `colgroup` |
| Source roman mặc định | Italic nếu PDF italic |

#### QA desktop bảng (trước khi responsive)

1. So side-by-side với trang bảng PDF: lưới đen liên tục, không “ô nổi”.
2. Equities / Bonds / Currency đúng chỗ + màu Ochre.
3. Mọi ô % có class đúng fill PDF; chữ trắng trên teal/maroon.
4. Source một dòng dưới bảng.

### B.6.3 Heat table — mobile / tablet (responsive thân thiện)

Desktop fidelity trước (C.6.10). Trên viewport hẹp:

1. **Giữ bảng thật** (`<table>` + lưới đen + heat) — không card-stack từng chỉ số.
2. `.mr-table-wrap { overflow-x: auto; -webkit-overflow-scrolling: touch; }` — scroll ngang **cục bộ**; `document.scrollWidth` không vượt viewport.
3. Giữ `min-width` trên `.mr-table` để mật độ cột giống desktop khi vuốt.
4. Cho phép giảm `--mr-table-cell-size` nhẹ; heat + chữ trắng đủ contrast; grid vẫn `1px solid #000`.
5. Tuỳ chọn: sticky cột tên (`position: sticky; left: 0; background: #fff; z-index: 1`) — không bắt buộc.
6. QA: vuốt hết CYTD…5Y; section + source còn đủ; không mất màu heat.

## B.7 Biến thể theo nhóm tài liệu

### Nhóm A — Market Review

- Trang bìa: hero cao ~150–200pt (vd. April 2026 MMR ≈ **184pt**), **title overlay** trên ảnh (Baskerville lớn; dòng tháng/năm caps — đôi khi **hai cỡ** trong một dòng, vd. APRIL 21pt + 2026 26pt), **không logo trên hero** trừ khi PDF có.
- **Vị trí chữ hero** — bắt buộc khớp PDF (**B.7.1**): cùng mép trái với thân bài; pad-top theo y đo được — **không** dùng `5vw` gutter làm lệch cột.
- **Heat table** — bắt buộc khớp PDF (**B.6.2**): lưới đen đầy đủ, ô heat khít border, `colgroup`, không `colspan` section.
- **Spacing** — dense rhythm theo PDF (**B.7.3**): token `--mr-para-gap` / `--mr-section-gap-*` / `--mr-chart-block-gap-*`; không dùng spacing Perspective rộng.
- Scrim: đo opacity/fill PDF (vd. xám-đen ~**0.65**) — không để chữ trắng trên ảnh sáng.
- Thân bài dày hơn (PDF ~9–10pt) vì nhiều bullet + bảng; list thường **Flush** (B.9).
- **Hai khối số liệu đặc trưng** (bắt buộc xử lý đúng — xem B.6.2–B.6.3 và B.7.2):
  1. **Heat table** "Global Markets" (ô tô màu dương/âm)
  2. **Lưới 6 chart** (2×3 desktop → stack mobile)
- CTA / note (nếu PDF có): vd. `click here` màu `#D17B19` **+ underline ochre** khi PDF có hairline (April); `text-underline-offset: 2px` — có khe trắng nhỏ dưới chữ (không `0` kẻo gạch chen vào glyph; không ~0.12–0.15em kẻo quá rộng). `text-decoration-skip-ink: none` nếu PDF là hairline liền. Không để `text-decoration: none` rồi chỉ underline lúc hover. Note box nền `#EAEFF1` / `#eaedf1`, pad-y đủ thoáng (`--mr-note-pad-y`), gap CTA→note / note→footer qua `--mr-cta-gap-after` / `--mr-note-gap-after`. CTA thường **left** align, không center nếu PDF full-measure.
- Footer: dải **nền tối** + contacts B.5 + legal; email/www **underline trắng** + Proxima Regular (B.5.6); city Baskerville; logo footer **chỉ khi PDF có**.

**Template HTML tái sử dụng:** `website/template-market-review.html`  
Token `--mr-*` + geometry (B.7.1) + spacing (B.7.3); class `family-market-review`. Convert: copy template → đo PDF → override tokens → điền heat table + 6 chart + dark footer (B.5.4). Mobile: lề trái/phải `--gutter: 20px` như Perspective (B.7.1); hero nới tỉ lệ (B.4); table scroll-x (B.6.3); chart stack (B.7.2); contacts 2 cột (B.5).

### B.7.1 Hero overlay placement (nhóm A) — desktop khớp PDF

Title/date nằm **trên ảnh**. Sai lệch thường gặp: chữ quá cao / lề trái hẹp hơn body (do `clamp(..., 5vw, ...)`).

**Đo trên PDF (pt), cùng hệ toạ độ trang:**

| Token | Đại lượng | Ví dụ April 2026 MMR |
| ----- | --------- | -------------------- |
| `--mr-page-w-pt` | Chiều rộng trang | `594.96` |
| `--mr-content-x-pt` | `x0` của title **và** dòng body đầu | `85.08` (phải trùng) |
| `--mr-content-x-right-pt` | lề phải = `pageW − body/table x1` (thường **hẹp hơn** trái) | April ≈ `55.28` (không pad đối xứng 85 — cột sẽ hẹp, text wrap sớm, bảng scroll) |
| `--mr-hero-title-y-pt` | `y0` mép trên title | `55.28` |
| `--mr-hero-aspect` | W trang / H dải hero | `594.96 / 183.78` |

**CSS (desktop) — trong template:**

```css
.container {
  padding-left: max(20px, calc(100% * var(--mr-content-x-pt) / var(--mr-page-w-pt)));
  padding-right: max(20px, calc(100% * var(--mr-content-x-right-pt, var(--mr-content-x-pt)) / var(--mr-page-w-pt)));
}
.mr-hero__inner {
  padding-top: max(16px, calc(100% * var(--mr-hero-title-y-pt) / var(--mr-page-w-pt)));
}
```

`padding-%` tính theo **chiều ngang** containing block (= shell/hero width) → khi `--page-max` = khổ PDF, offset px = `pt × 96/72`, khớp bản in. Heat table desktop: `min-width: 0` + `overflow-x: visible` (khớp bề rộng cột); chỉ mobile mới `min-width` + scroll trong `.mr-table-wrap`.

**QA desktop (bắt buộc):**

1. Cạnh trái title = cạnh trái đoạn body đầu (một cột dọc).
2. Khoảng từ mép trên hero → mép trên title ≈ `title_y / band_H` chiều cao hero (không dính sát top, không “treo” giữa band nếu PDF không vậy).
3. Date sát dưới title (`--mr-date-gap` thường ~0); nếu PDF hai cỡ (APRIL/2026) dùng `.mr-hero__month` / `.mr-hero__year`.
4. Cột nội dung đủ rộng để wrap giống PDF (đo `x1` body/table — **không** pad phải = pad trái nếu PDF lệch); bảng Global Markets **không** scroll ngang trên desktop.
5. **Desktop:** **không** dùng `padding-inline: clamp(20px, 5vw, …)` cho cột nhóm A — dùng `--mr-content-x-pt` / `--mr-content-x-right-pt`.

**Mobile (≤768px) — lề trái/phải = Perspective:**

- `.container { padding-left/right: var(--gutter) }` với `--gutter: 20px` — **cùng** `template-perspective.html`.
- **Không** giữ `calc(100% * --mr-content-x-* / --mr-page-w-pt)` trên mobile (shell hẹp → pad ~36–56px, lệch Perspective).
- Hero title cùng mép body nhờ chung `.container`; nới `aspect-ratio` / `--mr-hero-pad-top` (B.4).

### B.7.2 Chart grid nhóm A — desktop giống PDF, mobile dễ đọc

PDF thường đặt **6 panel** cùng một trang (Global Equity Performance / Valuations / Inflation / Bond Index / PMIs / AUD-USD…). Mỗi panel gồm: title + subtitle/date, plot (trục Y đôi khi **mirror trái+phải**), legend, `Source: LSEG Datastream` (hoặc tương đương).

| Yếu tố           | Desktop (khớp PDF)                                                                                          | Mobile / tablet                                                                 |
| ---------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Asset            | **Tách 6 ảnh** (clip từng panel) — `chart-01` … `chart-06` dưới `assets/<slug>/images/`                     | Cùng 6 ảnh                                                                      |
| Layout           | CSS grid **2 cột × 3 hàng** (`.mr-chart-grid`) — cùng thứ tự đọc PDF (trái→phải, trên→dưới)               | **1 cột**, full content-width; `order` giữ thứ tự PDF                           |
| Composite        | **Cấm** xuất một PNG/JPEG gộp 6 chart rồi `img` co nhỏ trên mobile (chữ trục/legend không đọc được)         | —                                                                               |
| Source / title   | Nếu đã nằm **trong** ảnh clip → **không** lặp figcaption trùng; nếu tách text ngoài ảnh → caption theo PDF | Giữ như desktop                                                                 |
| Gap              | `--mr-chart-gap` đo khoảng gutter PDF giữa panel                                                            | Gap dọc đủ để không dính hai chart                                              |
| Kích thước       | Mỗi panel co trong nửa content column; `max-width: 100%; height: auto`                                      | Full width cột; tránh fixed height kéo méo tỉ lệ                                |
| QA               | So side-by-side với trang chart PDF: đủ 6, đúng thứ tự, không mất source                                    | Mỗi chart đọc được trục/legend; không horizontal page scroll                    |

Thứ tự đọc mẫu (April 2026 MMR — xác nhận lại từng PDF):

1. Global Equity Market Performance  
2. Global Equity Valuations  
3. U.S., Aust & German Headline Inflation  
4. U.S. & Aust 10 Yr Government Bond Index  
5. Manufacturing PMIs  
6. AUD/USD FX Rates  

### B.7.3 Spacing rhythm — type Market Review (text + images)

Nhóm A **dày hơn** Perspective: leading và gap giữa khối nhỏ. Sai lệch hay gặp: dùng `--space-3` (16px) / `--space-5` (32px) / `--space-6` (48px) làm mọi margin → trang “thoáng” quá so với PDF.

**Đo PDF (pt → px @ 96dpi ≈ ×4/3).** Ví dụ April 2026 MMR:

| Junction | PDF (pt) | Token web (gợi ý) | Ghi chú |
| -------- | -------- | ----------------- | ------- |
| Hero bottom → first body | ~14.4 | `--mr-band-gap: 19px` | `.mr-article { padding-top }` |
| Within-para leading | ~12.2 / 10 | `--mr-body-lh: 1.22–1.28` | Không dùng 1.5 Style Guide body |
| Body para → para | ~6.5 | `--mr-para-gap: 9px` | `.mr-body > p` margin-bottom |
| Body/list → h2 | ~5–6 | `--mr-section-gap-before: 10px` | Margin collapse với para/list dưới |
| h2 → list/body | ~3–4 | `--mr-section-gap-after: 6px` | |
| Bullet item → item | ~6 | `--mr-list-item-gap: 8px` | `li:last-child { margin-bottom: 0 }` |
| After list block | ~6–10 | `--mr-list-block-gap: 10px` | |
| Before/after heat table | ~6–12 | `--mr-table-block-gap: 12px` | |
| Table → chart grid | (page break trên PDF) | `--mr-chart-block-gap-before: 28px` | Continuous web — vừa đủ tách khối |
| Chart panel gutter | row ~6 / col ~48 | `--mr-chart-gap` + `--mr-chart-gap-col` | |
| Charts → CTA | ~18 | `--mr-chart-block-gap-after: 24px` | |
| CTA → note | ~14–24 | `--mr-cta-gap-after: 28px` | Clearspace tới mép grey box |
| Note pad | ~10–12pt | `--mr-note-pad-y` / `--mr-note-pad-x` | Tránh box bị “bẹp” |
| Note → footer | ~17 | `--mr-note-gap-after: 24px` + footer pad | |
| Article → footer | — | `--mr-article-pad-bottom: 8px` | Tránh cộng dồn với footer `padding-top` |

**Template:** `website/template-market-review.html` — mọi margin khối article/chart/CTA/note dùng `--mr-*-gap*`, **không** hard-code `--space-5/6` cho rhythm nội dung.

**Cảnh báo CSS:** `.mr-cta` / `.mr-note` thường là `<p>` trong `.mr-body` — phải dùng `.mr-body > p.mr-cta` / `.mr-body > p.mr-note` (hoặc specificity tương đương) kẻo bị `.mr-body > p { margin-bottom: var(--mr-para-gap) }` ghi đè gap CTA/note.

**QA:** so PDF vs HTML — mật độ đoạn intro, khoảng h2 Australia/International, gap trên/dưới lưới chart và CTA; không để “lỗ” 32–48px giữa mọi section trừ khi PDF có clearspace tương đương.

### Nhóm B — Quarterly Outlook

Token `--qo-*` + class `family-quarterly-outlook`. Convert: copy `website/template-quarterly-outlook.html` → đo PDF → override tokens → điền title/byline/body/split/quote + dark back cover (B.5.4). Tham chiếu PDF: March 2026 *Equities: the tug of war*; June 2026 *Still waters run deep*.

- Trang bìa: logo stacked **`MT-Logo.svg` căn giữa** trên hero, đường kẻ ngang (`.qo-hero__rule`), kicker serif **"Quarterly Outlook"** (trắng, ~39pt). **Logo rộng đúng ½ kicker** — wrap `.qo-hero__brand` (`width: max-content`) + `.qo-hero__logo { width: 50% }` (không `--qo-logo-width: 360px`). **Tiêu đề bài viết cụ thể** nằm **dưới ảnh** trên nền trắng (`.qo-article__title`, Baskerville ink — không overlay như nhóm A).
- **Body rhythm dày** như PDF: `--qo-para-gap: 8px` (~6–7pt giữa đoạn); `--qo-body-lh: 1.28` (PDF ~1.2); list `--list-item-gap: 4px`; byline → body ~10px — không dùng `--space-5` / 1.45 Perspective.
- Byline PDF *"Written by [Tên] | [ngày]"* → `.qo-byline` **một lần** trong article; **không** lặp running footer / số trang.
- **Hai kiểu section head** (đừng nhầm với numbered list B.9). Selector lede/display **phải thắng** `.qo-body h2` (nếu không, heading bị serif lớn + màu bịa):
  - **Màu heading:** đo HEX PDF, so với `#CB962E`. Cùng tông vàng nhạt → map Ochre. Khác rõ (June numbered + Asset class views + views h3 = **`#D17B19`**) → `--qo-section-color` / `--qo-section-lede-color: #d17b19` — **không** `#CB962E`.
  - **June:** `.qo-section` Baskerville ~16pt + `#D17B19` — `<span class="qo-section__num">1.</span>` + heading.
  - **March lede:** `.qo-section.qo-section--lede` **Proxima, cùng cỡ thân bài** (`--qo-section-lede-size: var(--qo-body-size)`). Đo màu lede từng PDF; `#CBA020` gần Ochre thì map `#CB962E`, `#D17B19` thì giữ. Không dùng Baskerville lớn cho lede.
  - **March display** (hiếm): `.qo-section--display` Baskerville cỡ H1, mực `--color-ink` (vd. *Positioning portfolios for the decade ahead*).
- **Callout/pull-quote** (`.qo-quote`): nền đo từ PDF rồi map Light Grey `#F4F4F4` khi gần; March fill ≈ `#EEEEEE`. Quote **Baskerville roman** trừ khi PDF italic; attribution sans, thường **căn phải**. Không invent italic.
- **2 cột text + chart** — **đo bbox PDF**, không mặc định 50/50 và **không cap 320px**:
  - `.qo-split`: `--qo-split-text-fr` / `--qo-split-media-fr` (March p0 ≈ **38fr / 62fr** — text ~176pt, chart ~284pt).
  - `.qo-float`: chart `float: right; width: var(--qo-float-media-pct)` (March ≈ **61%**); pie rộng `--qo-float-media-pct-wide` ≈ **68%**. Gutter `--qo-split-gap` ~8–10px.
  - Mobile: stack full width. **Một ảnh mỗi chart** — không composite.
- Lề nội dung nhóm B trái ~**72pt**; **phải đo từng PDF** (March chart x1 ~540pt → `--qo-content-x-right-pt: 55`). Desktop pad `%` từ page W; **mobile ≤768: `--gutter: 20px`**.
- Body: **10pt / 13.33px** Proxima (`--qo-body-size`) — không bump 14px. Mực `--color-ink` `#000000` (PDF `#1B1B20` map Black).
- **Inline link (nhóm B):** đo từng PDF — **colour, italic, underline**. June 2026 (*Strategic Defence*, *Behind the façade*, *The security of everything*, *connect*): `#D17B19` (cùng heading, không `#CB962E`), **italic** (`<em>` trong `<a>`), **không** class `is-underlined` — gạch 1px HTML nặng hơn hairline PDF ~0.24pt và trông như bịa. Hover được gạch nhẹ. `--color-link: #d17b19`.
- **Back cover** `.qo-footer`: **ngoại lệ A4** — đây là trang cuối PDF (nền `#1B1B20`); trên web là **một slab** `min-height: calc(var(--page-max) * var(--qo-page-h-pt) / var(--qo-page-w-pt))` ≈ chiều cao A4 trong shell (không phải nhiều `.document-page`). Logo stacked + tagline trong `.qo-footer__brand`. Đo March 2026 p.6:
  - trước logo `--qo-footer-pad-top` ≈ **297pt** (~396px)
  - logo → tagline `--qo-footer-logo-gap` ≈ **29pt**
  - tagline → contacts `--qo-footer-brand-gap` ≈ **246pt** (~328px)
  - sau legal `--qo-footer-pad-bottom` ≈ **54pt**
  Mobile: bỏ `min-height` A4, pad nhỏ hơn. Contacts + disclaimer 3 đoạn (B.5.1). Không lặp running footer / số trang.

| Token | Đo từ PDF | Ghi chú |
| --- | --- | --- |
| `--qo-page-w-pt` / `--page-max` | page W | A4 ≈ 594.96pt → ~793px |
| `--qo-content-x-pt` | x0 body (~72) | không 5vw; không pad A/C ~55pt |
| `--qo-content-x-right-pt` | x1 chart/body | March ~55pt (chart → 540pt); đo từng file |
| `--qo-hero-aspect` | page W / hero H | March ≈ `594.96 / 224.6` |
| `--qo-kicker-size` | "Quarterly Outlook" trên ảnh | ~39pt |
| Hero logo width | **½ kicker** | `.qo-hero__brand` + `.qo-hero__logo { width: 50% }` |
| `--qo-body-size` | body 10pt | **13.33px** — không 14px |
| `--qo-para-gap` | ~6–7pt giữa đoạn | `8px` — không 14–16px web default |
| `--qo-body-lh` | PDF ~1.2 | `1.28` web |
| `--qo-title-size` | H1 dưới ảnh | March 20pt; June ~28pt |
| `--qo-section-lede-size` | = body | Proxima; màu `--qo-section-lede-color` (đo PDF — June `#D17B19`) |
| `--qo-split-text-fr` / `--qo-split-media-fr` | bbox text vs chart | March p0 **38fr / 62fr** — không 50/50 |
| `--qo-float-media-pct` | chart share khi wrap | March **61%**; wide pie **68%**; không `min(48%, 320px)` |
| `--qo-page-h-pt` | page H | A4 ≈ 842pt — dùng cho `min-height` back cover |
| `--qo-footer-pad-top` | trước logo ~297pt | `calc(page-max * 297 / page-w)` ≈ 396px |
| `--qo-footer-logo-gap` | logo → tagline ~29pt | calc từ page-max |
| `--qo-footer-brand-gap` | tagline → contacts ~246pt | ≈ 328px — không 88px |
| `--qo-footer-pad-bottom` | sau legal ~54pt | calc từ page-max |
| `--qo-footer-logo-width` | stacked footer ~190pt | `200px` |

**QA desktop:** logo hero = ½ width kicker; H1 + body cùng mép trái; lede = body size Proxima Ochre; text|chart % khớp bbox PDF; **footer slab cao ≈ A4** (pad trước logo + sau tagline như PDF p.cuối); quote upright nếu PDF roman.

### Nhóm D — White Paper

- **Khổ trang PDF:** bìa dọc A4 (p0) + **spread ngang 2×A4** (1191×842pt) cho p1–p31 + trang cuối dọc (p32).
- **Layout web:** **một trang một hàng** trên mọi viewport — mỗi `.wp-spread__page` stack dọc, `max-width: var(--page-max)`. Trang đơn (cover/back) dùng `.wp-single`. **Không** ghép 2 cột spread desktop (đã thử — revert về 1 trang/hàng).
- **Bỏ qua nửa/trang trống:** Spread PDF mà một bên **chỉ nền một màu, không text/ảnh/logo** → **không render** bên đó trên web (vd. p1 trái đen trống — chỉ giữ cột phải Purpose).
- **Shell width:** `--page-max` ≈ 794px (1 A4); `--wp-page-height` = chiều cao A4 trong shell.
- **Body:** Proxima **12pt → `--text-regular` (16px)** — alias Style Guide giống Perspective (C), **không** 13.33px Outlook/MMR.
- **Heading/subhead:** Baskerville **`--text-h5` (24px)** cho `.wp-body h2` / `.wp-subhead`; **`--text-h3` (40px)** cho section opener / display title — cùng token `--text-*` với templates A/B/C; mobile **`--text-h5: 20px`**, **`--text-h3: 28px`**.
- **Typography map (bắt buộc):** mọi cỡ chữ Nhóm D dùng token Style Guide `--text-*` trong template — **không** hard-code px/pt rời cho body/h2/opener trừ token `--wp-*` đo từ PDF (quote 22pt, stat numbers, legal 7pt…).
- **Accent vàng PDF:** `#dd971a` — giữ HEX nguồn; không map `#CB962E` / `#D17B19` nếu mắt thấy khác.
- **Component đặc trưng:** bìa tối + co-brand; purpose band đen + monogram; TOC chấm dẫn + số trang vàng; section opener 30pt trắng; stat SC700; case study; bảng so sánh Family Office; Gemstone infographic; contributors.
- **Chunked build (PDF >10 trang):** state `.pdf-chunks.json`; mỗi chunk ≤10 trang PDF; append HTML trước marker `<!-- wp-chunk:N pending -->`; chunk `completed` không rebuild trừ khi retry.

**Template:** `website/template-white-paper.html` — token `--wp-*`, class `family-white-paper`. Skeleton markup cho mọi panel p9+ nằm trong comment **TYPE D COMPONENT CATALOG** cuối `<main>`.

**Component catalog (gặp PDF → class — bắt buộc):**

AI copy markup từ template, điền copy/SVG/màu đo PDF. **Không** invent class mới trong file bài; **không** composite PNG.

**Gặp layout mới (chưa có trong bảng dưới):**

1. Đo PDF (fill, font, bbox, thứ tự DOM).
2. Thêm vào **`website/template-white-paper.html`**: token `--wp-*` → CSS `.wp-*` → comment skeleton trong khối `TYPE D COMPONENT CATALOG`.
3. Thêm **một hàng** vào bảng lookup này + ghi chunk/trang PDF nguồn.
4. **Rồi mới** dùng class đó khi build `why-the-modern-family-office-matters.html` (hoặc white paper sau).
5. Không để markup “chỉ sống” trên trang bài — lần sau AI phải tìm được trên template.

Cùng pattern, khác nhấn mạnh → modifier (`.wp-model-card--accent`, `.wp-era--accent`, `.wp-callout-stack`), không tách class song song.

| PDF pattern | Class | Ghi chú |
| ----------- | ----- | ------- |
| Bìa 3 vùng | `.wp-cover` | Footer logos căn trái |
| Purpose đen + monogram | `.wp-purpose` | `background-image` `#000c1d` |
| Gạch dưới title một phần | `.wp-title-rule` / `__mark` | Không `text-decoration` |
| TOC | `.wp-toc` | Số trang vàng |
| Section opener trên ảnh | `.wp-section-opener` | Overlay / inset |
| Bullet body vàng | `.wp-list` | Không browser default |
| Quote **cả trang** Baskerville roman | `.wp-pull-panel` + `.wp-pull-quote` | p4 — attrib ALL CAPS |
| Quote **trong body** italic sans | `.wp-callout` | p11–13, p20 — attrib sentence case |
| Nhiều callout + bullet catalytic | `.wp-callout-stack` | p10 trái |
| Lưới số 3 cột | `.wp-stat-board` | HTML + SVG icon |
| Donut + legend | `.wp-donut-panel` | SVG path PDF, không arc `A` |
| Byline portrait | `.wp-byline` | Nền `#f1f1f2`; render PDF nếu extract đen |
| Case study beige | `.wp-spread__page--case-study` | `#faefe0` trên **page** |
| 4 card SFO/BFO/VFO/MFO | `.wp-model-grid` | MFO = `--accent` |
| Bảng Model / Strengths / Challenges | `.wp-compare-table` | Bullet **ink**, không vàng |
| Timeline Wealth 1.0–3.0 | `.wp-era-grid` | 3.0 = `--accent` |
| Gemstone 5 facets | `.wp-gemstone` | SVG PDF, không PNG ghép |
| 3 kiểu wealth transfer thành công | `.wp-outcome-list` | p20 |
| Contributors | `.wp-contributors` | Tên Medium caps vàng |
| About + logo | `.wp-about` | p28–29 trái |
| Contact offices | `.wp-offices` + `.wp-spread__page--offices` | `tel:` |
| Footnotes i–xvi | `.wp-endnotes` | p30 |
| Legal / back cover | `.wp-legal` / `.wp-back` | Bỏ nửa đen trống p31 phải |
| Body liên tục nhiều trang in | `.wp-spread--flow` | Gap `--wp-intra-block-gap` |

**Hai quote — không trộn:**

| | `.wp-pull-quote` (p4) | `.wp-callout` (p11+) |
|--|----------------------|----------------------|
| Container | Full page `.wp-pull-panel` | In-flow beige box |
| Quote | Baskerville **roman** 22pt vàng | Proxima **italic** body-size vàng |
| Attribution | ALL CAPS 8pt Light | Sentence case, không italic |

**Markup — callout / model grid / compare table / era / gemstone / outcomes / contributors:** xem comment catalog trong `template-white-paper.html` (khối `TYPE D COMPONENT CATALOG`).

**Chunk build tiếp (pilot):** 3 = p9–p13 (opener S2, model-grid, callout, compare-table); 4 = p14–p18 (era-grid, gemstone, case study); 5 = p19–p25 (facets + outcome-list); 6 = p26–p32 (contributors, about, offices, endnotes, legal, back).

**Markup spread (bắt buộc):**

```html
<div class="wp-single"><!-- p0 cover --></div>
<div class="wp-spread wp-spread--purpose">
  <div class="wp-spread__page wp-spread__page--dark wp-purpose">…</div>
  <!-- p1 trái đen trống: bỏ qua -->
</div>
<div class="wp-spread">
  <div class="wp-spread__page wp-spread__page--left">…</div>
  <div class="wp-spread__page wp-spread__page--right">…</div>
</div>
```

**Layout:** `.wp-spread { grid-template-columns:1fr; max-width:var(--page-max) }`. Trang **text** — chiều cao theo nội dung (không `min-height: A4`). Trang **visual** — ảnh `height: auto` desktop (tỷ lệ gốc); cover mobile `100vh`.

**Vertical rhythm web (UX — thu gọn khoảng trống pagination PDF):**

Nguyên tắc giống nhóm B QO (`template-quarterly-outlook.html`: `--qo-band-gap`, `--qo-para-gap`, không ép slab A4 cho body liên tục). **Không** copy pad PDF lớn (72pt, 105pt, 147pt) lên web nếu chỉ là khoảng trống cuối trang in.

| Token | Desktop | Mobile | Dùng cho |
| ----- | ------- | ------ | -------- |
| `--wp-surface-pad-top` / `--wp-surface-pad-bottom` | 48px / 32px | 32px / 32px | **Trang có nền màu** (`.wp-purpose`, `.wp-pull-panel`) — `padding-block` trên phần tử **có background**, tạo breathing room như PDF |
| `--wp-page-pad-start` / `--wp-page-pad-end` | 51.3pt / 55pt scaled | `20px` (`--gutter`) | **`padding-inline` trên `.wp-spread__page`** (text/toc/purpose); pull-quote panel dùng inline trên `.wp-pull-panel` |
| `--wp-title-gap-after` | 32px | 24px | Title + partial rule → body (Purpose, TOC, Welcome, Introduction) |
| `--wp-section-head-gap` | 24px | 24px | **Heading ↔ khối liền kề** (`.wp-body h2` / `.wp-subhead`): cùng gap **trên và dưới**. Không dùng `--wp-section-gap` (48px) làm margin-top heading. Đoạn ngay trước heading: `margin-bottom: 0` (`:has(+ h2)`) để không cộng `--wp-para-gap` |
| `--wp-ack-gap-before` | 48px | 32px | Copy chính → legal/ack (Purpose) — **không** `margin-top: auto` |
| `--wp-block-gap` | 48px (`--wp-page-gap`) | 32px (`--space-5`) | **`margin-top` trên `.wp-spread__page`** — chỉ khi **tách khối thật** (section mới, visual page, TOC, cover↔body). **Không** dùng cho nội dung liên tục bị cắt bởi pagination PDF |
| `--wp-intra-block-gap` | 24px (`--space-4`) | 24px | Text ↔ ảnh/chart/stat **cùng page**; figure trong `.wp-body.wp-flow`; **gap giữa page cùng nội dung** (`.wp-spread--flow`) — **bằng** khoảng cách khối nội bộ thông thường |
| `--wp-quote-stack-gap` | 48px | 48px | Giữa hai `.wp-pull-quote` |

**Tránh:** `height/min-height: var(--wp-page-height)` trên trang text; `margin-top: auto` đẩy footer xuống đáy A4; title `margin-bottom: 105pt` PDF; **padding vertical trên inner panel** gây double gap khi stack pages; **`--wp-block-gap` giữa các đoạn body liên tục** chỉ vì PDF sang trang mới.

**Nội dung liên tục vs page block (bắt buộc):**

Ranh giới trang PDF **không** đồng nghĩa ranh giới HTML. Khi cùng một section/article dài trải nhiều trang in:

1. **Ưu tiên:** append copy vào **cùng** `.wp-body` / `.wp-flow` div trước — `<p>`, `<h2>`, `<ul>`, `<figure>` nối tiếp, **không** mở `.wp-spread__page` mới chỉ vì PDF hết trang. Ví dụ chunk 1: **Methodology** nối sau “What is a Family Enterprise?” trong **một** `.wp-body.wp-flow` — **không** `.wp-spread__page--right` riêng (tránh `--wp-block-gap` 48px).
2. **Không** thêm `--wp-block-gap` (48px) giữa các đoạn liên tục — khi bắt buộc tách wrapper DOM, dùng **`--wp-intra-block-gap`** (cùng gap khối nội bộ thông thường, 24px).
3. Trong **một** `.wp-body.wp-flow`: chỉ `--wp-para-gap` giữa đoạn; figure/stat/chart cách body bằng `--wp-intra-block-gap`.
4. **Chỉ tách page block + `--wp-block-gap`** khi có thành phần tách khối rõ: section opener / visual full-bleed, TOC, Purpose, pull-quote panel, cover↔body, section mới (Section 2, 3…).
5. Khi chunk build bắt buộc tách DOM: bọc chuỗi continuation bằng **`.wp-spread--flow`** — gap giữa page wrapper / spread liền kề = **`--wp-intra-block-gap`**, không `--wp-block-gap`.

```html
<!-- Đúng — body dài liên tục, một div -->
<div class="wp-spread wp-spread--flow">
  <div class="wp-spread__page">
    <div class="wp-spread__inner wp-body wp-flow">
      <p>… đoạn cuối trang PDF trái …</p>
      <p>… đoạn đầu trang PDF phải — cùng div, không page gap …</p>
      <section class="wp-donut-panel" aria-labelledby="wp-donut-title">…</section>
      <p>… tiếp tục …</p>
    </div>
  </div>
</div>

<!-- Chỉ khi cần tách wrapper (chunk) — flow chain, gap vừa phải -->
<div class="wp-spread wp-spread--flow">…page A…</div>
<div class="wp-spread wp-spread--flow">…page B continuation — margin-top: var(--wp-intra-block-gap) …</div>
```

**Page-block spacing (bắt buộc — desktop + mobile):**

- `.wp-spread__inner--left`, `.wp-spread__inner--right`, `.wp-spread__inner--below-band`, `.wp-purpose__inner`, `.wp-toc__panel` → **`padding: 0`**.
- **Không** dùng `margin-top` trên `.wp-spread + .wp-spread` — spacing chỉ trên **`.wp-spread__page`** (trừ `.wp-spread--flow`, xem trên):
  - `.wp-spread__page + .wp-spread__page` — mặc định `--wp-block-gap`; **`.wp-spread--flow .wp-spread__page + .wp-spread__page`** và **`.wp-spread--flow + .wp-spread--flow > .wp-spread__page:first-child`** → **`--wp-intra-block-gap`** (bằng gap khối nội bộ);
  - `.wp-single + .wp-spread > .wp-spread__page:first-child` — sau cover;
  - `.wp-spread + .wp-spread > .wp-spread__page:first-child` — sang spread mới (**`--wp-block-gap`** nếu section break; **`--wp-intra-block-gap`** nếu spread trước/sau đều `.wp-spread--flow`).
- Ảnh band / hero + body **cùng page**: `.wp-spread__page > .wp-spread__inner:not(:first-child) { margin-top: var(--wp-intra-block-gap) }`.
- Ảnh full-bleed trong page có text: negative `margin-inline` + `width` breakout trên `.wp-photo-hero`, `.wp-band`, `.wp-photo-band`.
- **Infographic / data panels:** xem mục **Infographic / data panels** bên dưới — **cấm composite PNG** cho stat board, donut/pie + legend; dùng `.wp-stat-board` / `.wp-donut-panel` HTML + SVG.

**Lề trái/phải content column:**

- Token `--gutter: clamp(20px, 5vw, 40px)` desktop; **`--gutter: 20px`** mobile — override `--wp-page-pad-*` trong `@media (max-width:768px)`.
- **`padding-inline: var(--wp-page-pad-start/end)`** trên `.wp-spread__page:has(> .wp-spread__inner | .wp-toc__panel | .wp-purpose__inner)` — **không** pad trên inner.
- `.wp-pull-panel`: `padding-inline` + **`padding-block: var(--wp-surface-pad-*)`** (nền beige full width page); vertical gap **giữa pages** vẫn từ page `margin-top`.
- **Trang nền màu** (`.wp-purpose`, `.wp-pull-panel`, **`.wp-spread__page--case-study`**): giữ **`padding-block`** (hoặc `padding-bottom` trên page case study) trên phần tử painted — **không** chuyển pad dọc sang inner; trang trắng thì inner `padding:0`, spacing giữa pages = `margin-top` trên `.wp-spread__page` only.
- Cover header: `padding-inline: var(--gutter)`; cover **footer logos**: `padding-inline: var(--wp-page-pad-start)` (cùng mép cột body).
- **Không** dùng `--content-inset` riêng — dùng `--wp-page-pad-*` / `--gutter`.

**Content column (desktop) — thống nhất mọi trang text:**

- Token `--wp-content-x-pt: 51.3` (trái), `--wp-content-x-right-pt: 55` (phải) — map vào `--wp-page-pad-start/end`.
- **Không** dùng pad trái khác nhau theo cột spread PDF (40pt / 95pt) trên web — mọi trang stack dùng **cùng mép trái**.
- Heading + body + list trong `.wp-body` **flush** cùng cột: `margin-inline:0; padding-inline:0` trên `h2, p, ol, ul`.

**Pilot:** `2023_Why_the_Modern_Family_Office_Matters.pdf` → `website/why-the-modern-family-office-matters.html` (6 chunks; chunk 1 = p0–p3 cover + purpose + front matter + TOC).

| Token | PDF | Ghi chú |
| ----- | --- | ------- |
| `--page-max` | 595pt A4 | ~794px — **1 trang / 1 hàng** |
| `--gutter` | Perspective shell | `clamp(20px, 5vw, 40px)`; **mobile 20px** |
| `--wp-content-x-pt` | ~51pt PDF | **51.3** — lề trái thống nhất mọi trang text |
| `--wp-content-x-right-pt` | ~55pt PDF | **55** — lề phải thống nhất |
| `--wp-page-height` | 842pt | `page-max × 841.89/595.28` |
| `--wp-body-size` | 12pt | **`var(--text-regular)`** — 16px |
| `--wp-h2-size` / `--wp-subhead-size` | ~16–20pt Baskerville | **`var(--text-h5)`** — 24px; mobile **`--text-h5: 20px`** |
| `--wp-section-opener-size` | ~30pt Baskerville | **`var(--text-h3)`** — 40px; mobile **`--text-h3: 28px`** |
| `--wp-cover-kicker-size` | 12pt | **`var(--text-regular)`** |
| `--wp-cover-title-size` | 45pt | 60px; mobile 42px |
| `--wp-cover-lines` | ngắt dòng PDF desktop | `<br class="wp-cover__br">` — ẩn mobile, hiện ≥769px |
| `--wp-quote-size` | 22pt | 29.33px |
| `--wp-quote-panel-bg` | `#faefdf` | Pull quotes p4 phải |
| `--wp-callout-bg` | `#fbf1e5` | Callout in-flow (p11+) — gần highlight, đo từng PDF |
| `--wp-quote-attrib-color` | `#7d8698` | Attribution pull + callout |
| `--wp-model-head` / `--wp-model-body` | `#eaeaed` / `#f3f3f4` | Card SFO/BFO/VFO + era 1.0/2.0 |
| `--wp-model-accent-head` / `--wp-model-accent-body` | `#f7e3c8` / `#fdf6ed` | MFO card + Wealth 3.0 |
| `--wp-byline-photo-bg` | `#f1f1f2` | Khung ảnh byline p5 — fill PDF phía sau portrait |
| `--wp-case-study-bg` | `#faefe0` | Nền full page case study (đo fill PDF spread phải) — **không** dùng `#faefdf` pull panel |
| `--wp-accent-gold` | `#dd971a` | TOC số trang, quotes, stat numbers |
| `--wp-stat-panel-bg` | `#f2f3f4` | Stat board panel chính |
| `--wp-stat-highlight-bg` | `#fbf1e5` | Stat board band 28.5% |
| `--wp-stat-number-size` | 49.33px (37pt) | `.wp-stat__number` |
| `--wp-stat-number-size-lg` | 53.33px (40pt) | `.wp-stat__number--lg` (28.5%) |
| `--wp-stat-unit-size` | 17.07px (12.8pt) | `.wp-stat__unit` MILLION/BILLION |
| `--wp-stat-growth-overlap-pt` | 5.562pt | 28.5% bbox → arrow bbox overlap; icon `margin-left` âm |
| `--wp-stat-growth-lift` | 0.2 | Icon `translateY` lên **20%** cỡ `.wp-stat__number--lg` (~9.7pt PDF) |
| `--wp-donut-seg-gold` | `#dd971a` | Segment lớn nhất donut (đo fill PDF) |
| `--wp-donut-seg-blue` | `#b4b9c3` | Segment xanh nhạt donut + legend dot |
| `--wp-donut-seg-slate` | `#7d8898` | Segment xám donut + legend dot |
| `--wp-donut-seg-cream` | `#f0cf9b` | Segment mỏng donut (arc fill PDF) |
| `--wp-donut-seg-cream-dot` | `#edc487` | Legend dot segment cream (fill legend PDF có thể khác arc) |
| `--color-surface-dark` | `#000000` | Purpose band nền đen tuyền PDF |
| `--wp-monogram-color` | `#000c1d` | Monogram watermark — rgb(0, 12, 29); **fill trực tiếp trong SVG**, không brighten web (`#001428`) |
| `--wp-title-rule-width-pt` | 48pt PDF | Gạch dưới **Introduction / section opener** (p5, p6…) |
| `--wp-title-rule-width-wide-pt` | 67.1pt PDF | Gạch dưới **Purpose** (p1) |
| `--wp-title-rule-gap-pt` | 2.34pt | Khoảng cách baseline → rule (mọi variant) |
| `--wp-list-bullet-color` | `#dd971a` PDF p5/p6 | Bullet body — vàng, không dot đen |
| `--wp-list-bullet-x-pt` | 17pt | Marker offset từ mép cột |
| `--wp-list-text-indent-pt` | 28.3pt | Text sau bullet |

**Cover p0 — layout 3 vùng (desktop khớp PDF):**

- `.wp-cover__frame` grid `auto \| 1fr \| auto` (header/footer theo nội dung; ảnh chiếm phần còn lại — PDF ~171/522/149pt).
- **Không** dùng `%` cố định cho header/footer nếu title 2 dòng bị clip — dùng `grid-template-rows: auto minmax(0, 1fr) auto`.
- **Full-bleed, không viền trắng** — bỏ inset border/padding quanh cover.
- **Header** nền đen: kicker + title; ngắt dòng desktop qua `<br class="wp-cover__br">` (ẩn ≤768px).
- **Photo:** ảnh p0 + `.wp-cover__photo-fade` gradient đen→trong suốt ~32% mép trên ảnh (title đọc được trên ảnh).
- **Footer:** `.wp-cover__footer` — `padding-inline: var(--wp-page-pad-start)` (cùng mép cột nội dung); `.wp-cover__brands` — logo MT + divider 1px + logo Uni Adelaide; **`justify-content: flex-start`** (căn trái, **không** căn giữa / chia 3 cột bằng nhau); asset trong `assets/<pdf-slug>/images/`.
- **Mobile ≤768:** `.wp-cover` và `.wp-cover__frame` — `aspect-ratio: auto; min-height: 100vh` (bìa cao tối thiểu full viewport).

```html
<div class="wp-cover__frame">
  <div class="wp-cover__header">…</div>
  <div class="wp-cover__photo"><img … /><div class="wp-cover__photo-fade"></div></div>
  <div class="wp-cover__footer"><div class="wp-cover__brands">…</div></div>
</div>
```

**Purpose band p1:**

- Nền `#000000`; trang cố định chiều cao A4 + `overflow: hidden`.
- **Monogram watermark:** `website/assets/MT-Monogram.svg` — **`fill: #000c1d`** trong file SVG (PDF rgb 0,12,29).
- **Cách render (đã thử):** dùng `background-image: url('assets/MT-Monogram.svg')` trên `.wp-purpose` — **không** dùng CSS `mask`, `::after` pseudo với mask, hay `<img>` overlay (monogram không hiện hoặc mất màu).
- Desktop: `background-position: calc(100% + 14%) calc(100% + 16%)`, `background-size: 86% auto`.
- Mobile: `background-position: calc(100% + 18%) calc(100% + 12%)`, `background-size: 92% auto`.
- `.wp-purpose__inner` — `background: transparent; z-index: 1` để monogram hiện qua vùng trống nội dung.
- **Title partial underline:** dùng component **`.wp-title-rule`** — **không** `text-decoration: underline` full-width, **không** CSS riêng từng trang.
- `.wp-purpose__title` + **`.wp-title-rule.wp-title-rule--wide`** (67.1pt).
- **Section opener** (ảnh nền + chữ trắng 30pt): wrapper **`.wp-section-opener`**; kicker **`.wp-section-opener__kicker`** (Proxima caps); title **`.wp-section-opener__title`**.
- Introduction (1 dòng): `class="wp-section-opener__title wp-title-rule"` → rule 48pt mép trái title.
- Section title nhiều dòng, rule dưới từ đầu dòng 2 (vd. “impact”): bọc từ trong **`<span class="wp-title-rule__mark">impact</span>`** — rule 48pt cố định, không full-width từ.
- Bullet list purpose (nền đen): marker `\2022` trắng tại `left: 15.3pt`, text indent `26.6pt`.
- **Bullet list body (nền trắng, p5/p6+):** marker `\2022` màu **`#dd971a`** (`--wp-list-bullet-color`) — **không** dùng dot tròn đen B.9. Đo PDF: bullet `x +17pt` từ cột content, text indent `28.3pt` (`--wp-list-bullet-x-pt`, `--wp-list-text-indent-pt`). Ordered list: số màu ink, cùng indent.

**Partial title rule — markup mẫu:**

```html
<!-- Purpose p1 -->
<h2 class="wp-purpose__title wp-title-rule wp-title-rule--wide">Mutual Trust’s Purpose</h2>

<!-- Introduction (p5) -->
<div class="wp-section-opener">
  <h2 class="wp-section-opener__title wp-title-rule">Introduction</h2>
</div>

<!-- Section 1 opener (p6) — rule under first word on line 2 -->
<div class="wp-section-opener">
  <p class="wp-section-opener__kicker">Section 1</p>
  <h2 class="wp-section-opener__title">
    The positive socio-economic<br />
    <span class="wp-title-rule__mark">impact</span> of wealthy families
  </h2>
</div>
```

**Infographic / data panels (HTML — cấm composite PNG):**

Panel số liệu / biểu đồ có legend trong White Paper **không** export thành một ảnh PNG ghép (body + chart). Build **semantic HTML + CSS**; vector (donut arc, icon mũi tên) = **inline SVG** từ path PDF khi có.

| Pattern PDF | Component | Quy tắc |
| ----------- | --------- | ------- |
| Lưới số + nền xám/beige | `.wp-stat-board` | HTML grid/flex; panel `--wp-stat-panel-bg` / `--wp-stat-highlight-bg`; **không** `p*-left-stats.png` composite |
| Donut/pie + legend bên phải | `.wp-donut-panel` | SVG path PDF + legend list; **không** `p*-left-chart.png` composite |
| Gemstone 5 facets | `.wp-gemstone` | SVG từ `get_drawings()`; **không** một PNG composite |
| 4 card operating models | `.wp-model-grid` | Cột 4 `--accent`; icon SVG |
| Bảng so sánh 3 cột | `.wp-compare-table` | `<table>` semantic; bullet ink |
| Timeline 3 era | `.wp-era-grid` | Cột 3 `--accent` |

**`.wp-stat-board` (stat panel):**

- Wrapper `.wp-stat-board`; từng vùng `.wp-stat-board__panel--primary` / `--highlight`.
- Divider giữa hàng: `.wp-stat-board__midrule` — đo **margin-top / padding-top / margin-bottom** từ PDF (pt → calc `--page-max`).
- Số lớn: `.wp-stat__number` (Baskerville SC, `--wp-accent-gold`); band highlight 28.5%: `.wp-stat-highlight`.
- **Icon vector:** inline SVG `<path>` extract PDF (vd. growth arrow 23.031×27.03pt `#dd971a`) — class `.wp-stat__icon--growth`; **không** PNG + clip wrapper che thừa.
- Overlap số ↔ icon: `--wp-stat-growth-overlap-pt` (`margin-left` âm trên icon); `--wp-stat-growth-lift` (`translateY` theo % `--wp-stat-number-size-lg`); số `z-index: 1` trên icon.

**`.wp-donut-panel` (donut + legend):**

- Nền panel: `--wp-stat-panel-bg` (`#f2f3f4`); padding 24/20pt scaled — giống stat panel.
- Layout: `.wp-donut-panel__grid` — **2 cột** chart \| legend desktop (~0.92fr / 1.08fr); **mobile ≤640px stack** (chart trên, legend dưới).
- **Donut SVG:** `viewBox="0 0 200 200"`; paths **extract trực tiếp từ PDF** (`get_drawings()` → `l`/`c` bezier) — **không** dùng arc tròn chuẩn (`A`) vì PDF dùng pie wedge + cạnh ngoài lõm (scooped) bên trái; lỗ trắng = path circle riêng (`fill: #fff`) phủ lên tâm.
- **Màu segment:** đo `fill` RGB từ PDF → hex token `--wp-donut-seg-*`.
- **Nhãn %:** vị trí bbox text PDF; chữ trắng Semibold ~9pt; legend 8pt Light — dot tròn 6.24pt, text trái, **% căn phải**; rule vàng 0.5pt trên title; title 10pt Semibold caps + `<sup>` footnote.
- Spacing tới body: `--wp-intra-block-gap` (trong `.wp-body.wp-flow` hoặc `.wp-spread__page > .wp-donut-panel { margin-top: … }`).
- Chart column: `justify-content: flex-start` (căn trái như PDF).

```html
<section class="wp-donut-panel" aria-labelledby="wp-donut-title">
  <div class="wp-donut-panel__grid">
    <div class="wp-donut-panel__chart">
      <svg class="wp-donut-chart" viewBox="0 0 200 200" role="img" aria-label="…">
        <path fill="var(--wp-donut-seg-cream)" d="…"/>
        <!-- arc segments + <text class="wp-donut-chart__label"> -->
      </svg>
    </div>
    <div class="wp-donut-panel__legend">
      <div class="wp-donut-panel__rule" aria-hidden="true"></div>
      <h3 class="wp-donut-panel__title" id="wp-donut-title">…<sup>iv</sup></h3>
      <p class="wp-donut-panel__lede">…</p>
      <ul class="wp-donut-legend">…</ul>
    </div>
  </div>
</section>
```

**QA infographic Nhóm D:** segment % khớp PDF; màu hex khớp fill vector; nhãn trong vòng đọc được; legend dot màu khớp segment; mobile stack không cắt chart; **không** horizontal scroll; copy legend verbatim.

**Case study page (nền beige full page):**

PDF spread phải có case study thường **fill cả nửa trang** màu beige (đo `get_drawings()` — pilot `#faefe0`), **khác** pull-quote panel `#faefdf`.

- Wrapper: **`.wp-spread__page--case-study`** trên page chứa `.wp-case-study` (+ `.wp-photo-band` nếu có).
- Nền: `background: var(--wp-case-study-bg)` trên **page wrapper** — không chỉ inner text, **không** nền trắng mặc định.
- `padding-bottom: var(--wp-surface-pad-bottom)` trên page modifier (breathing room cuối trang tinted).
- Ảnh band đầu trang: vẫn `.wp-photo-band` breakout full-bleed trong page; nền beige hiện quanh/dưới ảnh như PDF.
- Markup: `.wp-case-study` + `__label` / `__title` / body `<p>` + `__note` (privacy — 7pt Medium, không `.wp-footnote`).

```html
<div class="wp-spread__page wp-spread__page--right wp-spread__page--case-study">
  <figure class="wp-photo-band wp-photo-band--short">…</figure>
  <div class="wp-spread__inner wp-body">
    <div class="wp-case-study">…</div>
  </div>
</div>
```

**Tránh (pilot chunk 1):**

- Spread 2 cột desktop — gây lệch đọc web; giữ 1 trang/hàng.
- Render nửa spread trống (p1 trái đen) — bỏ hẳn DOM node.
- Viền trắng/inset quanh cover — PDF full-bleed.
- Grid row `%` cố định cover — clip dòng title thứ 2.
- Monogram `#001428` hoặc mask — dùng SVG `#000c1d` + `background-image`.
- Pad trái 40pt / 95pt theo cột spread — thống nhất `--wp-content-x-pt: 51.3`.
- Gạch chân title bằng `text-decoration` hoặc `::after` riêng từng component — dùng **`.wp-title-rule`** / **`.wp-title-rule__mark`**.
- **Composite PNG** cho stat board / donut / gemstone / model grid / compare table — dùng class catalog HTML+SVG.
- Layout PDF mới viết thẳng one-off trên trang bài, không lên template — lần convert sau không base được. Luôn: template CSS + catalog comment + hàng lookup MD **trước** khi dùng trên HTML bài.
- Cover footer logos **căn giữa** hoặc `flex: 1` chia cột — PDF căn **trái** (`justify-content: flex-start` trên `.wp-cover__brands`).
- Growth stat icon PNG + clip wrapper — dùng **inline SVG path** PDF + token overlap/lift.

**QA chunk 1 (p0–p3):** cover 3 vùng + gradient + footer logos; title 2 dòng desktop không clip; mobile cover ≥100vh; purpose monogram góc dưới-phải crop một phần, màu `#000c1d`; title underline 67.1pt; mọi trang text cùng mép trái 51.3pt; mobile gutter 20px; TOC số trang vàng `#dd971a`; không horizontal scroll.

**Chunk 2 (p4–p8) — Welcome + Introduction + Section 1:**

| Trang PDF | Web (1 hàng/trang) | Component |
| --------- | ------------------ | --------- |
| p4 trái | Welcome body + chữ ký | `.wp-display-title.wp-title-rule`, `.wp-signatures` |
| p4 phải | Pull quotes | `.wp-pull-panel` (nền `#faefdf`); `.wp-pull-quote` 22pt Baskerville `#dd971a`; `.wp-pull-quote__attrib` — **8pt Proxima Light**, `#7d8698`, **ALL CAPS** verbatim PDF, `font-style: normal` (không italic `<cite>`) |
| p5 trái | Ảnh + Introduction overlay + body | `.wp-photo-hero` + `.wp-section-opener--inset` + `.wp-title-rule` |
| p5 phải | Letter + byline UoA | `.wp-byline` — thứ tự PDF: **ảnh** (clip panel `#f1f1f2`, `p5-byline-photo.png` render từ PDF — **không** `extract_image` nền đen) → **chữ ký** → tên/chức danh; **không** crop/filter ảnh |
| p6 trái | Section opener full-bleed | `.wp-spread__page--visual` + `.wp-section-opener--overlay`, kicker `SECTION 1`, `.wp-title-rule__mark` trên “impact” |
| p6 phải | Body + bullets | `.wp-subhead` (20pt), `.wp-list` |
| p7 trái | Stat board | `.wp-stat-board` — HTML grid; `.wp-stat-board__midrule` spacing đo PDF; growth icon = **inline SVG** path PDF + `--wp-stat-growth-overlap-pt` / `--wp-stat-growth-lift` |
| p7 phải | Ảnh band + body | `.wp-photo-band` + `.wp-spread__inner--below-band` |
| p8 trái | Body + donut chart | `.wp-donut-panel` — SVG donut + legend HTML (màu/góc đo PDF); **cấm** composite PNG |
| p8 phải | Ảnh + case study | `.wp-spread__page--case-study` nền **`#faefe0`**; `.wp-photo-band--short`, `.wp-case-study`; ghi chú privacy → **`.wp-case-study__note`** (7pt / `--wp-note-size`, **Medium**) |

Assets: `website/assets/why-the-modern-family-office-matters/images/chunk-02/`.

**Chunk 3–6 (p9–p32) — map PDF → catalog class:**

| Trang PDF | Component |
| --------- | --------- |
| p9 trái | `.wp-section-opener--overlay` (Section 2) |
| p9 phải | Body + `.wp-model-grid` (MFO `--accent`) |
| p10 trái | `.wp-callout-stack` |
| p10 phải | `.wp-body` + `.wp-list` |
| p11–13 trái / p12 | `.wp-subhead` + `.wp-callout` (lặp) |
| p13 phải | `.wp-compare-table` |
| p14 trái | `.wp-section-opener--overlay` (Section 3) |
| p14 phải | `.wp-era-grid` |
| p15 | `.wp-spread--flow` body |
| p16 trái | `.wp-gemstone` |
| p16 phải | `.wp-photo-band` + facet 1 body |
| p17–18, p22–23 | `.wp-spread__page--case-study` |
| p19, p21, p24 | Facet heading + `.wp-list` / photo |
| p20 | `.wp-callout` + `.wp-outcome-list` |
| p25 | Conclusion `.wp-body` |
| p26–27 | `.wp-contributors` |
| p28–29 | `.wp-about` + `.wp-offices` |
| p30 | `.wp-endnotes` |
| p31 trái | `.wp-legal` — **bỏ** p31 phải đen trống |
| p32 | `.wp-back` |

**Trang chỉ có ảnh (full-bleed visual):**

- PDF spread mà một nửa **chỉ có ảnh full trang** (vd. TOC trái p3, section opener sau này) → `.wp-spread__page--visual` + `<figure class="wp-page-visual">`.
- **Desktop:** `width: 100%` (trong `--page-max`); ảnh `width: 100%; height: auto` — **tỷ lệ gốc** từ `width`/`height` attribute hoặc intrinsic; **không** `100vh`, **không** `object-fit: cover` kéo theo chiều cao viewport.
- **Mobile cover (p0):** vẫn `min-height: 100vh` — riêng `.wp-cover`, không áp cho `.wp-page-visual`.
- Overlay section opener: `.wp-section-opener--overlay` absolute trên `.wp-spread__page--visual`; chiều cao trang = chiều cao ảnh tự nhiên.
- Markup mẫu:

```html
<div class="wp-spread__page wp-spread__page--left wp-spread__page--visual">
  <figure class="wp-page-visual">
    <img src="…" alt="" width="1245" height="1759" />
  </figure>
</div>
```

### Nhóm C — Perspective / Insight Article

- Trang bìa: hero trong `--page-max` (đo **W×H band** — khoảng ~210–320pt H trên A4); web: **aspect-ratio W/H** trong shell → H ≈ PDF; **logo nhỏ góc trên-trái trên ảnh**; tiêu đề bài **dưới ảnh** (nền trắng). Logo trắng cần **scrim** theo B.4 khi PDF có (thường flat ~25% đen).
- **H1 màu không đồng nhất giữa 3 bài**: 2/3 dùng Ochre thương hiệu; 1 bài ("Protecting intergenerational wealth…") dùng xanh xám `#4E5E72` — **không có trong Style Guide Colour**; cần xác nhận với brand (chủ đích vs lệch export). Khi chưa chốt: mặc định Ochre/Black theo Style Guide.
- Không có bảng heat-color hay lưới 6 chart như nhóm A.
- Callout (nếu có) đa dạng theo bài — xem B.8.
- Kết bài: **khối chữ ký tác giả** (tên đậm, chức danh, "Mutual Trust") trước legal.
- Disclaimer ngắn hơn, trên nền trắng cuối trang nội dung — **không** back cover đen riêng.

## B.8 Thành phần riêng của từng PDF

| File                                | Thành phần độc quyền                                                                                    |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------- |
| June 2026 QMR, Oct 2025 MMR, April 2026 MMR | Bảng "Global Markets" heat-style + lưới 6 chart (B.6.2 / B.7.2); hero overlay B.7.1; April thêm note quarterly |
| March 2026 Quarterly Outlook        | Biểu đồ cột ngang "S&P 500 Index Sector Performance"                                                    |
| June 2026 Quarterly Outlook         | Pie chart "Indicative Mutual Trust asset allocation"; 4 câu hỏi mở đầu dạng numbered list               |
| Protecting Intergenerational Wealth | Box "Interested in learning more?" + thumbnail podcast + link; H1 xanh xám (biến thể ngoài Style Guide) |
| Perspective from Brendan Henderson  | Flow-chart 5 khối + mũi tên ("double death tax") — infographic phức tạp nhất, không lặp lại             |
| Strengthening Farm Safety           | Callout thuần trích dẫn (text + attribution, không ảnh/sơ đồ)                                           |

## B.9 List / Bullet — style đo trực tiếp từ PDF

Đã trích glyph-level (font, size, màu, vị trí x) của toàn bộ bullet/numbered list trong 7 PDF bằng PyMuPDF (không suy đoán). Kết quả nhất quán ở phần lõi, lệch ở phần vị trí:

| Thuộc tính                  | Giá trị đo được                                                         | Ghi chú                                                                                                                                                                                                                                                   |
| --------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ký tự bullet                | `•` (U+2022)                                                            | Luôn font **SymbolMT** — artefact Word export, không phải chủ đích thiết kế (đã ghi ở B.1). Trên web: **đừng** render `•` ở full body `font-size` (sẽ to hơn PDF). Dùng disc CSS nhỏ (~**5px** @ 96dpi khi body 12pt) — xem cỡ marker dưới                |
| Ký tự numbered              | số + `.` (`1.` `2.` `3.` …)                                             | Font **body** (Proxima Nova Light/Regular), **không** phải font riêng cho số                                                                                                                                                                              |
| Màu marker                  | luôn theo màu **ink thân bài** — `#000000`, vài chỗ `#1B1B1F`/`#1B1B20` | **Không bao giờ dùng Ochre** cho bullet/numbered marker trong 7/7 file. Lưu ý phân biệt với numbered **section heading** (đánh số phần lớn, Baskerville 16–22pt + Ochre `#D17B19`, xem B.7 nhóm B) — đây là 2 pattern khác nhau, không nhầm lẫn khi build |
| Cỡ marker (optical)         | Disc **~5px** web khi body 12pt→16px                                    | Crop PDF (SymbolMT 12pt) đo ~**4px**; token web dùng **+20%** → **5px** cho đọc rõ hơn trên màn hình mà vẫn nhỏ hơn nhiều so với glyph `•` browser 16px. QA so size + indent                                                                              |
| Khoảng cách marker → text   | **18pt cố định** (≈ 24px web)                                           | Từ **mép trái origin của marker** → **mép trái text** (tab-stop Word 0.25in). Không tỷ lệ theo font-size. Gap trống sau disc nhỏ chiếm phần lớn 18pt — nếu bullet web quá to sẽ “ăn” khoảng trống và trông sát chữ hơn PDF                                |
| Hanging indent              | Có                                                                      | Dòng wrap thứ 2+ của một item canh thẳng với vị trí **text** (sau tab-stop), không lùi về vị trí marker — xác nhận ở mọi list nhiều dòng đo được                                                                                                          |
| Line-height trong list item | ≈ **1.2× cỡ chữ**, giống thân bài                                       | Không có leading riêng cho list (xem B.2). Căn marker theo trục dọc dòng đầu (không trôi baseline)                                                                                                                                                        |

**Vị trí marker so với lề thân bài — không đồng nhất giữa file (3 kiểu quan sát được):**

| Kiểu                      | Cách đo                                                                  | File quan sát                                                |
| ------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------ |
| (a) Flush (phổ biến nhất) | Marker canh đúng lề thân bài; text lùi thêm 18pt                         | Oct 2025 MMR, March 2026 QO, June 2026 QO (3/5 file có list) |
| (b) Outdent               | Marker lùi ra **ngoài** lề thân bài 18pt; text canh đúng lề thân bài     | June 2026 QMR                                                |
| (c) Inset                 | Cả block list lùi vào thêm 18pt so với lề thân bài; marker + 18pt = text | Protecting Intergenerational Wealth                          |

**Khuyến nghị:** dùng **(a) Flush** làm base rule (đa số) — marker canh lề thân bài, text +18pt/24px. Khi convert 1 file cụ thể rơi vào (b)/(c), **override theo đo PDF của đúng file đó** — đúng nguyên tắc "PDF thắng" ở indent list (xem bảng ưu tiên đầu tài liệu, dòng 2).

**Spacing giữa 2 item trong list** không đo được nhất quán giữa file — có file chỉ cách đúng 1 line-height (không thêm khoảng), có file có thêm ~18pt. **Chưa chốt một số cố định** — cần so trực quan với ảnh chụp trang khi build từng file (xem C.5).

### Design tokens — List / Bullet

```
--list-marker-color: var(--color-ink);   /* #000000 — theo body ink, KHÔNG dùng --color-accent/Ochre */
--list-marker-gap:   24px;                /* = 18pt PDF, CỐ ĐỊNH — không theo em/cỡ chữ */
--list-indent:        24px;               /* padding text / hanging — = marker-gap */
--list-marker-size:   5px;                /* PDF crop ~4px +20% web readability */
```

```css
/* Base: kiểu (a) Flush — marker canh lề thân bài; text +24px; wrap canh text */
ul.mt-list,
ol.mt-list {
  list-style: none;
  padding-left: 0;
  margin: 0;
}
ul.mt-list > li,
ol.mt-list > li {
  position: relative;
  padding-left: var(--list-indent);
  text-indent: 0; /* absolute marker — không dùng text-indent âm (dễ lệch size/position) */
  line-height: var(--text-body-line-height, 1.5);
}
/* Disc nhỏ khớp PDF — KHÔNG dùng • full-size (sẽ to và “ăn” gap marker→text) */
ul.mt-list > li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0.55em;
  width: var(--list-marker-size);
  height: var(--list-marker-size);
  border-radius: 50%;
  background-color: var(--list-marker-color);
}
ol.mt-list {
  counter-reset: mt-counter;
}
ol.mt-list > li::before {
  counter-increment: mt-counter;
  content: counter(mt-counter) '.';
  position: absolute;
  left: 0;
  width: var(--list-indent);
  color: var(--list-marker-color);
  font-size: inherit;
  line-height: inherit;
  background: none;
  border-radius: 0;
}
/* Biến thể (b) Outdent — dùng khi PDF nguồn khớp kiểu June 2026 QMR */
.mt-list--outdent {
  margin-left: calc(-1 * var(--list-indent));
}
/* Biến thể (c) Inset — dùng khi PDF nguồn khớp kiểu Protecting Intergenerational */
.mt-list--inset {
  padding-left: var(--list-indent);
}
/* Quan trọng: reset `ul` trong body không được ghi đè --inset / --outdent (specificity) */
.perspective-body ul.mt-list--inset {
  padding-left: var(--list-indent);
}
```

---

# C. Base Framework đề xuất

_Chưa build. Tokens visual = Style Guide; layout/component variants = PDF patterns._

## C.1 Spacing

Style Guide Desktop Typography frame dùng nhịp lớn (padding section ~64px, gap swatch/type block ~24–48px) — dùng làm **baseline spacing web**:

```
--space-1: 4px
--space-2: 8px
--space-3: 16px
--space-4: 24px
--space-5: 32px
--space-6: 48px
--space-7: 64px
```

Khi convert PDF cụ thể: **override** khoảng hero↔content, content↔footer, paragraph gap, list indent theo clearspace đo từ PDF (xem B.3 / B.7) để fidelity cao hơn.

## C.2 Grid (từ PDF patterns)

- **Page shell** `--page-max`: = **chiều rộng trang PDF** @ 96dpi (A4 ≈ **794px** từ 595.32pt). Hero + article nằm trong shell này — không full-bleed viewport.
- **Content column** `--container-max`: đo lề nội dung PDF (thường ~**646–760px** trên A4 với lề ~55pt) — hẹp hơn `--page-max`; logo/title/body/footer canh cùng mép cột.
- Một continuous page trong shell; không giả lập nhiều artboard trang.
- Quyết định còn mở: hợp nhất lề A/C (~55pt) vs B (~72pt) thành 1 content width, hay giữ 2 biến thể theo family

## C.3 Thư viện component (từ recurring PDF patterns + Style Guide styling)

Layout/panel mới trên PDF **phải** vào template family trước khi build bài — xem **Layout mới → component trong template**.

1. **Hero/Header** — 3 biến thể: (a) title overlay trên ảnh — Market Review (`template-market-review.html`); (b) logo stacked **căn giữa** + kicker "Quarterly Outlook" trên ảnh, **H1 dưới ảnh** — Outlook (`template-quarterly-outlook.html`); (c) logo ngang góc trên-trái + title dưới ảnh — Perspective (`template-perspective.html`). Logo: URL A.5. Hero trong `--page-max`; `aspect-ratio` = W/H dải PDF (B.4); scrim (C.6.3).
2. **Section heading** — Baskerville; có/không đánh số; accent Ochre hoặc Black theo ngữ cảnh PDF.
3. **Callout/quote box** — nền Light Grey; nội dung: quote + attribution, podcast thumb + link, hoặc infographic.
4. **Heat data table (nhóm A)** — B.6.2–B.6.3: `.mr-table` + `.is-positive` / `.is-negative` (và neutral theo PDF); section Equities/Bonds/Currency; wrap `overflow-x: auto` trên mobile; **không** card-stack trên desktop.
5. **Chart grid (nhóm A)** — B.7.2: `.mr-chart-grid` **2×3 desktop → 1 cột mobile**; **một ảnh mỗi panel** (cấm composite 6-in-1); source trong ảnh hoặc caption — không duplicate.
5b. **Infographic / panel (nhóm D)** — catalog: `.wp-stat-board`, `.wp-donut-panel`, `.wp-gemstone`, `.wp-model-grid`, `.wp-compare-table`, `.wp-era-grid`, `.wp-callout` (khác `.wp-pull-quote`). HTML + SVG; **cấm** composite PNG. Markup: `template-white-paper.html` comment **TYPE D COMPONENT CATALOG**.
6. **Author sign-off** — tên, chức danh, "Mutual Trust" (nhóm C).
7. **Document meta / byline** — author/date khi PDF có (nhóm B); đặt một lần trong article, **không** lặp running footer + số trang.
8. **Legal + contacts footer** — một khối cuối document theo **B.5** (markup `.perspective-legal` / `.perspective-contacts` làm nền; calibrate copy + spacing từ PDF). Variant nền: trắng (C) / dải hoặc back-cover tối (A, B).
9. **Office contact grid** — nằm trong B.5.2; 4 cột điển hình (HQ + 2 stack city + meta); AI override theo PDF.
10. **List (bullet & numbered)** — marker màu ink (`--color-ink`, không Ochre); disc optical ~**5px** (PDF ~4px +20%; không `•` full-size); gap marker→text cố định 24px; wrap canh text; numbered dùng số body font + dấu `.`; base = Flush, biến thể Outdent/Inset theo PDF — chi tiết B.9.
11. **Inline link** — đối chiếu PDF: **colour**, **italic/roman**, **bold/regular**, **có/không underline**. Màu thường `#D17B19` hoặc Ochre `#CB962E` (nếu lệch rõ → HEX PDF). **Underline chỉ khi PDF nhìn thấy rõ**; không mặc định `is-underlined`. Nhiều Perspective / Outlook June chỉ tô màu (+ italic), không gạch chân nhìn thấy (C.6.7).

## C.4 Checklist convert PDF → HTML

_Tham chiếu đầy đủ quy trình visual: **C.6**._

1. Đọc toàn bộ PDF nguồn — inspect theo C.6.2 trước khi viết HTML/CSS.
2. Gán font family + map màu brand sang token Style Guide (mục A); load font từ `assets/fonts` và xác minh browser đang dùng đúng font (C.6.3–C.6.4).
3. Chọn document family (A / B / C) và hero/footer variant (mục B.7).
4. Chọn logo URL đúng biến thể PDF (`logo-m.svg` ngang vs `MT-Logo.svg` stacked — mục A.5); xử lý trắng/tối theo nền.
5. **Page shell** — `--page-max` = chiều rộng trang PDF @ 96dpi; không để layout tràn full browser (B.4, C.2).
6. **Hero geometry** — trong shell: `aspect-ratio: W / H` dải PDF → chiều cao hero = H PDF quy đổi; xác nhận crop/position không cắt chủ thể (B.4, C.6.5).
7. **Hero overlay/scrim** — đo từ PDF (opacity / gradient); áp lên HTML trước khi chốt contrast logo/chữ trên ảnh (B.4, C.6.3). Không tắt scrim chỉ vì “ảnh đã đẹp”.
8. **Calibrate geometry rồi typography** theo C.6.4–C.6.5 (content width, size, line-height, spacing, placement từ PDF).
9. Giữ toàn bộ copy PDF — không omit / invent / duplicate.
10. Semantic / one-off colours và link treatment theo PDF khi có (C.6.7).
11. List/bullet theo B.9 + C.6.6 — không dùng browser default.
12. **Nhóm A — heat table + chart grid:** build theo B.6.2 / B.7.2 (`template-market-review.html`); desktop đủ cột + lưới 2×3; mobile table scroll-x + chart stack (B.6.3 / C.6.10). Hero overlay placement: B.7.1.
12b. **Nhóm B — Quarterly Outlook:** copy `template-quarterly-outlook.html`; hero stacked logo = **½ width kicker**; H1 dưới ảnh; body 10pt; lede Proxima Ochre cùng cỡ body (selector thắng `.qo-body h2`); text|chart **đo bbox** (`.qo-split` / `.qo-float`, không cap 320px); `.qo-quote` roman; `.qo-footer` back cover (B.7 B).
12c. **Nhóm D — White Paper:** copy `template-white-paper.html`; chọn class từ **Component catalog**. Layout chưa có class → **thêm component vào template + hàng lookup MD trước**, rồi mới build bài (mục *Layout mới → component*). Typography `--text-*`; `.wp-spread--flow`; infographic HTML+SVG; cover footer căn trái; monogram `background-image` `#000c1d`. Quote trong body = `.wp-callout`, không `.wp-pull-quote`.
13. **Footer/legal** — bắt đầu từ cấu trúc chuẩn **B.5**; đo PDF rồi override (B.5.4). Không số trang / running footer.
14. **Không tái tạo pagination của PDF trên web.** Nội dung chuyển thành continuous document flow. Page boundary của PDF chỉ dùng làm checkpoint trong visual QA để phát hiện cumulative spacing/typography drift (C.6.8–C.6.9).
15. Chạy Visual Comparison Loop (C.6.8) — tối đa 3 vòng correction nếu còn khác biệt đáng kể; **desktop fidelity đạt trước** rồi mới responsive (C.6.10).
16. Chỉ đánh dấu hoàn thành khi đạt Definition of Done (C.6.11).
17. **Chưa deploy** cho đến khi được yêu cầu.

## C.5 Việc còn cần xác nhận

- License font Proxima Nova + Baskerville khi build web công khai.
- H1 xanh xám `#4E5E72` ở "Protecting Intergenerational Wealth": chủ đích hay lệch? Style Guide Colour **không** có mã này — mặc định map Ochre/Black cho đến khi brand xác nhận.
- Hợp nhất 2 chuẩn lề (A/C vs B) hay giữ 2 biến thể theo family (chỉ ảnh hưởng content width web, không giữ A4).
- Heat-table (nhóm A) và flow-chart (Brendan Henderson): component tái sử dụng hay case-by-case.
- Có thêm Mobile Typography trong Style Guide Figma hay không — hiện tài liệu lấy **Desktop Typography** (`2:611`) làm baseline; mobile scale sẽ bổ sung khi có node chính thức.
- List/bullet: vị trí marker (Flush/Outdent/Inset, xem B.9) khác nhau giữa file — cần chọn theo đúng PDF nguồn khi build. Spacing giữa 2 item chưa đo cố định — so trực quan khi build (QA checkpoint, không tái tạo page break).

## C.6 Quy trình Visual Fidelity — PDF → HTML

### C.6.1 Nguyên tắc

Bản PDF nguồn là **visual reference chính**.

Không được coi HTML hoàn thành chỉ vì:

- nội dung đúng
- component đúng
- font family đúng
- template render thành công

HTML chỉ được coi là đạt khi đã trải qua **visual comparison** với PDF.

### C.6.2 Inspect trước khi build

Trước khi viết HTML/CSS phải xác định:

- asset thật được sử dụng
- logo variant, size, placement
- page width → `--page-max` (shell = khổ PDF, không full viewport)
- hero dimensions; **W×H band → aspect-ratio trong shell** (H web ≈ H PDF @ 96dpi); image crop / object-position
- hero overlay / scrim (có/không, flat opacity hay gradient, độ tối) — contrast logo/chữ trên ảnh
- hero image **transform** (có mirror ngang không) + vị trí subject (trái/phải) so với render PDF
- content width, alignment
- font family, weight, style, size, line-height, letter-spacing
- **italic/oblique thật trên render** (kể cả khi tên font Regular)
- heading hierarchy; paragraph / byline / h2 spacing (đo pt)
- màu sắc; link treatment (size + underline, đặc biệt email/www footer)
- bullet/list geometry
- callout / promo styling
- author/sign-off; legal/contact theo **B.5** (grid, clearspace contacts→legal, meta không underline lệch size)
- **Nhóm A — heat table:** số cột, section labels + gạch Ochre, fill dương/âm (sample drawing), source line, độ rộng bảng vs content column (B.6.2)
- **Nhóm A — hero overlay:** `content_x`, `title_y`, page W (B.7.1)
- **Nhóm A — chart grid:** bbox 6 panel, thứ tự đọc, có/không source trong ảnh; chuẩn bị clip riêng từng panel (B.7.2)
- **Nhóm B — Outlook:** hero logo = ½ kicker; H1 dưới ảnh; lede size/family; **màu heading đo PDF** (June `#D17B19`, không ép `#CB962E` nếu lệch rõ); text|chart bbox %; para-gap dày; back-cover padding A4 quanh logo+tagline (B.7 B)
- **Nhóm D — White Paper:** spread 1 hàng/trang; **gặp panel chưa có class → thêm vào template + bảng catalog trước khi build bài**; catalog (callout ≠ pull-quote; model-grid / compare-table / gemstone / era-grid); `--wp-content-x-pt`; `.wp-spread--flow`; cover footer căn trái; monogram `#000c1d`

Không bắt đầu từ browser default hoặc generic web styling.

### C.6.3 Asset fidelity

Ưu tiên asset thật.

- Không dựng logo bằng text.
- Không crop logo từ screenshot nếu đã có SVG chính thức (A.5).
- Không thay ảnh khi có thể extract/reuse ảnh gốc.
- Không dùng fallback font nếu font Mutual Trust tương ứng đã có trong `website/assets/fonts`.
- **Page shell + hero aspect-ratio:** `--page-max` = page W PDF @ 96dpi (A4 ≈ 794px). Hero full-bleed **trong shell**, `aspect-ratio: W / H` (vd. `595.32 / 224.2`) → H ≈ 299px đúng PDF — **không** full-bleed viewport (tránh hero quá cao / crop sai).
- **Hero overlay / contrast:** so PDF vs ảnh extract. Nếu PDF có lớp tối (flat opacity hoặc gradient) trên hero — **bắt buộc** áp CSS scrim tương đương (`::after` / `--*-hero-scrim`). Mục tiêu: logo trắng / chữ trên ảnh đạt contrast như PDF. Ví dụ đo được: fill `#000000` @ **~25% opacity** phủ full hero (_Protecting Intergenerational Wealth_). Không tắt overlay khi logo HTML sáng hơn / kém đọc hơn bản PDF.

Sau khi load font phải xác minh browser thực sự đang sử dụng font đó.

### C.6.4 Typography calibration

Typography phải được calibrate **trước** spacing.

Thứ tự kiểm tra khi line wrapping khác PDF:

1. font-family
2. font file thực tế đã load hay chưa
3. font-weight / font-style
4. content width
5. font-size
6. letter-spacing
7. line-height (đo **line advance** pt→px — không nới lh web nếu PDF đặc hơn)

**Paragraph / byline / heading rhythm:** đo ink-to-ink (y1 dòng cuối → y0 khối sau). Override margin mặc định của template (`--space-5`, `28px` trên h2…) khi lệch PDF.

**Italic / oblique — không tin mỗi font name:**

- Một số PDF (vd. _Double Death Tax Trap_) đặt cả đoạn “What if…” nghiêng nhưng span vẫn tên `ProximaNova-Regular` (không `Italic` trong tên / flag).
- Bắt buộc đối chiếu **render PDF** + dấu hiệu kỹ thuật (glyph bbox lệch origin, crop vùng chữ).
- Khi PDF nghiêng: `<em>` / class `is-italic` + `font-style: italic` (dùng face RegularIt nếu có). **Không** bỏ italic chỉ vì extractor báo Regular; **không** italic hoá đoạn roman.

Không dùng margin/padding để chữa lỗi line-wrap do font hoặc content width sai.

Mục tiêu: paragraph wrapping và mật độ chữ gần PDF nguồn.

### C.6.5 Geometry calibration

Hiệu chỉnh theo thứ tự:

1. **page shell** `--page-max` (= PDF page width)
2. content column `--container-max`
3. horizontal alignment (logo/body cùng cột trong shell)
4. hero **aspect-ratio** trong shell (W/H dải PDF) → H khớp PDF
5. hero **orientation** (mirror/flip nếu PDF transform scaleX âm — B.4) rồi mới crop / `background-position`
6. logo size/placement
7. typography
8. paragraph rhythm (lh + para/byline/h2 gaps đo từ PDF)
9. section spacing
10. component-specific spacing (contacts meta size/underline, legal clearspace — B.5)

Không tinh chỉnh margin nhỏ khi geometry tổng thể vẫn sai.

### C.6.6 List/Bullet fidelity

Không dùng browser default `<ul>` / `<ol>` styling.

Phải đối chiếu: marker **type**, **optical size**, **position** (x so với lề thân bài), gap marker→text, hanging indent / wrapped-line alignment, item spacing, khoảng trước/sau list.

Dùng pattern Flush / Outdent / Inset đã phân tích tại B.9.

**Lỗi thường gặp (đã quan sát khi convert Perspective):**

- Glyph `•` ở body size → marker **to hơn** token web (~5px) và trông sát chữ hơn vì “ăn” khoảng 18pt.
- `text-indent` + `::before { width: 24px }` với `•` lớn → lệch vị trí cảm nhận dù số đo indent đúng.
- Reset `.perspective-body ul { padding-left: 0 }` ghi đè `.mt-list--inset` nếu specificity thấp hơn.

Khuyến nghị: disc CSS `--list-marker-size` + `position: absolute; left: 0` trên `li`; verify inset bằng đo `marker x` / `text x` so với content column.

### C.6.7 Link và màu

Không tự động áp style link web generic (đặc biệt **không** mặc định underline mọi link).

Link phải đối chiếu PDF về: **colour**, **italic/roman**, **font-weight**, **có/không underline**, **font-size**. Ví dụ _Protecting Intergenerational Wealth_ (và nhiều Perspective): link `#D17B19` / ochre-tinted, **không gạch chân**. **Outlook June 2026:** `#D17B19` + **italic** (`<em>`), không `is-underlined` — HTML 1px underline lệch PDF. Hover có thể thêm underline nhẹ — chỉ là enhancement web, không đổi base style lệch PDF.

**Đích link (`href`) — bắt buộc, không chỉ màu/gạch chân:**

- Mọi vùng link trong PDF (annotation / URI) phải map 1:1 sang `<a href="URI">`.
- Trích URI từ PDF **trước** khi styling; không suy ra từ màu chữ.
- **Cấm** `href="#"` trong HTML deliverable. Placeholder template (`<!-- OUTLOOK_URL -->`, `<!-- WEBSITE_URL -->`, …) phải được thay bằng URI thật trước khi giao.
- CTA Market Review “click here” (B.4 / `.mr-cta`): URI thường trỏ tới PDF hoặc trang Insights của bản Quarterly Outlook mới nhất — **lấy từ annotation PDF**, không hard-code `#`.
- Footer: `tel:`, `mailto:`, `https://www.mutualtrust.com.au/` theo URI PDF hoặc chuẩn B.5 (đã có trong template).
- QA: side-by-side PDF vs HTML — click từng link; không link chết / placeholder.

**Ngoại lệ nhóm A — CTA `click here` (April MMR và PDF tương tự):**

- Base: `text-decoration: underline` + `text-decoration-color` = màu link (`#D17B19`) — **không** chỉ underline khi `:hover`.
- `text-decoration-thickness: 1px`; `text-underline-offset: 2px` — khe nhỏ dưới baseline như PDF (gạch **không** chen vào chữ; tránh `offset: 0`).
- `text-decoration-skip-ink: none` khi PDF vẽ hairline liền dưới cả cụm từ.

**Contacts meta (email / www) trong footer B.5:**

- Cùng **font-size / line-height** với dòng địa chỉ / SĐT (Market Review ~6pt) — không để link “phình” hơn cột văn phòng; Proxima Regular, không bold.
- Underline **theo PDF**: nhiều Perspective **không** gạch chân; **Market Review dark footer** thường **có** hairline trắng dưới email/www (B.5.6).
- `tel:` trong cột văn phòng: thường không underline.
- Tránh rule `.perspective-legal a { text-decoration: underline }` làm **rò** xuống mọi `.perspective-contacts a`. Style riêng `.perspective-contacts__meta a` khi PDF gạch chân.

Brand colour map theo Style Guide; nếu PDF có intentional PDF-specific treatment đã xác định thì **PDF thắng** theo bảng ưu tiên đầu tài liệu.

### C.6.8 Visual Comparison Loop

Sau khi build HTML:

1. Render HTML ở desktop viewport chuẩn.
2. Render/chụp PDF thành visual reference.
3. So sánh PDF và HTML side-by-side.
4. Kiểm tra toàn bộ document từ trên xuống dưới.
5. Liệt kê visual differences.
6. Sửa CSS/HTML.
7. Render lại.
8. Compare lại.

Không kết thúc sau lần generate đầu tiên. Thực hiện tối đa **3 vòng correction** nếu vẫn còn khác biệt đáng kể.

Mỗi vòng ưu tiên sửa theo thứ tự: assets/logo → geometry/content width → fonts → typography → line wrapping → spacing → lists → colours/links → component details.

### C.6.9 Cumulative drift

Page boundary của PDF dùng như **QA checkpoint**, **không** phải web page break.

Ví dụ: nếu tại vị trí tương đương cuối PDF page 1, HTML đã dài/ngắn hơn đáng kể thì kiểm tra font load, font-size, line-height, content width, paragraph/heading margin, list spacing.

Không thêm blank space hoặc page break để ép content “đúng trang”. Mục tiêu là tìm nguyên nhân gây drift.

### C.6.10 Responsive

Chỉ bắt đầu responsive adaptation sau khi **desktop fidelity** đã đạt mức chấp nhận được.

**Desktop:** PDF fidelity ưu tiên cao nhất — hero `aspect-ratio` = W/H dải PDF trong `--page-max` (B.4); nhóm A title/date placement B.7.1. **Nhóm A:** bảng heat đủ cột + lưới chart **2×3** giống trang PDF (B.6.2 / B.7.2).

**Tablet/mobile — giữ:** visual identity, typography hierarchy, assets, colours, content order, component meaning, hướng subject hero, scrim, **ý nghĩa heat colour** (dương/âm), **thứ tự 6 chart**.

**Cho phép:** stack columns, giảm font-size hợp lý, đổi padding, **nới tỉ lệ / min-height hero** (B.4 mobile), scale logo/kicker, tinh chỉnh `background-position`, **table `overflow-x: auto`**, **chart grid → 1 cột**.

**Hero mobile QA (bắt buộc trước khi Done):**

1. Logo + mọi chữ overlay **nằm trọn** trong hero — không cắt, không tràn đáy/mép.
2. Chủ thể ảnh (hoa, người, horizon…) vẫn nhận ra; không crop mất cụm chính vì band quá dẹt.
3. Chữ không đè nặng lên vùng sáng/chi tiết tới mức mất đọc (điều chỉnh size/position/scrim tối thiểu).
4. Không horizontal scroll **cả trang**; hero vẫn trong page shell (không bắt buộc full browser width).

**Nhóm A — table + chart mobile QA (bắt buộc):**

1. **Table:** vẫn là bảng so sánh đa cột + **lưới đen**; vuốt ngang trong `.mr-table-wrap` xem hết CYTD…5Y; `document.scrollWidth` không vượt viewport vì bảng.
2. **Heat:** ô dương/âm vẫn teal/maroon phủ **cả ô** (không pill/gutter trắng giữa ô) + chữ trắng; không mất màu khi thu nhỏ.
3. **Charts:** 6 panel **stack** full-width, đúng thứ tự PDF; mỗi ảnh đọc được title/trục/legend — **không** một composite nhỏ.
4. Section Equities/Bonds/Currency và dòng Source dưới bảng vẫn có mặt.

**Nhóm D — infographic mobile QA (bắt buộc):**

1. **Donut panel:** `.wp-donut-panel__grid` stack 1 cột; chart full content-width, segment labels vẫn đọc được.
2. **Stat board:** `.wp-stat-grid--3` → 1 cột nếu template quy định; số + icon growth không overlap sai / không clip.
3. **Flow continuation:** spread `.wp-spread--flow` liền kề không dùng gap 48px giữa body cùng section.

Không cố giữ kích thước vật lý A4 / đúng H PDF tuyệt đối trên mobile nếu làm hỏng hero QA (1)–(3) hoặc table/chart QA trên.

### C.6.11 Definition of Done

Một conversion chỉ hoàn thành khi:

- đúng toàn bộ nội dung; đúng assets; logo đúng variant và placement
- **Desktop:** `--page-max` = khổ PDF; hero trong shell, **aspect-ratio W/H** → chiều cao khớp PDF; crop/position/orientation không cắt chủ thể; overlay/scrim khớp PDF khi cần; logo/chữ đủ contrast
- **Nhóm A desktop:** heat table khớp cấu trúc/section/heat colours PDF; chart grid **2×3** với **6 asset tách**; so side-by-side với trang table + trang chart
- **Mobile/tablet:** hero tỉ lệ hợp lý (B.4 / C.6.10) — không cắt ảnh mất subject, không mất/đè chữ overlay; logo + kicker đọc được
- **Nhóm A mobile:** table scroll-x cục bộ; chart stack đọc được (C.6.10)
- **Nhóm D:** stat/donut HTML+SVG (không composite PNG); donut stack mobile; `.wp-spread--flow` gap đúng `--wp-intra-block-gap`
- font thực sự load đúng; typography / content width / spacing rhythm gần PDF (desktop)
- line wrapping không lệch lớn; bullet/list đúng geometry
- links: đúng màu/gạch chân **và** đúng `href` (không `#`, không placeholder); component đặc thù đúng
- không còn visual difference lớn khi compare side-by-side (desktop)
- desktop fidelity đạt trước responsive; mobile/tablet QA hero + content pass
- **không** tái tạo pagination không cần thiết của PDF
