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

### Nguyên tắc ưu tiên khi convert PDF → HTML

**Mục tiêu hàng đầu: like-for-like thị giác với PDF nguồn trên desktop**, trong một trang web liên tục. Style Guide không được làm trang “đúng brand token nhưng lệch bản PDF”. Chi tiết quy trình so sánh: **C.6**.

| Ưu tiên      | Cái gì                                                                       | Ai thắng khi xung đột                                                                  |
| ------------ | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| 1 (cao nhất) | Nội dung, bố cục, placement, hierarchy, imagery, spacing giữa các khối       | **PDF**                                                                                |
| 2            | Cỡ chữ, line-height, độ đậm/nghiêng, indent list, khoảng hero↔content↔footer | **PDF** (đo từ nguồn; Style Guide chỉ là điểm xuất phát)                               |
| 3            | Font _family_ và mã màu brand (Black / White / Light Grey / Grey / Ochre)    | **Style Guide** — map lệch export PDF về HEX/font chuẩn, **miễn là nhìn vẫn khớp PDF** |
| 4            | Semantic / one-off trong PDF (bảng dương–âm, H1 lệch màu một bài…)           | **PDF** — giữ và ghi chú PDF-specific                                                  |

**Quy tắc vận hành**

1. Style Guide cung cấp **tên token đúng** (Baskerville, Proxima Nova, Ochre `#CB962E`…) — tránh invent font/màu sai.
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

**Không** extract/crop logo từ PDF khi convert HTML trừ khi URL dưới không khớp biến thể trên PDF. Mọi template (`template.html`, `template-perspective.html`, `template-market-review.html`, `template-quarterly-outlook.html`) dùng một trong hai URL sau — **chọn theo loại logo mà PDF gốc đang dùng**:

| File              | URL                                                                                       | Hình dạng                                                                    | Dùng khi PDF có…                                                                                   |
| ----------------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **`logo-m.svg`**  | `https://www.mutualtrust.com.au/wp-content/themes/mutual_trust/assets/images/logo-m.svg`  | Ngang: icon mái vòm **bên trái** + wordmark `MUTUAL TRUST` (viewBox ~238×27) | Logo ngang trên hero (góc trên-trái — nhóm C Perspective); footer/legal khi PDF dùng bản ngang     |
| **`MT-Logo.svg`** | `https://www.mutualtrust.com.au/wp-content/themes/mutual_trust/assets/images/MT-Logo.svg` | Xếp chồng: icon **phía trên**, wordmark phía dưới (viewBox ~194×51)          | Logo căn giữa trên hero / back cover (nhóm B Quarterly Outlook), hoặc mọi chỗ PDF dùng bản stacked |

**Gợi ý map theo family (vẫn phải đối chiếu PDF từng file):**

| Family                    | Hero / cover                                  | Web HTML (không lặp theo trang)                                                              |
| ------------------------- | --------------------------------------------- | -------------------------------------------------------------------------------------------- |
| A — Market Review         | Thường **không** logo trên hero               | Footer/legal một lần: `logo-m.svg` nếu PDF có logo ở vùng đó                                 |
| B — Quarterly Outlook     | Hero căn giữa → **`MT-Logo.svg`** (stacked)   | Back-cover/legal cuối: **`MT-Logo.svg`** khi PDF có; **không** lặp running header từng trang |
| C — Perspective / Insight | Hero góc trên-trái → **`logo-m.svg`** (ngang) | Logo hero một lần; **không** lặp logo đầu mỗi “trang” PDF chỉ để đánh dấu pagination         |

**Styling**

- Cả hai SVG mặc định **fill trắng** — đặt trực tiếp trên ảnh hero / nền tối.
- Trên nền trắng / Light Grey: đảo sang mực tối (CSS `filter`, `currentColor` + chỉnh SVG, hoặc lớp tương đương) để khớp logo đen/xám trên PDF — **không** để logo trắng trên nền trắng.
- Giữ tỷ lệ gốc; width theo đo PDF (không méo). Placement (top-left / center / hidden) theo PDF, không theo thói quen web.

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
| **B — Outlook** | Back cover tối: logo stacked / tagline *"Helping families achieve what matters most."* + disclaimer dài; byline PDF đưa vào article, không chạy footer |

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

