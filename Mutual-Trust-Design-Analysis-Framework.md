# Phân tích thiết kế bộ tài liệu Mutual Trust & Đề xuất Base Framework

*Phạm vi: phân tích 7 file PDF trong thư mục `demo-pdf`. Đây là tài liệu phân tích và đề xuất — chưa build HTML.*

## 0. Danh sách tài liệu & phân nhóm

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

Cả 3 nhóm dùng chung một hệ nhận diện (font, màu, logo, cấu trúc legal) nhưng khác nhau ở bố cục trang bìa, mật độ nội dung và một số component đặc thù. Phần dưới đây tách rõ theo yêu cầu: **điểm chung / biến thể / thành phần riêng**, sau đó đề xuất framework nền tảng.

---

## 1. Điểm chung giữa tất cả các PDF

### 1.1 Typography

| Vai trò | Font | Ghi chú |
|---|---|---|
| Heading / display (H1 bìa, H2 section, pull-quote) | **Baskerville** (serif) | Dùng nhất quán cho mọi tiêu đề lớn ở cả 7 file |
| Nội dung, bảng, chú thích, disclaimer | **Proxima Nova** — 3 weight: Light, Regular, Bold | Font chủ đạo, chiếm >90% lượng chữ trong mọi tài liệu |
| Ký tự bullet/glyph phụ | ArialMT, SymbolMT, đôi khi Wingdings2 | Đây là artefact do xuất file từ Word (glyph bullet mặc định), **không phải chủ đích thiết kế** — khi build lại nên thay bằng bullet CSS thuần |

Cỡ chữ đo được (điểm PDF, đã đối chiếu qua nhiều trang):
- Cỡ chữ thân bài phổ biến nhất: **9.5–11pt** (tuỳ tài liệu)
- Chú thích/nguồn biểu đồ, disclaimer: **6–8pt**
- Tiêu đề H2 trong bài (Baskerville): **16–22pt**
- Tiêu đề bìa: **28–40pt** tuỳ nhóm

**Line-height (đo bằng khoảng cách baseline giữa các dòng thân bài):** tỷ lệ ổn định ở cả 3 nhóm ≈ **1.2× cỡ chữ** (ví dụ font 10pt → line gap ~12.2pt). Đây là leading khá chặt, đặc trưng của tài liệu in ấn; khi đưa lên web nên cân nhắc nới lên 1.4–1.5 để dễ đọc trên màn hình mà vẫn giữ cảm giác "đặc" của bản gốc.

Đoạn văn không thụt đầu dòng, ngăn cách nhau bằng khoảng trắng dòng.

### 1.2 Màu sắc

Tất cả màu trích xuất trực tiếp từ dữ liệu PDF (có dao động nhỏ giữa các file do khác bản export/nén — đã gộp nhóm theo tông màu):

| Nhóm màu | Giá trị quan sát được | Vai trò |
|---|---|---|
| Đen/mực chữ | `#000000`, `#1B1B1F`, `#1B1B20` | Text chính |
| Xám phụ | `#8D8D90`, `#99999B`, `#545458` | Text phụ, caption |
| **Vàng đồng / cam (accent thương hiệu)** | `#D17B19`, `#D17A18`, `#CB962E`, `#CBA020`, `#C99329` | Hyperlink, số thứ tự section, tiêu đề nhấn, viền box |
| Xanh rêu đậm | `#00675A` | Dữ liệu dương (bảng số liệu) |
| Đỏ mận/maroon | `#822333` | Dữ liệu âm (bảng số liệu) — **thay cho đỏ/xanh lá tiêu chuẩn**, đây là lựa chọn thương hiệu có chủ đích |
| Đen "rich black" cho nền tối | `#06060D`, `#10161F`, `#1B1B1F` | Nền footer/back cover — không phải đen tuyền `#000000` |
| Xám xanh nhạt (nền box) | `#E0E4EB`, `#EAECF0`, `#F3F4F4`, `#C3CCD5` | Nền callout/pull-quote box |
| Trắng | `#FFFFFF` | Chữ trên ảnh/nền tối |

Ghi chú quan trọng: các mã vàng đồng (`#D17B19` … `#C99329`) rất có thể **cùng một màu thương hiệu** nhưng bị lệch nhẹ do từng file được export ở thời điểm/phần mềm khác nhau. Khi chuẩn hoá framework, nên xin bộ brand guideline chính thức thay vì lấy trung bình các giá trị này.

