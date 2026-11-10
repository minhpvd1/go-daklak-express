# HỒ SƠ ĐỀ XUẤT KỸ THUẬT & DỰ TOÁN KINH PHÍ
## DỰ ÁN: NỀN TẢNG ĐIỀU PHỐI VẬN TẢI & TIỆN CHUYẾN ĐỊA PHƯƠNG
**Địa bàn triển khai:** Huyện Krông Pắk & Huyện Krông Ana – Tỉnh Đắk Lắk  
**Tiêu chuẩn cấu trúc:** Phân rã công việc WBS (Work Breakdown Structure)  
**Mã tài liệu:** `PRP-LMP-DKL-2026` | **Phiên bản:** `1.1-Production`

---

> ### 📌 NGUYÊN TẮC THIẾT KẾ & TIẾP CẬN KỸ THUẬT
> Tài liệu này được xây dựng dựa trên nguyên lý **Kiến trúc Tinh gọn (Lean Architecture)** và mô hình dịch vụ đám mây chuyên dụng (BaaS/PaaS). 
> Hệ thống ứng dụng chuẩn công nghệ **PWA (Progressive Web App)** đa nền tảng cho khách hàng kết hợp ứng dụng chuyên dụng cho tài xế, loại bỏ hoàn toàn các rào cản dung lượng bộ nhớ trên điện thoại phổ thông tại địa bàn huyện, đồng thời không phát sinh chi phí duy trì tài khoản Apple Developer đắt đỏ. 
> Toàn bộ giải pháp được thiết kế khép kín, bảo đảm tính sẵn sàng cao, vận hành bền bỉ và kiểm soát chi phí thực tế tối ưu ngay từ ngày đầu đi vào hoạt động.

---

## PHẦN I: CẤU TRÚC PHÂN CHIA CÔNG VIỆC CHI TIẾT (WBS BREAKDOWN)

Hệ thống được thiết kế theo mô hình **Tam giác Điều phối Thời gian thực (Real-time Tri-party Dispatch Framework)**, bảo đảm tính toàn vẹn dữ liệu, chống rớt cuốc và tối ưu hóa trải nghiệm người dùng mạng 4G nông thôn:

```
                                [HỆ THỐNG ĐIỀU PHỐI VẬN TẢI ĐỊA PHƯƠNG]
                                                   │
         ┌─────────────────────────┬───────────────┴───────────────┬─────────────────────────┐
         ▼                         ▼                               ▼                         ▼
   [WBS 1.0 CORE]          [WBS 2.0 PASSENGER]             [WBS 3.0 DRIVER]          [WBS 4.0 ADMIN]
 Kiến trúc Nền tảng       Giao diện Khách hàng            Ứng dụng Tài xế           Hệ thống Quản trị
 & Cơ sở Dữ liệu          (PWA & Web Mobile)              (Android Engine)           & Điều phối viên
```

### WBS 1.0: KIẾN TRÚC LÕI, CƠ SỞ DỮ LIỆU & BẢO MẬT (CORE INFRASTRUCTURE)
* **1.1. Thiết kế Lược đồ Dữ liệu Quan hệ (Relational Schema Design):**
  * Thiết lập cụm cơ sở dữ liệu PostgreSQL chuẩn hóa bậc 3 (3NF) trên nền tảng Cloud BaaS chuyên dụng.
  * Định nghĩa các bảng thực thể: `Users`, `Drivers`, `Vehicles`, `Rides`, `Trip_Stages`, `Wallets`, `Transactions`, `Audit_Logs`.
* **1.2. Máy trạng thái Vòng đời Chuyến đi (Trip Lifecycle State Machine):**
  * Xây dựng máy trạng thái hữu hạn kiểm soát 8 trạng thái cuốc xe:
    `REQUESTED` ➔ `BROADCASTING` ➔ `ACCEPTED` ➔ `DRIVER_ARRIVING` ➔ `IN_TRANSIT` ➔ `COMPLETED` (hoặc `CANCELLED` / `EXPIRED`).
  * Khóa logic chống nhận đúp cuốc (Row-level Mutex Lock): Khi 2 tài xế cùng bấm nhận 1 cuốc trong cùng 1 thời điểm, hệ thống bảo đảm chỉ 1 tài xế duy nhất nhận thành công.