PDF export từng lệch nhẹ quanh Ochre (`#D17B19`, `#D17A18`, `#CBA020`, `#C99329`…) và vài tông xám/đen phụ (`#1B1B1F`, `#8D8D90`, `#E0E4EB`…). **Khi chuẩn hoá: map về 5 mã Style Guide** (mục A.3).

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

- Trang bìa: logo stacked **`MT-Logo.svg` căn giữa** trên hero, đường kẻ ngang (`.qo-hero__rule`), kicker serif **"Quarterly Outlook"** (trắng, ~39pt). **Tiêu đề bài viết cụ thể** nằm **dưới ảnh** trên nền trắng (`.qo-article__title`, Baskerville ink — không overlay như nhóm A).
- Byline PDF *"Written by [Tên] | [ngày]"* → `.qo-byline` **một lần** trong article; **không** lặp running footer / số trang.
- **Hai kiểu section head** (đừng nhầm với numbered list B.9):
  - **June:** `.qo-section` Baskerville ~16pt + Ochre `#D17B19` — `<span class="qo-section__num">1.</span>` + heading.
  - **March:** `.qo-section.qo-section--lede` Proxima Light, cỡ thân bài, màu `#CBA020` (không đánh số serif lớn).
- **Callout/pull-quote** (`.qo-quote`): nền đo từ PDF (March ≈ `#EEEEEE`; đôi khi `#E0E4EB`). Quote **Baskerville roman** trừ khi PDF italic; attribution sans, thường **căn phải** (vd. `BLACKROCK, MARCH 2026`). Không invent italic.
- **2 cột** (`.qo-split`): text trái / chart phải trên desktop; mobile stack (mặc định text→ảnh; `.qo-split--media-first` nếu cần ảnh trước). **Một ảnh mỗi chart** — không composite.
- Lề nội dung nhóm B ~**72pt** (`--qo-content-x-pt`) — hẹp hơn A/C; desktop pad `%` từ page W; **mobile ≤768: `--gutter: 20px`** như Perspective.
- **Back cover** `.qo-footer`: nền `#1B1B20` (đo fill PDF); logo stacked + tagline *"Helping families achieve what matters most."* + contacts (March: 4 văn phòng địa chỉ đủ dòng + meta; June có thể stack 2 city/cột) + disclaimer dài 3 đoạn (B.5.1).

| Token | Đo từ PDF | Ghi chú |
| --- | --- | --- |
| `--qo-page-w-pt` / `--page-max` | page W | A4 ≈ 594.96pt → ~793px |
| `--qo-content-x-pt` | x0 body (~72) | không 5vw; không pad A/C ~55pt |
| `--qo-hero-aspect` | page W / hero H | March ≈ `594.96 / 224.6` |
| `--qo-kicker-size` | "Quarterly Outlook" trên ảnh | ~39pt |
| `--qo-title-size` | H1 dưới ảnh | March 20pt; June ~28pt |

**QA desktop:** kicker căn giữa trên ảnh; H1 + body cùng mép trái; section numbered ≠ bullet numbered; quote upright nếu PDF roman; bảng/chart không scroll ngang trừ khi hẹp hơn `--page-max`.

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