### 1.3 Khổ trang, lề & content width

- Khổ trang: **A4 – 595 × 842pt (210 × 297mm)**, tuyệt đối nhất quán ở cả 7 file.
- Lề trái/phải đo được dao động theo nhóm (chi tiết ở phần Biến thể), nhưng đặc điểm chung: **layout 1 cột** là mặc định, content width luôn chừa lề đối xứng hai bên, không có cột lề trang trí.
- Số trang + tên rút gọn tài liệu luôn nằm ở **footer, cùng một hàng, cách đều mép trang**, xuất hiện trên mọi trang kể cả trang bìa.

### 1.4 Hình ảnh & placement

- **Ảnh bìa (hero) luôn full-bleed** — tràn hết chiều ngang trang (từ mép trái đến mép phải, đôi khi tràn cả ra ngoài viền theo toạ độ âm), là ảnh chụp thật phong cách thiên nhiên/đời sống (núi, đồng cỏ, hoa, mặt nước, hàng rào trang trại), tông ấm, có lớp phủ tối (gradient/overlay) phía trên để chữ trắng nổi rõ.
- **Logo Mutual Trust** (biểu tượng mái vòm cách điệu + wordmark chữ hoa dãn chữ rộng) xuất hiện dưới 2 hình thức:
  - Trắng, đặt trực tiếp trên ảnh hero
  - Xám nhạt, đặt trên nền trắng (đầu trang nội dung, hoặc trong dải footer đen)
- Biểu đồ luôn có **tiêu đề chart + dòng "Source: …"** đặt ngay dưới, phong cách tối giản, không tô nền.

### 1.5 Footer / Disclaimer (thành phần lặp lại quan trọng nhất)

Cấu trúc pháp lý xuất hiện ở **mọi tài liệu**, gồm 3 tầng nội dung cố định:
1. Câu "Liability limited by a scheme approved under Professional Standards Legislation…"
2. Đoạn miễn trừ trách nhiệm tài chính đầy đủ (forward-looking statement disclaimer, khuyến nghị tìm tư vấn cá nhân…)
3. Câu **Acknowledgement of Country** ("Mutual Trust acknowledges and pays respect to the past and present Traditional Custodians…") — xuất hiện ở tất cả 7/7 file, không thiếu file nào.

Đi kèm luôn là khối liên hệ văn phòng (địa chỉ + số điện thoại nhiều chi nhánh: Melbourne, Sydney, Brisbane, Perth, Adelaide), email, website, ABN, AFSL.

---

## 2. Các biến thể theo nhóm tài liệu

### Nhóm A — Market Review
- Trang bìa: hero cao ~150–200pt, **tiêu đề 2 dòng overlay trực tiếp lên ảnh** (dòng lớn serif + dòng caps nhỏ hơn ngay dưới), **không có logo trên ảnh bìa** — logo chỉ nằm trong footer.
- Cỡ chữ thân bài nhỏ hơn nhóm khác (9–10pt) vì mật độ thông tin dày (nhiều bullet + bảng số liệu).
- Có **bảng dữ liệu tô màu theo giá trị** (xanh rêu = dương, mận đỏ = âm) — component đặc trưng chỉ nhóm này có.
- Trang cuối là **lưới 6 biểu đồ (2 cột × 3 hàng)**.
- Disclaimer nằm ngay trong dải nền đen ở cuối trang nội dung cuối cùng — **không tách thành trang bìa sau (back cover) riêng**.

### Nhóm B — Quarterly Outlook
- Trang bìa: logo + wordmark **căn giữa** trên ảnh hero, có đường kẻ ngang phân cách, rồi đến tiêu đề chung "Quarterly Outlook" (serif, lớn). **Tiêu đề bài viết cụ thể** ("Still waters run deep", "Equities: the tug of war") nằm ở khối nội dung ngay dưới ảnh, không đặt trên ảnh.
- Cấu trúc nhiều phần được **đánh số với heading màu vàng đồng** (ví dụ "4. How do we design resilient portfolios?").
- Có **callout/pull-quote box** mở đầu mỗi phần — nền xám xanh nhạt, trích lời chuyên gia nội bộ/khách mời (in caps, có tên + chức danh).
- Bố cục đôi khi chuyển sang **2 cột** (văn bản trái, biểu đồ/pie chart phải) cho các phần minh hoạ số liệu.
- **Có back cover riêng**: 1 trang cuối cùng nền đen tuyền, logo + tagline "Helping families achieve what matters most." căn giữa, đoạn disclaimer là **dài và đầy đủ nhất** trong 3 nhóm.
- Footer running text có thêm dòng "Written by [Tên tác giả] | [ngày]" — chi tiết này không xuất hiện ở 2 nhóm còn lại.