* **1.3. Đồng bộ Tọa độ Vệ tinh Thời gian thực (Real-time Pub/Sub Engine):**
  * Cấu hình kênh truyền thông hai chiều WebSocket truyền tải tọa độ GPS tài xế về máy khách hàng với độ trễ < 300ms, tự động nội suy vị trí mượt mà.
* **1.4. Tự động hóa Khớp lệnh Nạp Ví VietQR (Automated Webhook Ledger):**
  * Xây dựng Webhook Endpoint nhận tín hiệu biến động số dư ngân hàng qua giao thức bảo mật chữ ký HMAC-SHA256, tự động định danh mã giao dịch và nạp tiền vào ví tài xế trong 3 giây.

### WBS 2.0: PHÂN HỆ KHÁCH HÀNG (PASSENGER CLIENT - PWA WEB APP)
* **2.1. Công nghệ Progressive Web App (Cài đặt 1 Chạm không qua App Store):**
  * Hỗ trợ chuẩn PWA đa nền tảng:
    * Trên **iPhone (Safari):** Hướng dẫn khách bấm nút *Chia sẻ* ➔ Chọn *Thêm vào Màn hình chính (Add to Home Screen)*.
    * Trên **Android (Chrome/Cốc Cốc):** Tự động hiển thị nút cài đặt ứng dụng trực tiếp ra màn hình điện thoại chỉ với 1 chạm.
  * Khởi chạy ở chế độ Độc lập (Standalone Mode): Mở ứng dụng toàn màn hình, ẩn thanh địa chỉ trình duyệt, hoạt động mượt mà và trực quan như ứng dụng tải từ kho ứng dụng, dung lượng siêu nhẹ (< 1MB) giúp máy nào cũng cài được.
* **2.2. Giao diện Đặt xe 3 Chạm Tối giản (3-Tap Booking UI):**
  * Tự động ghim điểm đón qua GPS điện thoại; gợi ý nhanh các điểm nóng địa phương: Chợ Phước An, Bệnh viện Krông Pắk, Ngã 3 Buôn Trấp, Ngã 6 Buôn Ma Thuột.
  * Lựa chọn 3 dịch vụ trọng tâm: **Xe Ôm / Giao Hàng** | **Xe Ghép Tiện Chuyến BMT (theo ghế)** | **Bao Trọn Xe Ô tô**.
* **2.3. Định vị Xe & Dự toán Chi phí Minh bạch (Fare Estimation Engine):**
  * Tính cước tự động theo ma trận khoảng cách: Hiển thị giá cước cố định trước khi bấm đặt xe.
  * Màn hình theo dõi hành trình trực quan kèm nút **SOS khẩn cấp** và tính năng gửi thông tin chuyến đi cho người thân.

### WBS 3.0: PHÂN HỆ TÀI XẾ (DRIVER PARTNER APPLICATION - FLUTTER ANDROID)
* **3.1. Thu nhận Đơn hàng & Cảnh báo Âm thanh (Acoustic Dispatch Dispatcher):**
  * Tích hợp chuông báo âm lượng lớn và rung liên tục, hoạt động ổn định cả khi màn hình điện thoại đang khóa hoặc khi tài xế đang di chuyển ngoài đường.
  * Hiển thị bảng thông tin tóm tắt trong 15 giây: Điểm đón, Điểm trả, Giá cước ròng thực nhận, Khoảng cách đón.
* **3.2. Bản đồ Điều hướng Chuyên dụng (In-app Turn-by-Turn Navigation):**
  * Tích hợp SDK bản đồ vector hỗ trợ tiếng Việt, dẫn đường tối ưu tránh các đoạn đường xấu hoặc ngõ cụt tại địa bàn nông thôn.
