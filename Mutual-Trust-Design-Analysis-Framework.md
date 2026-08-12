# Mutual Trust — Design Analysis & Base Framework

*Phạm vi: phân tích 7 file PDF trong `demo-pdf` + đối chiếu Official Style Guide trên Figma. Đây là tài liệu phân tích và đề xuất — **chưa build HTML**.*

## Cách đọc tài liệu này

Hai nguồn thông tin được tách rõ — **không trộn giá trị suy đoán từ PDF vào design token chính thức**:

| Nguồn | Vai trò | Áp dụng cho |
|---|---|---|
| **A. Official MT Style Guide** (Figma) | **Source of truth cho token** (tên font, HEX brand, hệ type/UI chuẩn) | Font family, colour HEX, tên style (H1–H6, Text large…) |
| **B. Phân tích 7 PDF** | **Source of truth cho bản convert cụ thể** | Layout, placement, hierarchy thực tế, spacing, cỡ chữ trên trang, imagery, components, biến thể theo file |

### Nguyên tắc ưu tiên khi convert PDF → HTML

**Mục tiêu hàng đầu: like-for-like với PDF nguồn.** Style Guide không được làm trang “đúng brand token nhưng lệch bản PDF”.

| Ưu tiên | Cái gì | Ai thắng khi xung đột |
|---|---|---|
| 1 (cao nhất) | Nội dung, bố cục, placement, hierarchy, imagery, spacing giữa các khối | **PDF** |
| 2 | Cỡ chữ, line-height, độ đậm/nghiêng, indent list, khoảng hero↔content↔footer trên trang đó | **PDF** (đo từ nguồn; Style Guide chỉ là điểm xuất phát) |
| 3 | Font *family* và mã màu brand (Black / White / Light Grey / Grey / Ochre) | **Style Guide** — map lệch export PDF về HEX/font chuẩn, **miễn là nhìn vẫn khớp PDF** |
| 4 | Semantic / one-off trong PDF (bảng dương–âm, H1 lệch màu một bài…) | **PDF** — giữ và ghi chú PDF-specific |

**Quy tắc vận hành**

1. Style Guide cung cấp **tên token đúng** (Baskerville, Proxima Nova, Ochre `#CB962E`…) — tránh invent font/màu sai.
2. Khi type scale Style Guide (ví dụ H1 70px) **khác** cỡ trên PDF → **override theo PDF**. Không phóng cover lên 70px chỉ vì Style Guide ghi vậy.
3. Spacing Style Guide (`--space-*`) là baseline web; **khoảng cách thật trên trang theo PDF**.
4. Chỉ nới leading/body size so với bản in khi cần đọc trên màn hình — và chỉ vừa đủ; vẫn giữ cảm giác mật độ/hierarchy của PDF.
5. Không thay layout PDF bằng layout “chuẩn web” của Style Guide nếu làm lệch composition nguồn.

**Nguồn Style Guide**

