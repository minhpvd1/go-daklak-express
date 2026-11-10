---
name: GO Real-World Design System (100% White Light Theme Dominant)
colors:
  # Primary Brand Red
  primary: '#F9372D'
  primary-hover: '#D32F2F'
  primary-light: '#FFF1F0'
  on-primary: '#FFFFFF'
  
  # White Theme Dominant Colors (Chủ đạo chính theo chỉ thị của Hoàng Minh)
  bg-canvas: '#FFFFFF'
  bg-subtle: '#F8F9FA'
  bg-muted: '#F2F4F7'
  surface-card: '#FFFFFF'
  surface-card-hover: '#F9FAFB'
  border-subtle: '#E5E7EB'
  border-strong: '#D1D5DB'
  
  # Typography on White
  text-primary: '#111827'
  text-secondary: '#4B5563'
  text-muted: '#6B7280'
  text-light: '#9CA3AF'
  
  # Interactive Accents
  pill-inactive-bg: '#F3F4F6'
  pill-inactive-text: '#374151'
  pill-active-bg: '#F9372D'
  pill-active-text: '#FFFFFF'
  
  # Telematics & Status
  online-green: '#10B981'
  online-green-light: '#ECFDF5'
  badge-discount-red: '#EF4444'
  star-yellow: '#F59E0B'
typography:
  display:
    fontFamily: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Plus Jakarta Sans", sans-serif
    fontSize: 24px
    fontWeight: '800'
    lineHeight: 28px
  title-1:
    fontFamily: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Plus Jakarta Sans", sans-serif
    fontSize: 18px
    fontWeight: '700'
    lineHeight: 24px
  title-2:
    fontFamily: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Plus Jakarta Sans", sans-serif
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 22px
  body:
    fontFamily: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Plus Jakarta Sans", sans-serif
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
  caption:
    fontFamily: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Plus Jakarta Sans", sans-serif
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 14px
rounded:
  pill: 9999px
  card: 16px
  sheet: 24px
  sm: 8px
---

# Quy Chuẩn Thiết Kế GO — Nền Trắng Sáng Chủ Đạo (White Light Theme Dominant)

> **Chỉ thị trực tiếp từ Hoàng Minh (HM):**  
> *"Theme màu trắng là chủ đạo chính đi em"*  
> Toàn bộ hệ thống giao diện GO (Trang Chủ, Đặt Xe, Giao Hàng, Đồ Ăn, Cửa Hàng KFC, Chi Tiết Món Ăn, và App Tài Xế) chuyển đổi đồng bộ sang **Nền Trắng Tinh Khiết Hiện Đại** (`#FFFFFF` kết hợp `#F8F9FA` và viền `#E5E7EB`), điểm xuyết sắc đỏ thương hiệu rực rỡ (`#F9372D`), loại bỏ triệt để mọi phong cách AI giả tạo.

---

## 1. Nguyên Tắc Cốt Lõi
- **Màu trắng là chủ đạo tuyệt đối:** Canvas nền `#FFFFFF`, khối thẻ card `#FFFFFF` đổ bóng nhẹ tự nhiên (`shadow-sm`) hoặc nền xám siêu nhẹ `#F8F9FA`.
- **Tương phản chuẩn công thái học:** Chữ đen đậm `#111827`, mô tả xám trung tính `#4B5563`, phụ chú `#6B7280`. Dễ đọc dưới ánh sáng ban ngày.
- **Màu đỏ GO làm điểm nhấn hành động:** Nút bấm CTA chính, badge giảm giá, tab active, trạng thái đã chọn đều dùng `#F9372D`.
- **Tuyệt đối không AI ảo giác:** Không dùng gradient tím xanh mờ ảo, không dùng hình clip-art giả tạo. 100% sử dụng hình ảnh thật đã cắt từ ảnh thực chứng.

---

## 2. Hệ Thống 7 Màn Hình Chuẩn Nền Trắng
1. **01_screen_home_discovery.html:** Nền trắng sáng `#FAFAFA`, logo GO đỏ, 4 pill dịch vụ (Tất cả đỏ, Đặt xe, Giao hàng, Đặt đồ ăn), lưới 2 cột ảnh thật.
2. **02_screen_ride_hailing.html:** Bản đồ trên sáng rõ, bottom sheet trắng tròn `#FFFFFF`, 3 thẻ xe ngang (Xe máy viền đỏ nền `#FFF1F0`), giá 12k–18k, nút đỏ "Đặt xe".
3. **03_screen_delivery.html:** Bản đồ giao hàng, thẻ người gửi - người nhận trắng viền mảnh, lưới 2x2 thông số kiện hàng, công tắc COD đỏ ON, giá 35.000đ.
4. **04_screen_food_discovery.html:** Chuyển sang Nền Trắng `#FFFFFF`, header chữ đen `GO | Đồ ăn`, thanh tìm kiếm `#F3F4F6`, 5 pill danh mục sáng, banner KFC 50%, lưới 6 món ăn thẻ trắng bo góc thanh lịch.
5. **05_screen_kfc_store.html:** Chuyển sang Nền Trắng `#FFFFFF`, avatar KFC tròn viền đỏ, stats chữ đen, nút Theo dõi đỏ `#F9372D`, nút Nhắn tin nền xám nhẹ `#F3F4F6`, 5 highlight tròn trên nền trắng, lưới bài viết chia ranh giới trắng tinh sạch.
6. **06_screen_kfc_food_detail.html:** Chuyển sang Nền Trắng `#FFFFFF`, xô gà KFC trên nền trắng sang trọng, tiêu đề chữ đen `#111827`, giá 45.000đ đỏ nổi bật, nút chọn size thẻ trắng viền đỏ, thanh thêm vào giỏ trắng tinh viền mảnh.
7. **07_screen_driver_console.html:** Chuyển sang Nền Trắng / Xám Bạc Hiện Đại (`#F8F9FA` / `#FFFFFF`), thẻ tài xế Ba Cường viền ngọc lục bảo, thẻ doanh thu trắng tinh, thẻ cuốc xe mới viền đỏ tương phản cao, nút "NHẬN CUỐC" đỏ rực.