* **3.3. Sổ cái Tài chính & Quản trị Ví Tài xế (Driver Wallet & Ledger Module):**
  * Hiển thị số dư thực tế, lịch sử trừ phí sàn (16%) minh bạch trên từng cuốc xe.
  * Nút "Nạp tiền nhanh": Tạo mã VietQR cá nhân hóa kèm mã nạp tiền tự động. Cơ chế tự động khóa nhận cuốc khi số dư chạm ngưỡng an toàn (20.000đ).

### WBS 4.0: BÀN ĐIỀU PHỐI TRUNG TÂM & QUẢN TRỊ VIÊN (WEB ADMIN & DISPATCH CONSOLE)
* **4.1. Bản đồ Giám sát Vệ tinh Tổng thể (Geospatial Live Radar):**
  * Quan sát trực tiếp mật độ phân bổ tài xế đang trực tuyến (Online/Busy/Offline) trên toàn địa bàn 2 huyện.
* **4.2. Bàn Tổng đài Điều phối Bán tự động (Hybrid Call-Center Desk):**
  * Giao diện nhập nhanh cho nhân viên trực điện thoại: Tiếp nhận cuộc gọi của bà con lớn tuổi -> Nhập điểm đón -> Hệ thống tự quét và đẩy cuốc xuống app tài xế gần nhất.
* **4.3. Module Quản trị Bảng cước & Cấu hình Địa phương (Dynamic Pricing Policy):**
  * Cài đặt giá mở cửa, giá/km, phụ phí đón xa ngoài bán kính 3km, chính sách thưởng hoàn thành cuốc và quản lý doanh thu đối soát.

> **🛡️ TIÊU CHUẨN AN TOÀN DỮ LIỆU & CHỐNG LỖI MẠNG ĐỊA PHƯƠNG:**
> 1. **Bảo đảm Tính nhất quán Giao dịch (ACID Ledger):** Mọi thao tác trừ phí sàn và nạp ví tài xế đều được thực thi trong một Database Transaction duy nhất, bảo đảm tuyệt đối không xảy ra hiện tượng cộng lệch ví hay trừ tiền hai lần.
> 2. **Cơ chế Tự động Kết nối lại (Auto-reconnect & Offline Resilience):** Khi tài xế di chuyển qua các cung đường lõm sóng 4G tại Krông Pắk / Krông Ana, ứng dụng tự động lưu trữ tạm thời tọa độ và tự động truyền tải lại ngay khi có sóng, không làm gián đoạn hành trình.
> 3. **Nhật ký Kiểm toán Minh bạch (Tamper-proof Audit Trail):** Toàn bộ lịch sử nhận cuốc, hủy cuốc, thời gian đón trả và số tiền thực nhận được lưu trữ bảo mật, phục vụ công tác đối soát minh bạch giữa đơn vị vận hành và tài xế đối tác.

---

## PHẦN II: DỰ TOÁN BÁO GIÁ KỸ THUẬT & HẠ TẦNG (FINANCIAL ESTIMATE)