### Nhóm C — Perspective / Insight Article
- Trang bìa: hero cao hơn nhóm A (~210–320pt), **logo nhỏ đặt góc trên-trái ngay trên ảnh**; tiêu đề bài viết nằm **bên dưới ảnh** (trên nền trắng), không overlay lên ảnh như nhóm A.
- **Màu tiêu đề H1 không đồng nhất giữa 3 bài**: 2/3 bài dùng màu cam/vàng đồng thương hiệu, 1 bài ("Protecting intergenerational wealth…") dùng màu **xanh xám** (`#4E5E72`) — nhiều khả năng là điểm chưa nhất quán cần làm rõ với đội thương hiệu hơn là chủ đích.
- Không có bảng dữ liệu màu hay lưới biểu đồ như nhóm A.
- Callout box (nếu có) đa dạng nội dung tuỳ bài — xem mục 3 (thành phần riêng).
- Kết bài luôn có **khối chữ ký tác giả** (Tên in đậm, chức danh, "Mutual Trust") ngay trước phần legal.
- Disclaimer **ngắn gọn hơn** nhóm A/B, nằm ngay trên nền trắng cùng trang nội dung cuối, **không có back cover đen riêng**.

---

## 3. Thành phần riêng của từng PDF

| File | Thành phần độc quyền |
|---|---|
| June 2026 QMR & Oct 2025 MMR | Bảng "Global Markets" tô màu heat-style theo hiệu suất (2 file dùng chung format này, không xuất hiện ở file nào khác) |
| March 2026 Quarterly Outlook | Biểu đồ cột ngang "S&P 500 Index Sector Performance" minh hoạ riêng cho luận điểm bài |
| June 2026 Quarterly Outlook | Pie chart "Indicative Mutual Trust asset allocation"; danh sách 4 câu hỏi mở đầu dạng numbered list giới thiệu cấu trúc bài |
| Protecting Intergenerational Wealth | Box "Interested in learning more?" kèm ảnh thumbnail bìa podcast + link nghe; tiêu đề H1 màu xanh xám (biến thể màu riêng) |
| Perspective from Brendan Henderson | Sơ đồ flow-chart tự thiết kế (5 khối nối bằng mũi tên, minh hoạ tình huống "double death tax") — infographic phức tạp nhất trong toàn bộ 7 file, không lặp lại ở đâu khác |
| Strengthening Farm Safety | Callout box thuần trích dẫn (chỉ text + tên người trích, không ảnh, không sơ đồ) |

---

## 4. Đề xuất Base Framework

*Lưu ý: đây là đề xuất design token & component spec để làm nền tảng dựng HTML sau này — chưa build.*

### 4.1 Design tokens

**Font**
```
--font-serif: "Baskerville", Georgia, serif;      /* heading / display / pull-quote */
--font-sans:  "Proxima Nova", "Helvetica Neue", Arial, sans-serif; /* body */
--font-sans-weight-light: 300;
--font-sans-weight-regular: 400;
--font-sans-weight-bold: 700;
```
*(Proxima Nova là font thương mại có bản quyền — cần xác nhận license hoặc chọn font thay thế mã nguồn mở gần giống nếu build web công khai, ví dụ "Museo Sans"/"Nunito Sans" tuỳ ngân sách.)*

**Type scale (quy đổi tương đối từ pt gốc, line-height giữ tỷ lệ ~1.2 như bản in, có thể nới lên 1.4–1.5 cho web)**