- [Desktop Typography](https://www.figma.com/design/Gg76pDgGhJgQcPuh3Jigjd/Mutual-Trust-%E2%80%93-AI-Template?node-id=2-611) — node `2:611`
- [Colour](https://www.figma.com/design/Gg76pDgGhJgQcPuh3Jigjd/Mutual-Trust-%E2%80%93-AI-Template?node-id=2-466) — node `2:466`

---

# A. Official MT Style Guide (source of truth)

## A.1 Typefaces

| Vai trò | Font | Ghi chú Style Guide |
|---|---|---|
| Headings (H1–H6) | **Baskerville** Regular | Serif display / section titles |
| Body / UI text | **Proxima Nova** Regular + Bold | Sans — text large → small |

*(Proxima Nova là font thương mại — cần xác nhận license khi build web công khai.)*

## A.2 Desktop Typography system

Nguồn: Figma *Desktop Typography* (`2:611`). Line-height lấy từ style/computed trong file.

### Headings — Baskerville

| Style | Size | Line-height | Letter-spacing |
|---|---|---|---|
| Desktop Heading 1 | **70px** | 72px (~1.03) | 0 |
| Desktop Heading 2 | **48px** | 1.2 | 0 |
| Desktop Heading 3 | **40px** | 1.1 | 0 |
| Desktop Heading 4 | **32px** | 1.3 | 0 |
| Desktop Heading 5 | **24px** | 1.4 | 0 |
| Desktop Heading 6 | **16px** | 1.4 | 0 |

### Text styles — Proxima Nova

| Style | Size | Weight | Line-height |
|---|---|---|---|
| Text large | **20px** | Regular (Normal) | 1.5 |
| Text medium | **18px** | Regular (Normal) | 24px (≈1.33) |
| Text regular | **16px** | Regular **hoặc** Bold | 1.5 |
| Text small | **14px** | Regular **hoặc** Bold | 1.5 |

> **Convert rule:** bảng trên = token/style name chính thức. Khi build một PDF cụ thể, **size / line-height / spacing / placement lấy theo PDF** (xem B.2); chỉ giữ font family + colour HEX từ Style Guide. Không ép trang PDF vào đúng scale Desktop Typography nếu làm lệch bản gốc.

## A.3 Colour palette

Nguồn: Figma *Colour* (`2:466`).

| Tên (Style Guide) | HEX | Vai trò UI |
|---|---|---|
| **Black** | `#000000` | Text chính, mực chữ, nền tối khi cần đen tuyền |
| **White** | `#FFFFFF` | Nền trang, chữ trên ảnh/nền tối |
| **Light Grey** | `#F4F4F4` | Nền callout / pull-quote / surface phụ |
| **Grey** | `#767676` | Text phụ, caption, chú thích |
| **Ochre** | `#CB962E` | Accent — hyperlink, số thứ tự section, tiêu đề nhấn, viền box |

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
- Accent / link / nhấn: Ochre `#CB962E` (giữ underline/color theo treatment nguồn khi convert PDF)
- Surface phụ (callout, quote box): Light Grey `#F4F4F4` — **không** invent panel xám-xanh khác trừ khi PDF cụ thể bắt buộc match và đã ghi nhận ở mục B
- Heading: Baskerville; body/UI: Proxima Nova
- Không dùng màu ngoài 5 mã Style Guide cho brand UI; semantic data colours (nếu cần) nằm ở mục B.6

---

# B. Phân tích từ 7 PDF (layout & patterns)

*Phần này giữ nguyên giá trị phân tích thực tế từ PDF. Không dùng làm source of truth cho font/colour tokens — chỉ để layout, placement, spacing quan sát, families và component.*

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

| Quan sát PDF | Khớp Style Guide? |
|---|---|
| Heading / display / pull-quote → Baskerville | Có — dùng `--font-serif` |
| Body, bảng, caption, disclaimer → Proxima Nova (PDF còn thấy Light; Style Guide Desktop ghi Regular + Bold) | Có family; weight Light là biến thể PDF — khi build ưu tiên Regular/Bold theo Style Guide trừ khi PDF bắt buộc Light để match |
| Bullet glyph ArialMT / SymbolMT / Wingdings2 | Artefact Word export — **không** phải Style Guide; thay bằng bullet CSS |

## B.2 Type size & leading đo từ PDF *(override candidates)*

Các số đo dưới đây là **quan sát bản in**, không thay thế type scale Style Guide. Khi convert PDF → HTML: bắt đầu từ tokens mục A.2, rồi override size/line-height nếu cần fidelity.

| Vai trò trong PDF | Cỡ quan sát (pt) | Gợi ý map Style Guide (baseline) | Khi nào override |
|---|---|---|---|
| Tiêu đề bìa | 28–40pt | H2–H3 (48 / 40px) hoặc nhỏ hơn H1 70px | Hầu hết cover PDF nhỏ hơn H1 70px — **thường cần override xuống** |
| H2 section (Baskerville) | 16–22pt | H5–H6 (24 / 16px) | Override nhẹ theo file |
| Thân bài | 9.5–11pt | Text small / regular (14 / 16px) làm baseline web dễ đọc | Có thể giữ 14–16px web; nhóm A dày hơn có thể dùng `--text-small` |
| Caption / disclaimer | 6–8pt | Text small 14px (floor web) | PDF nhỏ hơn nhiều — web không nên xuống dưới ~11–12px vì accessibility |

**Line-height PDF:** ≈ **1.2×** cỡ chữ thân bài (leading in ấn chặt). Style Guide body dùng **1.5** — baseline web theo Style Guide; khi match PDF có thể siết về ~1.2–1.35 nếu cần cảm giác “đặc” của bản gốc.

Đoạn văn PDF: không thụt đầu dòng, ngăn cách bằng khoảng trắng dòng.

## B.3 Khổ trang, lề & content width

- Khổ trang: **A4 – 595 × 842pt (210 × 297mm)**, nhất quán cả 7 file.
- Layout mặc định: **1 cột**; content width chừa lề đối xứng, không có cột lề trang trí.
- Lề trái/phải đo được dao động theo nhóm:
  - Nhóm A/C ≈ **54–58pt** (~19–20mm)
  - Nhóm B ≈ **72pt** (~25mm)
- Khi lên web: A4 là cảm hứng max-width, không giữ khổ cứng. Content max-width đề xuất từ đo PDF: **~700–760px** (nhóm B hẹp hơn ~450pt content khi chia 2 cột).
- Số trang + tên rút gọn tài liệu luôn ở **footer, một hàng, cách đều mép trang**, kể cả trang bìa.

## B.4 Hình ảnh & placement

- **Ảnh bìa (hero) luôn full-bleed** — tràn hết chiều ngang; ảnh thiên nhiên/đời sống tông ấm; thường có gradient/overlay tối để chữ trắng đọc được.
- **Logo Mutual Trust** (mái vòm + wordmark caps):
  - Trắng trên ảnh hero (khi PDF có)
  - Xám/nhạt trên nền trắng hoặc dải footer tối
- Biểu đồ: **tiêu đề chart + "Source: …"** ngay dưới, tối giản, không tô nền.

## B.5 Footer / Disclaimer (recurring — mọi PDF)

Cấu trúc pháp lý xuất hiện ở **mọi tài liệu**, 3 tầng cố định:
1. "Liability limited by a scheme approved under Professional Standards Legislation…"
2. Đoạn miễn trừ trách nhiệm tài chính đầy đủ (forward-looking statement, khuyến nghị tư vấn cá nhân…)
3. **Acknowledgement of Country** — đủ 7/7 file

Đi kèm: khối liên hệ văn phòng (Melbourne, Sydney, Brisbane, Perth, Adelaide), email, website, ABN, AFSL.

## B.6 Màu quan sát trong PDF (không thuộc Style Guide palette)

PDF export từng lệch nhẹ quanh Ochre (`#D17B19`, `#D17A18`, `#CBA020`, `#C99329`…) và vài tông xám/đen phụ (`#1B1B1F`, `#8D8D90`, `#E0E4EB`…). **Khi chuẩn hoá: map về 5 mã Style Guide** (mục A.3).

**Semantic colours chỉ thấy ở bảng Market Review** (giữ khi build data table — PDF-specific, không có trong Figma Colour):

| Vai trò | HEX quan sát | Ghi chú |
|---|---|---|
| Dữ liệu dương | `#00675A` | Xanh rêu |
| Dữ liệu âm | `#822333` | Đỏ mận — thay đỏ/xanh lá tiêu chuẩn |

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

### Nhóm B — Quarterly Outlook
- Trang bìa: logo + wordmark **căn giữa** trên hero, đường kẻ ngang, tiêu đề chung "Quarterly Outlook" (serif). **Tiêu đề bài viết cụ thể** nằm dưới ảnh trên nền trắng.
- Section **đánh số + heading accent Ochre** (ví dụ "4. How do we design resilient portfolios?").
- **Callout/pull-quote box** mở đầu phần — nền surface phụ, trích lời (caps, tên + chức danh). PDF đôi khi dùng xám-xanh (`#E0E4EB`…). Khi convert file đó: **match nền như PDF**; nếu gần Light Grey thì map `#F4F4F4`, nếu lệch rõ thì giữ giá trị gần PDF (không đổi sang Light Grey nếu làm lệch nhìn).
- Đôi khi **2 cột** (text trái / chart phải).
- **Back cover riêng**: nền tối, logo + tagline "Helping families achieve what matters most.", disclaimer dài nhất 3 nhóm.
- Footer running có thêm "Written by [Tên] \| [ngày]" — không thấy ở nhóm A/C.

### Nhóm C — Perspective / Insight Article
- Trang bìa: hero cao hơn nhóm A (~210–320pt), **logo nhỏ góc trên-trái trên ảnh**; tiêu đề bài **dưới ảnh** (nền trắng), không overlay như nhóm A.
- **H1 màu không đồng nhất giữa 3 bài**: 2/3 dùng Ochre thương hiệu; 1 bài ("Protecting intergenerational wealth…") dùng xanh xám `#4E5E72` — **không có trong Style Guide Colour**; cần xác nhận với brand (chủ đích vs lệch export). Khi chưa chốt: mặc định Ochre/Black theo Style Guide.
- Không có bảng heat-color hay lưới 6 chart như nhóm A.
- Callout (nếu có) đa dạng theo bài — xem B.8.
- Kết bài: **khối chữ ký tác giả** (tên đậm, chức danh, "Mutual Trust") trước legal.
- Disclaimer ngắn hơn, trên nền trắng cuối trang nội dung — **không** back cover đen riêng.

## B.8 Thành phần riêng của từng PDF

| File | Thành phần độc quyền |
|---|---|
| June 2026 QMR & Oct 2025 MMR | Bảng "Global Markets" tô màu heat-style theo hiệu suất (2 file dùng chung format) |
| March 2026 Quarterly Outlook | Biểu đồ cột ngang "S&P 500 Index Sector Performance" |
| June 2026 Quarterly Outlook | Pie chart "Indicative Mutual Trust asset allocation"; 4 câu hỏi mở đầu dạng numbered list |
| Protecting Intergenerational Wealth | Box "Interested in learning more?" + thumbnail podcast + link; H1 xanh xám (biến thể ngoài Style Guide) |
| Perspective from Brendan Henderson | Flow-chart 5 khối + mũi tên ("double death tax") — infographic phức tạp nhất, không lặp lại |
| Strengthening Farm Safety | Callout thuần trích dẫn (text + attribution, không ảnh/sơ đồ) |

---

# C. Base Framework đề xuất

*Chưa build. Tokens visual = Style Guide; layout/component variants = PDF patterns.*

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

- Content max-width đề xuất: **~700–760px** (cảm hứng từ content width PDF)
- Một content column dùng chung cho logo, hero text, body, program blocks, footer (cùng mép trái/phải)
- Quyết định còn mở: hợp nhất lề A/C (~55pt) vs B (~72pt) thành 1 grid web, hay giữ 2 biến thể theo document family

## C.3 Thư viện component (từ recurring PDF patterns + Style Guide styling)

1. **Hero/Header** — 2 biến thể layout PDF: (a) title overlay trên ảnh — Market Review; (b) logo overlay + title tách khối nội dung — Outlook/Insight. Styling chữ/logo theo Style Guide colours.
2. **Section heading** — Baskerville; có/không đánh số; accent Ochre hoặc Black theo ngữ cảnh PDF.
3. **Callout/quote box** — nền Light Grey; nội dung: quote + attribution, podcast thumb + link, hoặc infographic.
4. **Data table** — semantic `--color-positive` / `--color-negative` (PDF-specific, nhóm A).
5. **Chart block** — đơn lẻ hoặc lưới 2 cột; luôn caption + Source.
6. **Author sign-off** — tên, chức danh, "Mutual Trust" (nhóm C).
7. **Footer running** — tên tài liệu (trái) + số trang (phải); optional author/date (nhóm B).
8. **Legal + Acknowledgement of Country** — inline cuối trang trắng (C) / dải hoặc back-cover nền tối (A, B).
9. **Office contact grid** — 4–5 văn phòng, email, website, ABN/AFSL.

## C.4 Checklist convert PDF → HTML

1. Đọc toàn bộ PDF nguồn — **kết quả phải giống PDF** (nội dung + bố cục + hierarchy + spacing).
2. Gán font family + map màu brand sang token Style Guide (mục A) — không invent font/HEX.
3. Chọn document family (A / B / C) và hero/footer variant (mục B.7).
4. **Đặt size / line-height / spacing / placement theo PDF** (B.2–B.4); Style Guide type scale chỉ dùng làm điểm xuất phát / đặt tên token, không được thắng PDF khi xung đột.
5. Giữ toàn bộ copy PDF — không omit / invent / duplicate.
6. Semantic / one-off colours theo PDF khi có (bảng dương–âm, biến thể H1…).
7. Responsive chỉ adapt khi cần (stack, chart grid) — không đổi composition desktop so với PDF.
8. **Chưa deploy / chưa build** cho đến khi được yêu cầu.

## C.5 Việc còn cần xác nhận

- License font Proxima Nova + Baskerville khi build web công khai.
- H1 xanh xám `#4E5E72` ở "Protecting Intergenerational Wealth": chủ đích hay lệch? Style Guide Colour **không** có mã này — mặc định map Ochre/Black cho đến khi brand xác nhận.
- Hợp nhất 2 chuẩn lề (A/C vs B) hay giữ 2 biến thể theo family.
- Heat-table (nhóm A) và flow-chart (Brendan Henderson): component tái sử dụng hay case-by-case.
- Có thêm Mobile Typography trong Style Guide Figma hay không — hiện tài liệu lấy **Desktop Typography** (`2:611`) làm baseline; mobile scale sẽ bổ sung khi có node chính thức.
