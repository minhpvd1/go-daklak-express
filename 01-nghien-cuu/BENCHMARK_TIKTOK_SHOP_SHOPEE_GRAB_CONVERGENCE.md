# BÁO CÁO NGHIÊN CỨU & ĐỐI CHIẾU TRẢI NGHIỆM NGƯỜI DÙNG (BENCHMARKING UX/UI)
## MÔ HÌNH HỘI TỤ ĐA NỀN TẢNG: GRAB × SHOPEEFOOD × TIKTOK
**Ứng dụng thực tế cho:** Nền tảng Điều phối Đi Lại Nơi Chốn & Ẩm Thực Quán Xá Krông Pắk – Krông Ana – TP. Buôn Ma Thuột  
**Mã tài liệu:** `RES-UXUI-DKL-2026` | **Tiêu chuẩn:** Kỹ sư Giải pháp & Phần mềm Thực địa

---

## I. BỐI CẢNH ĐẶC THÙ ĐI LẠI & QUÁN ĂN ĐỊA PHƯƠNG TẠI ĐẮK LẮK

1. **Nhu cầu đi lại giữa các nơi chốn địa phương:**
   - Bà con và người dân 2 huyện Krông Pắk & Krông Ana di chuyển liên tục giữa các địa điểm trọng yếu:
     - *TT. Phước An (Krông Pắk):* Cổng Chợ Phước An, Trung tâm Y tế Huyện, Phố ẩm thực Giải Phóng, Phố cà phê Km 19 Ea Knuèc.
     - *TT. Buôn Trấp (Krông Ana):* Bến xe Buôn Trấp, Chợ Trung tâm, Ngã 3 Buôn Trấp (phố ăn đêm), Khu du lịch Thác Dray Sáp / Gia Long.
     - *TP. Buôn Ma Thuột:* Ngã 6 Trung tâm, Bến xe Liên tỉnh (Km 4), Bệnh viện Đa khoa Vùng Tây Nguyên, Trường Đại học Tây Nguyên.
   - Thói quen gọi xe trước đây chủ yếu qua số điện thoại quen hoặc các nhóm Zalo/Facebook tự phát. Khách cần một nền tảng chuyên nghiệp: ghim nơi chốn đón/trả, thấy rõ giá cước cố định (không bị ép giá), theo dõi vị trí xe đón, có lựa chọn Xe Ghép Tiện Chuyến, Xe Ôm Hỏa Tốc hoặc Bao Xe Gia Đình.

2. **Nhu cầu đặt món ăn nóng hổi từ quán xá địa phương (ShopeeFood / GrabFood):**
   - Các quán ăn ngon, quán bún đỏ, bún chìa, phở khô hai tô, cơm tấm sườn nướng, tiệm trà sữa, cà phê rang xay, quán ăn vặt tại thị trấn Phước An và Buôn Trấp có lượng khách ăn tại chỗ và mua mang về rất lớn.
   - Trước đây người dân muốn ăn phải tự chạy xe ra quán hoặc nhờ người quen mua hộ. Các nền tảng giao đồ ăn lớn chưa phủ sóng sâu về các huyện.
   - **Mô hình kết hợp:** Tài xế xe máy và xe tiện chuyến địa phương vừa chở khách vừa nhận giao đồ ăn hỏa tốc từ các quán xá về tận nhà cho khách trong bán kính huyện chỉ mất **15 - 25 phút** với cước ship cố định 15.000đ - 20.000đ.

3. **Xu hướng Review quán ăn & nơi chốn qua Video Ngắn (TikTok Style):**
   - Giới trẻ và thực khách có thói quen xem video ngắn review tô bún đỏ bốc khói, dĩa cơm tấm nướng than hoa, ly trà sữa full topping, view quán cà phê chill.
   - Tích hợp tính năng thẻ vàng (Yellow Anchor): Đang xem video review quán nào có thể bấm ngay nút **"Đặt món quán này"** hoặc **"Đặt xe tới quán này ngay"**.

---

## II. MA TRẬN ĐỐI CHIẾU 4 NỀN TẢNG TINH HOA

