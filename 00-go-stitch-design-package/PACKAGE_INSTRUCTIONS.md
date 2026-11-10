# 📦 HƯỚNG DẪN SỬ DỤNG GÓI THIẾT KẾ CHO GOOGLE STITCH
## DỰ ÁN: "GO — ĐI ĐÂU CŨNG GO" (SUPER APP & DRIVER)

---

## 🗂️ 1. CẤU TRÚC GÓI ĐÓNG GÓI (PACKAGE STRUCTURE)

```text
00-go-stitch-design-package/
├── design.md                          # Hệ thống Design System chuẩn Google Stitch (Màu, Font, Layout)
├── MASTER_STITCH_PROMPTS.md           # Bộ Prompt Tiếng Việt chi tiết kèm link 6 ảnh thực tế
├── MASTER_PROMPTS_ENGLISH_FOR_STITCH.md # Bộ Prompt Tiếng Anh chuẩn hóa tối ưu cho AI Stitch
├── PACKAGE_INSTRUCTIONS.md            # Tài liệu hướng dẫn sử dụng nhanh này
└── images/                            # Toàn bộ 6 bức ảnh gốc anh Minh cung cấp
    ├── 01_go_home_discovery.jpg       # Trang chủ tổng hợp GO
    ├── 02_go_ride_hailing_map.jpg     # Màn hình đặt xe bản đồ BMT - Krông Pắk
    ├── 03_go_delivery_logistics.jpg   # Màn hình giao hàng COD
    ├── 04_go_food_discovery_dark.jpg  # Màn hình đồ ăn Dark Theme
    ├── 05_go_kfc_restaurant_store.jpg # Màn hình trang quán KFC Vietnam
    └── 06_go_kfc_food_item_detail.jpg # Màn hình chi tiết món gà rán & topping
```

---

## 🚀 2. CÁCH ĐƯA LÊN GOOGLE STITCH (https://stitch.withgoogle.com)

### Cách 1: Thiết kế trực tiếp trên Google Stitch Web
1. Truy cập: [https://stitch.withgoogle.com](https://stitch.withgoogle.com)
2. Bấm nút **"Create Project"** $\rightarrow$ Đặt tên: `GO — Super App & Driver Partner`.
3. Nhập Design System:
   - Mở file [`design.md`](file:///home/minh/30-cong-viec/12-dieu-phoi-goi-xe-krong-pak-krong-ana/00-go-stitch-design-package/design.md), copy toàn bộ nội dung dán vào mục Design MD của dự án.
4. Sinh từng màn hình (Generate Screen):
   - Mở file [`MASTER_PROMPTS_ENGLISH_FOR_STITCH.md`](file:///home/minh/30-cong-viec/12-dieu-phoi-goi-xe-krong-pak-krong-ana/00-go-stitch-design-package/MASTER_PROMPTS_ENGLISH_FOR_STITCH.md).
   - Copy đoạn prompt của màn hình cần tạo (Screen 1 đến Screen 7).
   - Tải kèm ảnh đối chiếu tương ứng trong thư mục `images/` vào ô upload của Stitch.
   - Bấm **Generate** $\rightarrow$ Google Stitch sẽ render ra giao diện UI/UX hoàn chỉnh chuẩn 100%!

---

## 💾 3. FILE NÉN BÀN GIAO (ZIP FILE)
Toàn bộ gói đã được nén thành file duy nhất để anh Minh dễ dàng chia sẻ hoặc lưu trữ:
- **Đường dẫn file nén:**  
  `/home/minh/30-cong-viec/12-dieu-phoi-goi-xe-krong-pak-krong-ana/GO_STITCH_UIUX_PACKAGE.zip`