1. **Hero/Header** — 3 biến thể: (a) title overlay trên ảnh — Market Review (`template-market-review.html`); (b) logo stacked **căn giữa** + kicker "Quarterly Outlook" trên ảnh, **H1 dưới ảnh** — Outlook (`template-quarterly-outlook.html`); (c) logo ngang góc trên-trái + title dưới ảnh — Perspective (`template-perspective.html`). Logo: URL A.5. Hero trong `--page-max`; `aspect-ratio` = W/H dải PDF (B.4); scrim (C.6.3).
2. **Section heading** — Baskerville; có/không đánh số; accent Ochre hoặc Black theo ngữ cảnh PDF.
3. **Callout/quote box** — nền Light Grey; nội dung: quote + attribution, podcast thumb + link, hoặc infographic.
4. **Heat data table (nhóm A)** — B.6.2–B.6.3: `.mr-table` + `.is-positive` / `.is-negative` (và neutral theo PDF); section Equities/Bonds/Currency; wrap `overflow-x: auto` trên mobile; **không** card-stack trên desktop.
5. **Chart grid (nhóm A)** — B.7.2: `.mr-chart-grid` **2×3 desktop → 1 cột mobile**; **một ảnh mỗi panel** (cấm composite 6-in-1); source trong ảnh hoặc caption — không duplicate.
6. **Author sign-off** — tên, chức danh, "Mutual Trust" (nhóm C).
7. **Document meta / byline** — author/date khi PDF có (nhóm B); đặt một lần trong article, **không** lặp running footer + số trang.
8. **Legal + contacts footer** — một khối cuối document theo **B.5** (markup `.perspective-legal` / `.perspective-contacts` làm nền; calibrate copy + spacing từ PDF). Variant nền: trắng (C) / dải hoặc back-cover tối (A, B).
9. **Office contact grid** — nằm trong B.5.2; 4 cột điển hình (HQ + 2 stack city + meta); AI override theo PDF.
10. **List (bullet & numbered)** — marker màu ink (`--color-ink`, không Ochre); disc optical ~**5px** (PDF ~4px +20%; không `•` full-size); gap marker→text cố định 24px; wrap canh text; numbered dùng số body font + dấu `.`; base = Flush, biến thể Outdent/Inset theo PDF — chi tiết B.9.
11. **Inline link** — màu theo PDF (thường Ochre / `#D17B19`); **underline chỉ khi PDF có**; nhiều Perspective chỉ tô màu, không gạch chân (C.6.7).

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
12b. **Nhóm B — Quarterly Outlook:** copy `template-quarterly-outlook.html`; hero stacked logo + kicker; H1 dưới ảnh; section numbered Ochre **hoặc** lede Proxima; `.qo-split` cho chart; `.qo-quote` roman; `.qo-footer` back cover (B.7 B).
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
- **Nhóm B — Outlook:** hero logo stacked + kicker vs H1 dưới ảnh; section numbered Ochre vs lede Proxima; split chart bbox; quote fill + slant; back-cover contacts/tagline (B.7 B)

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

Link phải đối chiếu PDF về: **colour**, **có/không underline**, **font-size**, font weight. Ví dụ _Protecting Intergenerational Wealth_ (và nhiều Perspective): link `#D17B19` / ochre-tinted, **không gạch chân**. Hover có thể thêm underline nhẹ — chỉ là enhancement web, không đổi base style lệch PDF.

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

Không cố giữ kích thước vật lý A4 / đúng H PDF tuyệt đối trên mobile nếu làm hỏng hero QA (1)–(3) hoặc table/chart QA trên.

### C.6.11 Definition of Done

Một conversion chỉ hoàn thành khi:

- đúng toàn bộ nội dung; đúng assets; logo đúng variant và placement
- **Desktop:** `--page-max` = khổ PDF; hero trong shell, **aspect-ratio W/H** → chiều cao khớp PDF; crop/position/orientation không cắt chủ thể; overlay/scrim khớp PDF khi cần; logo/chữ đủ contrast
- **Nhóm A desktop:** heat table khớp cấu trúc/section/heat colours PDF; chart grid **2×3** với **6 asset tách**; so side-by-side với trang table + trang chart
- **Mobile/tablet:** hero tỉ lệ hợp lý (B.4 / C.6.10) — không cắt ảnh mất subject, không mất/đè chữ overlay; logo + kicker đọc được
- **Nhóm A mobile:** table scroll-x cục bộ; chart stack đọc được (C.6.10)
- font thực sự load đúng; typography / content width / spacing rhythm gần PDF (desktop)
- line wrapping không lệch lớn; bullet/list đúng geometry
- links/colours đúng; component đặc thù đúng
- không còn visual difference lớn khi compare side-by-side (desktop)
- desktop fidelity đạt trước responsive; mobile/tablet QA hero + content pass
- **không** tái tạo pagination không cần thiết của PDF