| Token | Cỡ chữ | Font | Dùng cho |
|---|---|---|---|
| `--text-h1-cover` | 34–40px | Baskerville | Tiêu đề bìa |
| `--text-h1-caps` | 18–22px, letter-spacing rộng | Baskerville | Dòng phụ đề caps dưới H1 |
| `--text-h2` | 20–24px | Baskerville | Tiêu đề section trong bài |
| `--text-h3` | 14–15px, bold | Proxima Nova Bold | Sub-heading trong đoạn |
| `--text-body` | 14–15px | Proxima Nova Regular/Light | Nội dung chính |
| `--text-caption` | 11–12px | Proxima Nova Regular | Chú thích biểu đồ, nguồn |
| `--text-legal` | 10–11px | Proxima Nova Regular | Disclaimer, footer pháp lý |

**Màu sắc**
```
--color-ink:            #1A1A1A;   /* text chính, chuẩn hoá từ #000000/#1B1B1F */
--color-ink-muted:      #8C8C90;   /* text phụ/caption */
--color-accent-gold:    #C9932E;   /* CẦN XÁC NHẬN mã chính xác với brand guideline */
--color-positive:       #00675A;
--color-negative:       #822333;
--color-surface-dark:   #101018;   /* nền footer / back cover, không dùng đen tuyền */
--color-surface-tint:   #E7EAF0;   /* nền callout/quote box */
--color-white:          #FFFFFF;
```

**Spacing scale (ước lượng, làm mốc khởi điểm)**
```
--space-1: 4px   --space-2: 8px   --space-3: 16px
--space-4: 24px  --space-5: 32px  --space-6: 48px  --space-7: 64px
```

**Grid**
- Khổ trang gốc A4 → khi lên web dùng làm cảm hứng cho max-width nội dung, không cần giữ khổ cứng
- Content max-width đề xuất: **~700–760px** (tương ứng content width ~480–500pt trong 2 nhóm A/C; nhóm B hẹp hơn ~450pt do đôi khi chia 2 cột)
- Lề trái/phải: nhóm A/C tương đương ~54–58pt gốc (~19–20mm); nhóm B ~72pt (~25mm) — có thể hợp nhất về **1 giá trị lề chuẩn** khi dựng framework để nhất quán, thay vì giữ 2 chuẩn lề khác nhau như bản PDF gốc.

### 4.2 Thư viện component đề xuất

1. **Hero/Header** — 2 biến thể: (a) tiêu đề overlay trực tiếp lên ảnh — dùng cho Market Review; (b) logo overlay + tiêu đề tách sang khối nội dung — dùng cho Outlook/Insight
2. **Section heading** — có/không đánh số, màu cam accent hoặc đen tuỳ ngữ cảnh
3. **Callout/quote box** — nền xám nhạt, có thể chứa: trích dẫn + người nói, ảnh thumbnail + link, hoặc infographic tuỳ biến
4. **Data table** — style semantic màu dương/âm (dùng riêng cho báo cáo thị trường)
5. **Chart block** — đơn lẻ hoặc lưới 2 cột, luôn kèm caption + nguồn
6. **Author sign-off block** — tên, chức danh, "Mutual Trust"
7. **Footer running** — tên tài liệu (trái) + số trang (phải), có thể thêm tác giả/ngày tuỳ loại tài liệu
8. **Legal/disclaimer + Acknowledgement of Country** — 2 biến thể: inline cuối trang trắng (nhóm C) / back-cover nền tối riêng (nhóm A, B)
9. **Office contact grid** — 4–5 văn phòng, email, website, ABN/AFSL

### 4.3 Việc cần xác nhận trước khi build

- Xin bộ brand guideline chính thức (mã màu HEX/CMYK chuẩn, font Proxima Nova + Baskerville có license hợp lệ) — các giá trị màu trích từ PDF có sai lệch nhỏ (vài đơn vị hex) giữa các file do khác lần export.
- Xác nhận việc H1 màu xanh xám ở bài "Protecting Intergenerational Wealth" là chủ đích (theo chủ đề) hay chưa nhất quán — nếu là biến thể có chủ đích, nên định nghĩa rule (ví dụ: bài về "gia đình/thế hệ" dùng tông xanh, bài "chuyên môn/thuế/nông nghiệp" dùng tông cam).
- Quyết định có **hợp nhất 2 chuẩn lề** (nhóm A/C ~55pt vs nhóm B ~72pt) thành 1 grid chung hay giữ nguyên 2 biến thể lề theo loại tài liệu.
- Xác nhận có cần giữ nguyên bảng heat-color (nhóm A) và infographic flow-chart tuỳ biến (Brendan Henderson) như component tái sử dụng được, hay xử lý case-by-case.