Chi phí được cấu trúc trọn gói toàn diện, bảo đảm tính minh bạch, khép kín và loại trừ hoàn toàn các chi phí phát sinh ẩn:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          BẢNG BÁO GIÁ DỰ TOÁN CHI TIẾT (VNĐ)                            │
├───────┬────────────────────────────────────────────────────────┬───────────────────────┤
│ MÃ    │ HẠNG MỤC CÔNG VIỆC & PHÂN PHỔI TÀI NGUYÊN HỆ THỐNG     │ KINH PHÍ TRỌN GÓI     │
│ WBS   │                                                        │ (TOÀN DIỆN HỆ THỐNG)  │
├───────┼────────────────────────────────────────────────────────┼───────────────────────┤
│ **1** │ **Thuật toán Điều phối & Xử lý Lộ trình Tự động**      │ **1.300.000 VNĐ**     │
│       │ • Thiết lập thuật toán phân bổ cuốc xe theo bán kính   │                       │
│       │   tối ưu, module tính toán ghép chuyến thông minh      │                       │
│       │   và quy trình kiểm thử tự động.                       │                       │
├───────┼────────────────────────────────────────────────────────┼───────────────────────┤
│ **2** │ **Hạ tầng Cloud Server & Realtime Engine**             │ **1.200.000 VNĐ**     │
│       │ • Khởi tạo Database PostgreSQL phân tán.               │ (Bảo trợ trọn gói     │
│       │ • Kênh truyền Pub/Sub WebSocket GPS đa luồng.          │  03 tháng hạ tầng)    │
├───────┼────────────────────────────────────────────────────────┼───────────────────────┤
│ **3** │ **Bản quyền Map Routing & Tọa độ Địa phương**          │ **950.000 VNĐ**     │
│       │ • Cấu hình Mapbox / OSRM Geocoding API.                │                       │
│       │ • Tích hợp gói 30.000 lượt quét bản đồ/tháng           │                       │
│       │   (Bảo đảm không phát sinh phụ phí vận hành).          │                       │
├───────┼────────────────────────────────────────────────────────┼───────────────────────┤
│ **4** │ **Tích hợp Cổng Nạp Ví Tự động VietQR Webhook**        │ **750.000 VNĐ**       │
│       │ • Kết nối cổng tự động ngân hàng (MB Bank / VCB).      │                       │
│       │ • Cơ chế kiểm tra đối soát giao dịch tự động.          │                       │
├───────┼────────────────────────────────────────────────────────┼───────────────────────┤
│ **5** │ **Công đoạn Setup, Đóng gói & Bàn giao Hệ thống**       │ **1.600.000 VNĐ**     │
│       │ • Triển khai Web App chuẩn PWA (Safari/Chrome).        │                       │
│       │ • Biên dịch file cài đặt Android APK Tài xế.           │                       │
│       │ • Bàn giao Bàn điều phối Web Admin & Hướng dẫn.        │                       │
├───────┴────────────────────────────────────────────────────────┼───────────────────────┤
│ 👉 **TỔNG KINH PHÍ ĐẦU TƯ TRỌN GÓI (VNĐ)**                    │ **5.800.000 VNĐ**     │
└────────────────────────────────────────────────────────────────┴───────────────────────┘
```

> **📌 Ghi chú Phân bổ Kỹ thuật & Hạ tầng Vận hành:**
> * **Cơ chế Tối ưu Hạ tầng (Zero-idle Overhead):** Toàn bộ tài nguyên máy chủ được cấu hình theo mô hình điện toán đám mây tự động co giãn. Trong giai đoạn chạy đà, hệ thống hoạt động hoàn toàn trong định mức tài nguyên tối ưu, không làm phát sinh bất kỳ khoản phụ phí máy chủ bất thường nào cho đối tác.
> * **Tối ưu Chi phí Nền tảng với PWA:** Việc ứng dụng chuẩn công nghệ PWA cho khách hàng giúp dự án không phải trả phí duy trì tài khoản Apple Developer (2.500.000đ/năm), không chịu rủi ro bị xét duyệt chính sách hay bị từ chối cập nhật phiên bản.
> * **Quyền chọn Gia hạn Hạ tầng Linh hoạt:** Sau khi kết thúc thời gian 03 tháng bảo trợ hạ tầng ban đầu trọn gói, chi phí duy trì máy chủ thực tế chỉ dao động từ 150.000đ – 250.000đ/tháng tùy theo lưu lượng cuốc xe thực tế.

---

## PHẦN III: KẾ HOẠCH TRIỂN KHAI & TIÊU CHUẨN NGHIỆM THU (PROJECT SCHEDULE)

Lộ trình kỹ thuật được phân bổ trong 21 ngày làm việc với các tiêu chí nghiệm thu rõ ràng:

| GIAI ĐOẠN | THỜI GIAN | NỘI DUNG KỸ THUẬT TRỌNG TÂM | TIÊU CHUẨN NGHIỆM THU KỸ THUẬT |
| :--- | :---: | :--- | :--- |
| **Giai đoạn 1** | Ngày 01 – 05 (Tuần 1) | Khởi tạo Cụm Database Cloud & Bản quyền Map Routing | CSDL PostgreSQL hoạt động ổn định; API Mapbox/OSRM tính toán khoảng cách và lộ trình chính xác tại 2 huyện. |
| **Giai đoạn 2** | Ngày 06 – 13 (Tuần 2) | Phát triển PWA Khách hàng & Ứng dụng Android APK Tài xế | PWA cài đặt mượt mà trên Safari iOS và Chrome Android; App Tài xế nhận tín hiệu cuốc xe kèm còi hú và rung liên tục. |
| **Giai đoạn 3** | Ngày 14 – 17 (Tuần 3) | Tích hợp Bàn Điều phối Web Admin & Webhook VietQR | Bàn điều phối theo dõi trực tiếp vị trí tài xế trên bản đồ; Quét mã VietQR tự động cộng số dư ví tài xế trong 3 giây. |
| **Giai đoạn 4** | Ngày 18 – 21 (Tuần 3-4) | Kiểm thử Tải trọng Thực địa (UAT) & Bàn giao Toàn diện | Thực hiện thành công 20 cuốc xe thử nghiệm thực tế; Bàn giao toàn bộ mã nguồn, tài khoản Admin tối cao và file APK. |

---

## PHẦN IV: CAM KẾT CHẤT LƯỢNG (SLA) & LỘ TRÌNH GIẢI NGÂN (ESCROW)

### 1. Cam kết Chất lượng & Giới hạn Trách nhiệm (SLA):
* **Cam kết năng lực vận hành:** Hệ thống bảo đảm xử lý ổn định tải trọng đồng thời tối thiểu **50 cuốc xe cùng lúc** và **100 tài xế trực tuyến liên tục** mà không xảy ra nghéz mạng hay trễ dữ liệu.
* **Quyền sở hữu & Bàn giao mã nguồn:** Sau khi hoàn tất nghiệm thu, toàn bộ mã nguồn (Source Code), quyền quản trị cơ sở dữ liệu và tài khoản quản trị viên tối cao (Super Admin) được chuyển giao 100% cho bên đối tác dự án.
* **Chính sách bảo hành kỹ thuật:** Hỗ trợ giám sát hệ thống và khắc phục miễn phí các lỗi phát sinh (Bug fix) trong vòng **90 ngày** kể từ ngày bàn giao chính thức.

### 2. Kế hoạch Giải ngân theo Mốc Giao phẩm (Milestone-based Escrow):
Nhằm bảo đảm tính minh bạch và an toàn tài chính tuyệt đối giữa hai bên:
* **Đợt 1 (40% - Khởi động):** **2.320.000 VNĐ** ngay sau khi thống nhất thông số kỹ thuật (Dùng để khởi tạo cụm Server Database Cloud và đăng ký các gói API bản đồ).
* **Đợt 2 (40% - Kiểm thử UAT):** **2.320.000 VNĐ** khi hoàn thành bản demo chạy thử nghiệm nội bộ: PWA Web App đặt được xe thật trên điện thoại, App Tài xế rung chuông còi hú và nhận đơn thành công.
* **Đợt 3 (20% - Nghiệm thu bàn giao):** **1.160.000 VNĐ** khi xuất bản chính thức Web App, bàn giao file APK cài đặt cho 10 tài xế đầu tiên và bàn giao tài khoản quản trị Web Admin.

---

```
                              ĐẠI DIỆN BỘ PHẬN KỸ THUẬT & GIẢI PHÁP
                                         (Ký và Xác nhận)
```
