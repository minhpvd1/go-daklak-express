# ĐẮK LẮK EXPRESS (DXP) — HỆ THỐNG ĐIỀU PHỐI VẬN TẢI & SÀN NÔNG SẢN TIỆN CHUYẾN
### Tuyến Trọng Điểm: Krông Pắk — Krông Ana — Buôn Ma Thuột

Hệ thống phần mềm hoàn chỉnh (Full Production Grade) kết hợp mô hình gọi xe tiện chuyến của **Grab** với sàn thương mại nông sản tốc độ cao của **TikTok Shop & Shopee Mall**, phục vụ trực tiếp bà con nông dân, nhà vườn và tài xế tại tỉnh Đắk Lắk.

---

## 🏛️ Kiến Trúc Tổng Thể

```text
[KHÁCH HÀNG / BÀN TỔNG ĐÀI] ──▶ Đặt xe ghép / Mua sầu riêng tươi
         │
         ▼
[MÁY CHỦ PRODUCTION DXP (server.py)] ──▶ Đa luồng, SQLite thread-safe
   ├── Database: users, drivers, sellers, products, rides, orders, wallet_transactions
   ├── Định vị & Routing: Haversine distance, bảng cước linh hoạt theo số ghế
   └── Cổng thanh toán: Sinh mã VietQR Napas 247 dynamic
         │
         ▼
[TÀI XẾ CỐP XE RỖNG] ──▶ Nhận cuốc xe + Nhận đơn nông sản tiện chuyến giao trong 45-60p
         │
         ▼
[KÊNH NGƯỜI BÁN / HTX] ──▶ Quản lý kho sầu riêng, bơ, cà phê, xác nhận xuất kho
```

---

## 🚀 Hướng Dẫn Vận Hành Nhanh

```bash
# Di chuyển vào thư mục dự án
cd /home/minh/30-cong-viec/12-dieu-phoi-goi-xe-krong-pak-krong-ana

# Khởi chạy hệ thống hoàn chỉnh (Backend Server + Web Client tại cổng 8088):
make run

# Hoặc mở trực tiếp file Web trên trình duyệt:
make open

# Chạy bộ kiểm thử tự động API:
make test

# Nghiệm thu cổng kiểm định chất lượng:
make gate
```

---

## 📦 Cấu Trúc Thư Mục Thực Địa

```text
├── 00-nguon/                 # Hồ sơ báo giá kỹ thuật Word DOCX, PDF và bảng phân rã WBS
├── 01-nghien-cuu/            # Báo cáo hội tụ mô hình Grab x TikTok Shop x Shopee
├── 02-giao-dien-prompts/     # Đặc tả giao diện 6 màn hình chi tiết (MD + JSON)
├── 03-web-app/               # Hệ thống ứng dụng thực thụ
│   ├── server.py             # Backend Server đa luồng (Python Stdlib HTTP + SQLite)
│   ├── dxp_production.db     # Cơ sở dữ liệu SQLite thật với dữ liệu Krông Pắk & Krông Ana
│   ├── static/               # Giao diện PWA hoàn chỉnh
│   │   ├── index.html        # Giao diện Single Page App (Leaflet Map + Audio Siren + VietQR)
│   │   ├── manifest.json     # PWA Manifest hỗ trợ cài đặt app trên điện thoại
│   │   ├── sw.js             # Service Worker lưu cache offline tốc độ cao
│   │   └── icons/            # Biểu tượng ứng dụng SVG
│   └── tests/
│       └── test_api.py       # Bộ 6 kiểm thử tự động toàn diện
├── 04-cong-kiem/
│   └── cong_kiem.py          # Script cổng kiểm định 17 tiêu chí kỹ thuật
├── Makefile                  # Lệnh điều khiển chuẩn hóa (gate, test, run, open)
├── README.md                 # Tài liệu kỹ thuật
└── STATUS.md                 # Bảng theo dõi tiến độ và số liệu nghiệm thu
```
