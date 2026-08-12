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

**Không** extract/crop logo từ PDF khi convert HTML trừ khi URL dưới không khớp biến thể trên PDF. Mọi template (`template.html`, `template-perspective.html`, và các family template khác) dùng một trong hai URL sau — **chọn theo loại logo mà PDF gốc đang dùng**:

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

**Nhóm A — Market Review** (báo cáo thị trường định kỳ, nhiều số liệu)

- `June_2026_Quarterly_Market_Review.pdf` (3 trang)
- `October2025MonthlyMarketReview.pdf` (3 trang)

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
- Biểu đồ: **tiêu đề chart + "Source: …"** ngay dưới, tối giản, không tô nền.

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
| **A — Market Review** | Cùng nội dung legal + contacts; thường dải nền tối cuối trang; có thể có `logo-m.svg` — match PDF |
| **B — Outlook** | Back cover tối: logo stacked / tagline *"Helping families achieve what matters most."* + disclaimer dài; byline PDF đưa vào article, không chạy footer |

Số điện thoại / địa chỉ / ABN·AFSL lấy từ **PDF đang convert** (bảng trên chỉ là skeleton — luôn đối chiếu nguồn).

## B.6 Màu quan sát trong PDF (không thuộc Style Guide palette)

PDF export từng lệch nhẹ quanh Ochre (`#D17B19`, `#D17A18`, `#CBA020`, `#C99329`…) và vài tông xám/đen phụ (`#1B1B1F`, `#8D8D90`, `#E0E4EB`…). **Khi chuẩn hoá: map về 5 mã Style Guide** (mục A.3).

**Semantic colours chỉ thấy ở bảng Market Review** (giữ khi build data table — PDF-specific, không có trong Figma Colour):

| Vai trò       | HEX quan sát | Ghi chú                             |
| ------------- | ------------ | ----------------------------------- |
| Dữ liệu dương | `#00675A`    | Xanh rêu                            |
| Dữ liệu âm    | `#822333`    | Đỏ mận — thay đỏ/xanh lá tiêu chuẩn |

```
/* PDF-specific semantic — chỉ data table Market Review */
--color-positive: #00675A;
--color-negative: #822333;
```

## B.7 Biến thể theo nhóm tài liệu

### Nhóm A — Market Review

- Trang bìa: hero cao ~150–200pt, **tiêu đề 2 dòng overlay trực tiếp lên ảnh** (serif lớn + caps nhỏ hơn), **không có logo trên ảnh bìa** — logo chỉ trong footer.
- Thân bài dày hơn (PDF ~9–10pt) vì nhiều bullet + bảng.
- Có **bảng dữ liệu tô màu theo giá trị** (xanh rêu = dương, mận đỏ = âm) — đặc trưng nhóm này.
- Trang cuối: **lưới 6 biểu đồ (2 cột × 3 hàng)**.
- Disclaimer trong dải nền tối cuối trang nội dung — **không** tách back cover riêng.

**Template HTML tái sử dụng:** `website/template-market-review.html`  
Token `--mr-*`; class `family-market-review`. Khi convert PDF cụ thể: copy template → override geometry/type từ đo PDF (C.6); điền heat table / chart panels / dark footer theo B.5 + checklist B.5.4. Mobile: hero nới tỉ lệ (B.4); contacts 2 cột (B.5).

### Nhóm B — Quarterly Outlook

- Trang bìa: logo + wordmark **căn giữa** trên hero, đường kẻ ngang, tiêu đề chung "Quarterly Outlook" (serif). **Tiêu đề bài viết cụ thể** nằm dưới ảnh trên nền trắng.
- Section **đánh số + heading accent Ochre** (ví dụ "4. How do we design resilient portfolios?").
- **Callout/pull-quote box** mở đầu phần — nền surface phụ, trích lời (caps, tên + chức danh). PDF đôi khi dùng xám-xanh (`#E0E4EB`…). Khi convert file đó: **match nền như PDF**; nếu gần Light Grey thì map `#F4F4F4`, nếu lệch rõ thì giữ giá trị gần PDF (không đổi sang Light Grey nếu làm lệch nhìn).
- Đôi khi **2 cột** (text trái / chart phải).
- **Back cover riêng**: nền tối, logo + tagline "Helping families achieve what matters most.", disclaimer dài nhất 3 nhóm.
- Footer running PDF có thêm "Written by [Tên] \| [ngày]" — không thấy ở nhóm A/C. Trên web: đưa byline/meta vào khối article (một lần), không lặp theo trang.

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
| June 2026 QMR & Oct 2025 MMR        | Bảng "Global Markets" tô màu heat-style theo hiệu suất (2 file dùng chung format)                       |
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