| Yếu tố UX/UI | GRAB (Định vị & Đi lại) | SHOPEEFOOD (Gọi món quán) | TIKTOK (Khám phá video) | ĐẮK LẮK EXPRESS (DXP THỰC TẾ) |
|:---|:---|:---|:---|:---|
| **Màn hình chính (Home)** | Bản đồ vệ tinh, thanh tìm kiếm điểm đón/trả. | Danh mục quán ăn, món hot, flash sale đồ ăn. | Feed video ngắn ẩm thực & du lịch. | **Bản đồ Đi Lại Nơi Chốn kết hợp Menu Quán Ăn & Video Review Quán.** |
| **Trang Quán Ăn (Merchant)** | Hồ sơ quán ăn đơn giản. | Menu món ăn đầy đủ: Hình ảnh, giá, topping, ghi chú bếp. | Trang kênh quán ăn kèm video review món. | **Kênh Chủ Quán Ăn: Quản lý thực đơn, bật/tắt món còn/hết, nhận đơn làm món tức thì.** |
| **Quy trình Đặt cuốc / Đặt món** | Ghim điểm đón ➔ Chọn xe ➔ Đi ngay. | Chọn món ➔ Chọn địa chỉ giao ➔ Ship tận nơi. | Xem video ➔ Bấm giỏ hàng vàng ➔ Chốt đơn. | **2 Chạm Đặt Xe + Giỏ Hàng Đồ Ăn 15k Ship Hỏa Tốc (20-30 phút tới nơi).** |
| **Thanh toán & Ví** | Thẻ / Tiền mặt / GrabPay. | ShopeePay / COD. | Chuyển khoản / COD. | **Mã VietQR Napas 247 tự động nhận diện đơn + Tiền mặt trực tiếp cho tài xế.** |
| **Console Điều phối** | App Driver riêng biệt. | App ShopeeFood Merchant. | TikTok Studio. | **Bàn Tổng Đài Điều Phối & Multi-Role Console 4 trong 1 (Khách, Tài xế, Quán ăn, Tổng đài).** |

---

## III. 5 MÀN HÌNH CỐT LÕI VẬN HÀNH THỰC TẾ

1. **MÀN HÌNH 1: ĐI LẠI GIỮA CÁC NƠI CHỐN (GRAB STYLE CORE)**
   - Chọn nhanh các nơi chốn trọng điểm: *Chợ Phước An, Ngã 3 Buôn Trấp, BV Vùng Tây Nguyên, Ngã 6 BMT, Bến Xe*.
   - 3 Chế độ dịch vụ:
     - 🚗 **Xe Ghép Tiện Chuyến (35k - 50k/ghế)**: Đi lại liên huyện tiết kiệm.
     - 🚐 **Bao Xe 4-7 Chỗ (180k - 250k/chuyến)**: Đi gia đình, khám bệnh, sân bay.
     - 🛵 **Xe Ôm / Giao Hàng Hỏa Tốc (15k - 30k)**: Đón nhanh trong 5 phút.
   - Bản đồ Leaflet vẽ lộ trình trực tiếp, hiển thị vị trí tài xế và khoảng cách.

2. **MÀN HÌNH 2: QUÁN ĂN & MÓN NGON ĐỊA PHƯƠNG (SHOPEEFOOD)**
   - Phân loại món ăn nóng hổi:
     - 🍲 Bún Đỏ Đắk Lắk, Phở Khô Hai Tô, Bún Chìa Bắp Bò.
     - 🍛 Cơm Tấm Sườn Nướng, Cơm Gà Xối Mỡ, Bánh Mì Xíu Mại Sốt Cay.
     - 🧋 Trà Sữa Trân Châu Đường Đen, Cà Phê Mộc Pha Phin Đậm Vị.
     - 🍢 Mẹt Ăn Vặt, Bánh Ướt Thịt Nướng, Lẩu Bò Nhúng Cay.
   - Thêm món vào giỏ, chọn số lượng, ghi chú cho quán (ít đường, không hành, cay nhiều).

3. **MÀN HÌNH 3: VIDEO REVIEW QUÁN & NƠI CHỐN (TIKTOK FEED)**
   - Video review ngắn không gian quán, quy trình nấu tô bún đỏ, nướng sườn than hoa.
   - Thẻ sản phẩm màu vàng nổi bật kèm 2 nút hành động: "Đặt Món Quán Này" hoặc "Đặt Xe Tới Quán".

4. **MÀN HÌNH 4: TÀI XẾ ĐỐI TÁC (CHỞ KHÁCH & GIAO MÓN ĂN)**
   - Còi hú điều phối vang lên khi có khách đặt cuốc đi lại hoặc quán ăn nổ đơn cần ship.
   - Quản lý ví thu nhập, khấu trừ 16% chiết khấu sàn, rút tiền tức thì qua VietQR Napas.

5. **MÀN HÌNH 5: KÊNH CHỦ QUÁN ĂN (RESTAURANT CENTER)**
   - Nhận đơn món ăn từ khách $\rightarrow$ Bấm xác nhận bếp đang nấu $\rightarrow$ Bàn giao cho tài xế giao tới nhà.
   - Quản lý danh mục thực đơn của quán, tự thêm món mới kèm giá bán.
