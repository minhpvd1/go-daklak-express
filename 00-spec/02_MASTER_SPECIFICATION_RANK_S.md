# 📐 ĐẶC TẢ KỸ THUẬT & SẢN PHẨM BẬC THẦY (MASTER SPECIFICATION — RANK S+)
## HỆ THỐNG ĐIỀU PHỐI VẬN TẢI & APP TÀI XẾ 2 HUYỆN (KRÔNG PẮK & KRÔNG ANA)
### DỰ ÁN: GO — ĐẮK LẮK EXPRESS (DXP PRODUCTION GRADE)

---

## 1. TỔNG QUAN HỆ THỐNG & METADATA SẢN PHẨM

| Thuộc tính | Định nghĩa kỹ thuật |
|---|---|
| **Tên sản phẩm** | **GO Driver Partner — Đắk Lắk Express (DXP)** |
| **Mã định danh** | `DXP-SYS-2026-KRONG-PAK-ANA` |
| **Phiên bản kiến trúc** | `v2.5.0-PROD-STABLE` |
| **Phạm vi địa lý trọng điểm** | Tuyến Huyện Krông Pắk (QL26) — Huyện Krông Ana (TL2) — TP. Buôn Ma Thuột |
| **Công nghệ Backend** | Python 3 Stdlib (`http.server`, `socketserver.ThreadingMixIn`, `sqlite3` thread-safe) |
| **Công nghệ Frontend** | PWA Single Page Application, Tailwind CSS Engine, Leaflet Maps, Web Audio API Synthesizer |
| **Cổng thanh toán & Ví** | VietQR Dynamic Generator (Napas 247) + Ledger ví điện tử tài xế |

---

## 2. CHÂN DUNG NGƯỜI DÙNG & MA TRẬN VAI TRÒ (USER PERSONAS)

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   HỆ THỐNG 4 VAI TRÒ ĐỒNG BỘ DXP                       │
├──────────────────┬─────────────────┬─────────────────┬────────────────┤
│ 1. KHÁCH HÀNG    │ 2. TÀI XẾ GO    │ 3. QUÁN ĂN / HTX│ 4. TỔNG ĐÀI    │
├──────────────────┼─────────────────┼─────────────────┼────────────────┤
│ Đặt xe đón tận   │ Nhận cuốc còi   │ Quản lý món ăn, │ Điều phối thủ  │
│ ngõ, chọn ghế    │ hú, xem lộ      │ xuất kho sầu    │ công, can thiệp│
│ ghép hoặc xe     │ trình, nhận     │ riêng, gọi ship │ khi có sự cố,  │
│ riêng, mua sầu   │ tiền mặt và ví  │ hỏa tốc tiện    │ nạp/rút tiền ví│
│ riêng & đồ ăn    │ Napas tức thì   │ chuyến          │ tổng đại lý    │
└──────────────────┴─────────────────┴─────────────────┴────────────────┘
```

### Danh Sách Tài Xế Điển Hình Thực Địa:
1. **Tài xế Ba Cường (ID: 1):** Xe Xpander 7 chỗ, Biển số: `47A-528.39`. Tuyến chính: TT. Phước An, Ea Yông ⇄ BV Vùng Tây Nguyên & BMT.
2. **Tài xế Bảy Nam (ID: 2):** Xe Vios 4 chỗ, Biển số: `47A-481.12`. Tuyến chính: TT. Buôn Trấp, Dray Sáp ⇄ Ngã 6 BMT & ĐH Tây Nguyên.
3. **Tài xế Văn Tuấn (ID: 3):** Xe máy Wave RSX, Biển số: `47B1-892.44`. Giao đồ ăn KFC, bún riêu, bưu kiện hỏa tốc nội ô và liên huyện.

---

## 3. CƠ SỞ DỮ LIỆU & SCHEMA THỰC ĐỊA (SQLITE THREAD-SAFE)

```sql
-- 1. Bảng người dùng
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL, -- 'customer', 'driver', 'seller', 'dispatcher'
    full_name TEXT NOT NULL,
    phone TEXT UNIQUE NOT NULL,
    district TEXT,
    balance REAL DEFAULT 0,
    rating REAL DEFAULT 5.0,
    avatar TEXT,
    created_at TEXT NOT NULL
);

-- 2. Bảng tài xế đối tác
CREATE TABLE drivers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    vehicle_type TEXT NOT NULL, -- 'car_7', 'car_4', 'bike'
    license_plate TEXT NOT NULL,
    lat REAL NOT NULL,
    lng REAL NOT NULL,
    is_online INTEGER DEFAULT 1,
    is_busy INTEGER DEFAULT 0,
    completed_trips INTEGER DEFAULT 0,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

-- 3. Bảng cuốc xe chở khách
CREATE TABLE rides (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    customer_phone TEXT NOT NULL,
    origin_name TEXT NOT NULL,
    origin_lat REAL,
    origin_lng REAL,
    destination_name TEXT NOT NULL,
    destination_lat REAL,
    destination_lng REAL,
    ride_type TEXT DEFAULT 'carpool', -- 'carpool', 'private'
    seats INTEGER DEFAULT 1,
    distance_km REAL,
    price REAL NOT NULL,
    driver_id INTEGER,
    status TEXT DEFAULT 'PENDING', -- 'PENDING', 'IN_TRANSIT', 'COMPLETED', 'CANCELLED'
    notes TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY(driver_id) REFERENCES drivers(id)
);