1. **Hero/Header** — 2 biến thể layout PDF: (a) title overlay trên ảnh — Market Review (`template-market-review.html`); (b) logo trên ảnh + title tách khối nội dung — Outlook/Insight (`template-perspective.html`). Logo: URL A.5 (`logo-m.svg` hoặc `MT-Logo.svg` theo PDF). Hero trong `--page-max`; `aspect-ratio` = W/H dải PDF (B.4); scrim contrast (C.6.3).
2. **Section heading** — Baskerville; có/không đánh số; accent Ochre hoặc Black theo ngữ cảnh PDF.
3. **Callout/quote box** — nền Light Grey; nội dung: quote + attribution, podcast thumb + link, hoặc infographic.
4. **Data table** — semantic `--color-positive` / `--color-negative` (PDF-specific, nhóm A) — markup `.mr-table` / `.is-positive` / `.is-negative` trong template Market Review.
5. **Chart block** — đơn lẻ hoặc lưới 2 cột × 3 hàng (nhóm A: `.mr-chart-grid`); luôn caption + Source; **một ảnh mỗi panel**, stack mobile.
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
12. **Footer/legal** — bắt đầu từ cấu trúc chuẩn **B.5**; đo PDF rồi override (B.5.4). Không số trang / running footer.
13. **Không tái tạo pagination của PDF trên web.** Nội dung chuyển thành continuous document flow. Page boundary của PDF chỉ dùng làm checkpoint trong visual QA để phát hiện cumulative spacing/typography drift (C.6.8–C.6.9).
14. Chạy Visual Comparison Loop (C.6.8) — tối đa 3 vòng correction nếu còn khác biệt đáng kể; **desktop fidelity đạt trước** rồi mới responsive (C.6.10).
15. Chỉ đánh dấu hoàn thành khi đạt Definition of Done (C.6.11).
16. **Chưa deploy** cho đến khi được yêu cầu.

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

Không tự động áp style link web generic (đặc biệt **không** mặc định underline).

Link phải đối chiếu PDF về: **colour**, **có/không underline**, **font-size**, font weight. Ví dụ _Protecting Intergenerational Wealth_ (và nhiều Perspective): link `#D17B19` / ochre-tinted, **không gạch chân**. Hover có thể thêm underline nhẹ — chỉ là enhancement web, không đổi base style lệch PDF.

**Contacts meta (email / www) trong footer B.5:**

- Cùng **font-size / line-height** với dòng địa chỉ / SĐT (thường ~7pt) — không để link “phình” hơn cột văn phòng.
- **Không underline** trừ khi PDF gạch chân rõ.
- Tránh rule kiểu `.perspective-legal a { text-decoration: underline }` làm **rò** xuống `.perspective-contacts a`. Chỉ style link trong `.perspective-legal > p` (disclaimer) khi PDF có.

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

**Desktop:** PDF fidelity ưu tiên cao nhất — hero `aspect-ratio` = W/H dải PDF trong `--page-max` (B.4).

**Tablet/mobile — giữ:** visual identity, typography hierarchy, assets, colours, content order, component meaning, hướng subject hero, scrim.

**Cho phép:** stack columns, giảm font-size hợp lý, đổi padding, **nới tỉ lệ / min-height hero** (B.4 mobile), scale logo/kicker, tinh chỉnh `background-position`, xử lý chart/table responsive.

**Hero mobile QA (bắt buộc trước khi Done):**

1. Logo + mọi chữ overlay **nằm trọn** trong hero — không cắt, không tràn đáy/mép.
2. Chủ thể ảnh (hoa, người, horizon…) vẫn nhận ra; không crop mất cụm chính vì band quá dẹt.
3. Chữ không đè nặng lên vùng sáng/chi tiết tới mức mất đọc (điều chỉnh size/position/scrim tối thiểu).
4. Không horizontal scroll; hero vẫn trong page shell (không bắt buộc full browser width).

Không cố giữ kích thước vật lý A4 / đúng H PDF tuyệt đối trên mobile nếu làm hỏng (1)–(3).

### C.6.11 Definition of Done

Một conversion chỉ hoàn thành khi:

- đúng toàn bộ nội dung; đúng assets; logo đúng variant và placement
- **Desktop:** `--page-max` = khổ PDF; hero trong shell, **aspect-ratio W/H** → chiều cao khớp PDF; crop/position/orientation không cắt chủ thể; overlay/scrim khớp PDF khi cần; logo/chữ đủ contrast
- **Mobile/tablet:** hero tỉ lệ hợp lý (B.4 / C.6.10) — không cắt ảnh mất subject, không mất/đè chữ overlay; logo + kicker đọc được
- font thực sự load đúng; typography / content width / spacing rhythm gần PDF (desktop)
- line wrapping không lệch lớn; bullet/list đúng geometry
- links/colours đúng; component đặc thù đúng
- không còn visual difference lớn khi compare side-by-side (desktop)
- desktop fidelity đạt trước responsive; mobile/tablet QA hero + content pass
- **không** tái tạo pagination không cần thiết của PDF
