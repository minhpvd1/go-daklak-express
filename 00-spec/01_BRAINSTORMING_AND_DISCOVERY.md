# 🧠 BẢN BRAINSTORMING & KHẢO SÁT THỰC ĐỊA BẬC THẦY (DISCOVERY & BRAINSTORMING)
## HỆ THỐNG ĐIỀU PHỐI GỌI XE & APP TÀI XẾ 2 HUYỆN: KRÔNG PẮK — KRÔNG ANA
### THƯƠNG HIỆU: GO ("ĐI ĐÂU CŨNG GO") — ĐẮK LẮK EXPRESS (DXP)

---

## 1. BỐI CẢNH ĐỊA LÝ & NỖI ĐAU THỰC ĐỊA (PAIN POINTS)

### 1.1. Thực Trạng Giao Thông Tuyến Krông Pắk — Krông Ana — Buôn Ma Thuột
- **Tuyến 1: Huyện Krông Pắk ⇄ TP. Buôn Ma Thuột (~28 - 35 km dọc QL26)**
  - Các điểm tập trung dân cư: TT. Phước An, Xã Ea Yông, Ea Kly, Ea Phê, Hòa An, Hòa Đông.
  - Điểm đến trọng điểm tại BMT: Bệnh Viện Đa Khoa Vùng Tây Nguyên (đường Mai Hắc Đế), Trường Đại Học Tây Nguyên (đường Lê Duẩn), Chợ Trung Tâm BMT, Bến Xe Phía Nam.
  - Vấn đề: Xe buýt tuyến 04 chạy theo khung giờ cứng nhắc, dừng đỗ nhiều trạm mất hơn 1 tiếng rưỡi; Taxi truyền thống 1 chiều tốn từ 280.000đ - 350.000đ (quá đắt cho bà con đi khám bệnh định kỳ); Xe máy cá nhân đi đường quốc lộ bụi đỏ, mùa mưa trơn trượt nguy hiểm.
- **Tuyến 2: Huyện Krông Ana ⇄ TP. Buôn Ma Thuột (~22 - 28 km dọc Tỉnh lộ 2)**
  - Các điểm tập trung: TT. Buôn Trấp, Dray Sáp, Quảng Điền, Bình Hòa, Ea Na, Ea Bông.
  - Vấn đề: Nhu cầu buôn bán nông sản, cán bộ huyện đi công vụ, bệnh nhân và học sinh sinh viên rất lớn nhưng xe dù bến cóc không có giờ đón chuẩn xác, tài xế phải ngồi quán cà phê đợi khách hoặc đăng Facebook gom nhóm thủ công rất mất thời gian.
- **Tuyến 3: Nhu cầu kết hợp cốp xe rỗng giao hàng & đồ ăn**
  - Xe ô tô 4-7 chỗ chạy từ Krông Pắk/Krông Ana về BMT hoặc ngược lại thường còn trống cốp xe và 2-3 ghế ngồi.
  - Nhu cầu gửi sầu riêng tươi, bơ booth, cà phê bột, gà ta từ huyện lên phố; hoặc ship đồ ăn nhanh KFC, đồ ăn vặt từ TP về huyện rất cao nhưng chưa có nền tảng tự động kết nối.

---

## 2. NỘI HÓA BẢN SẮC 5 MÀN HÌNH MẪU THƯƠNG HIỆU GO

Từ 5 bức ảnh chụp màn hình thực tế do anh Minh cung cấp:
1. **Logo & Bản sắc nhận diện:** Chữ "GO" đỏ bo tròn năng động (`#E11D48`), slogan *"Đi đâu cũng GO — Nhanh chóng · An toàn · Tiện lợi"*.
2. **Hệ 3 Dịch Vụ Cốt Lõi:**
   - **Đặt xe (Go Ride):** Xe máy (từ 12.000đ), Ô tô 4 chỗ (từ 59.000đ), Ô tô 7 chỗ (từ 79.000đ), Xe tiện chuyến ghép ghế (từ 40.000đ - 50.000đ).
   - **Giao hàng (Go Delivery):** Hàng tiêu dùng, nông sản địa phương, bưu kiện dưới 5kg, tùy chọn COD thu hộ tiền mặt linh hoạt.
   - **Đặt đồ ăn (Go Food):** Tích hợp chuỗi thương hiệu lớn (KFC Vietnam, Mì cay Samyang, Khoai tây chiên) cùng các quán ăn đặc sản địa phương (Cơm tấm Buôn Trấp, Quán Cô Ba Phước An).