-- 4. Bảng đơn hàng giao nông sản & ẩm thực
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_code TEXT UNIQUE NOT NULL,
    customer_name TEXT NOT NULL,
    customer_phone TEXT NOT NULL,
    delivery_address TEXT NOT NULL,
    district TEXT NOT NULL,
    total_amount REAL NOT NULL,
    shipping_fee REAL DEFAULT 15000,
    payment_method TEXT DEFAULT 'VIETQR', -- 'VIETQR', 'COD'
    payment_status TEXT DEFAULT 'UNPAID', -- 'UNPAID', 'PAID'
    order_status TEXT DEFAULT 'PENDING',  -- 'PENDING', 'CONFIRMED', 'DELIVERING', 'COMPLETED'
    qr_payload TEXT,
    assigned_driver_id INTEGER,
    created_at TEXT NOT NULL
);

-- 5. Bảng lịch sử ví điện tử (Ledger)
CREATE TABLE wallet_transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    type TEXT NOT NULL, -- 'TRIP_EARNING', 'PLATFORM_FEE', 'WITHDRAW', 'TOPUP'
    amount REAL NOT NULL,
    balance_after REAL NOT NULL,
    reference_id TEXT,
    notes TEXT,
    created_at TEXT NOT NULL
);
```

---

## 4. QUY CHUẨN GIAO THỨC API (RESTFUL CONTRACT)

| Phương thức | Đường dẫn API | Mô tả chức năng | Mã phản hồi |
|---|---|---|:---:|
| `GET` | `/api/health` | Kiểm tra tình trạng sống của máy chủ và DB | `200 OK` |
| `GET` | `/api/bootstrap` | Nạp dữ liệu khởi tạo (Tài xế, Cửa hàng, Sản phẩm) | `200 OK` |
| `GET` | `/api/rides` | Lấy danh sách chuyến xe (Bộ lọc trạng thái & tài xế) | `200 OK` |
| `POST` | `/api/rides` | Khách tạo cuốc xe mới | `201 Created` |
| `POST` | `/api/rides/simulate` | Mô phỏng nổ cuốc xe tự động cho 2 huyện (Test Siren) | `201 Created` |
| `POST` | `/api/rides/{id}/accept` | Tài xế nhận cuốc (Row Lock bảo vệ) | `200 OK` / `400` |
| `POST` | `/api/rides/{id}/complete` | Hoàn thành cuốc xe (Trích 16% phí, cộng 84% vào ví) | `200 OK` |
| `POST` | `/api/drivers/{id}/toggle-online` | Bật/tắt trạng thái nhận cuốc của tài xế | `200 OK` |
| `POST` | `/api/orders` | Tạo đơn hàng ẩm thực / nông sản kèm VietQR | `201 Created` |
| `POST` | `/api/orders/{id}/confirm` | Quán ăn hoặc tài xế xác nhận giao hàng xong | `200 OK` |
| `POST` | `/api/wallet/withdraw` | Tài xế gửi lệnh rút tiền về Napas 247 | `200 OK` |

---

## 5. CÔNG THỨC TOÁN HỌC & ĐỊNH GIÁ CƯỚC (DYNAMIC PRICING ENGINE)

### 5.1. Khoảng cách địa lý Haversine
$$d = 2R \cdot \arcsin\left(\sqrt{\sin^2\left(\frac{\Delta \phi}{2}\right) + \cos(\phi_1)\cos(\phi_2)\sin^2\left(\frac{\Delta \lambda}{2}\right)}\right)$$
*Trong đó: $R = 6371\text{ km}$, $\phi_1, \phi_2$ là vĩ độ, $\lambda_1, \lambda_2$ là kinh độ.*

### 5.2. Công thức tính cước khách hàng & Thu nhập tài xế
- **Cước khách ghép tiện chuyến:**
  $$\text{Price}_{\text{carpool}} = \max\left(40.000, \, 15.000 + 1.200 \times d\right) \times \text{Seats}$$
- **Tiền ròng tài xế thực nhận (Net Earning):**
  $$\text{NetPayout} = \text{Price} \times (1 - 0.16) = \text{Price} \times 0.84$$
- **Phí sàn vận hành DXP (Platform Fee):**
  $$\text{Fee}_{\text{DXP}} = \text{Price} \times 0.16$$

---

## 6. QUY CHUẨN THIẾT KẾ UI/UX (DESIGN TOKENS CHO MOBILE TELEMATICS)

- **Màu sắc chủ đạo:**
  - `GO Red`: `#E11D48` (Màu thương hiệu GO - Đi đâu cũng GO).
  - `Online Emerald`: `#10B981` (Tài xế sẵn sàng nhận cuốc).
  - `Dark Slate Background`: `#070A12` (Màu nền chống chói khi lái xe ngoài nắng).
  - `Card Surface`: `#0F172A` (Nền thẻ thông tin tương phản cao).
  - `Text Primary`: `#FFFFFF`, `Text Muted`: `#94A3B8`.
- **Âm thanh cảnh báo (Web Audio API Synthesizer):**
  - Tần số cơ bản: Dao động sóng Sawtooth $750\text{ Hz} \leftrightarrow 960\text{ Hz}$.
  - Nhịp chuông: $220\text{ ms}$ đổi nhịp.
  - Phản hồi rung haptic: `[250ms, 100ms, 250ms, 100ms, 400ms]`.
- **Navigation:**
  - 5 Tab dưới đáy: Trực Tuyến (Radar), Đơn Giao, Ví Tiền, Cá Nhân.
  - Tương thích 100% PWA (Add to Home Screen trên iOS Safari và Android Chrome).

---

## 7. ĐỊNH NGHĨA HOÀN THÀNH (DEFINITION OF DONE - DOD)
- Mã nguồn độc lập, sạch sẽ, không có thư viện bên ngoài nặng nề.
- 100% chạy mượt trên cổng mặc định `8088`.
- Exit code kiểm thử và kiểm định: `rc=0`.
- Không tạo file rác trong workspace.