3. **App Tài Xế GO Chuyên Dụng (Go Driver Partner):**
   - Thiết kế giao diện **Dark Slate High-Contrast** (`#070A12` / `#0F172A`) chống chói mắt tuyệt đối dưới ánh nắng gay gắt Tây Nguyên khi tài xế gắn điện thoại trên giá đỡ xe máy hoặc taplo ô tô.
   - Nút nhận cuốc to bản (Toàn chiều ngang) bấm chuẩn xác ngay cả khi đang đeo găng tay.
   - Âm còi hú điều phối (Dispatch Siren) tần số dao động 750Hz - 950Hz từ Web Audio API kêu vang rõ rệt, kết hợp rung Haptic phản hồi.

---

## 3. PHÂN TÍCH MA TRẬN TÍNH NĂNG (MOSCOW MATRIX)

| Mức Độ | Tính Năng Cụ Thể | Lý Do Quyết Định |
|---|---|---|
| **MUST-HAVE** (Bắt buộc phải có) | - Đặt xe chở khách & ghép chuyến 2 huyện.<br>- Còi hú nổ cuốc Web Audio API không phụ thuộc file mạng.<br>- Nhận cuốc độc quyền trên SQLite đa luồng (tránh tranh chấp 2 tài xế).<br>- Bản đồ Leaflet OpenStreetMap định vị Krông Pắk, Krông Ana, BMT.<br>- Tự động tính cước, trích 16% phí sàn DXP, cộng 84% tiền ròng vào ví tài xế.<br>- Ví Napas 247 rút tiền tức thì. | Vận hành cốt lõi của nền tảng gọi xe thực thụ. |
| **SHOULD-HAVE** (Nên có ngay) | - Nút mô phỏng nổ cuốc nhanh (Simulate Dispatch) phục vụ kiểm thử và demo.<br>- Bộ lọc theo khu vực (Krông Pắk, Krông Ana, BMT).<br>- Tab giao đồ ăn và bưu kiện tiện chuyến.<br>- PWA Manifest và Service Worker hỗ trợ cài app lên màn hình điện thoại. | Tối ưu trải nghiệm sử dụng thực địa cho tài xế. |
| **COULD-HAVE** (Mở rộng giai đoạn 2) | - Chat trực tiếp tài xế - khách hàng qua WebSocket.<br>- Báo cáo cuốc xe theo tuần/tháng xuất file Excel.<br>- Tích hợp AI phân tích cung đường ngắn nhất tránh điểm kẹt xe. | Gia tăng tiện ích bổ trợ. |
| **WON'T-HAVE** (Loại bỏ triệt để) | - Quảng cáo rác bên thứ ba.<br>- Thủ tục đăng ký rườm rà bắt nạp tiền trước.<br>- Thiết kế theme sáng chói gây lóa mắt nguy hiểm cho tài xế. | Giữ app siêu nhẹ, an toàn khi lái xe. |

---

## 4. BẢN ĐỒ STATE MACHINE (VÒNG ĐỜI CUỐC XE & ĐƠN HÀNG)

```text
[KHÁCH HÀNG ĐẶT XE / TỔNG ĐÀI ĐIỀU PHỐI]
               │
               ▼
       [TRẠNG THÁI: PENDING] ──▶ Lưu SQLite thread-safe
               │
      Bắn radar quét bán kính 30km
               │
               ▼
[TÀI XẾ GO NHẬN TÍN HIỆU CÒI HÚ SIREN + ĐẾM NGƯỢC 15S]
       ├── Bỏ qua / Hết giờ ──▶ Chuyển cuốc cho tài xế kế tiếp
       └── Bấm 'NHẬN CUỐC NGAY'
               │
               ▼
     [TRẠNG THÁI: IN_TRANSIT] ──▶ Khóa hàng độc quyền (Row Lock)
               │
       Tài xế đón khách, chạy lộ trình
               │
               ▼
  [TÀI XẾ BẤM 'HOÀN THÀNH CUỐC XE']
               │
               ▼
     [TRẠNG THÁI: COMPLETED]
               │
               ├── Tự động trích 16% phí duy trì hệ thống
               ├── Cộng 84% tiền cước ròng vào ví tài xế
               └── Ghi nhận lịch sử giao dịch ví (Ledger)
```

