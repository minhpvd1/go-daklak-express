#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chụp ảnh màn hình Ultra HD 2K Retina toàn bộ 16 màn hình siêu ứng dụng GO
(Đắk Lắk Express - Krông Pắk & Krông Ana) bằng Google Chrome Headless.
Đóng gói trọn bộ vào ZIP để tải lên Google AI Studio tạo full-stack web.
"""

import os
import sys
import subprocess
import shutil
import zipfile

BASE_DIR = "/home/minh/30-cong-viec/12-dieu-phoi-goi-xe-krong-pak-krong-ana"
OUTPUT_DIR = os.path.join(BASE_DIR, "GO_FULL_SCREENS_GOOGLE_STUDIO")
ZIP_DEST = os.path.join(BASE_DIR, "GO_FULLSTACK_SCREENS_GOOGLE_STUDIO.zip")

SCREENS = [
    ("01_screen_home_discovery.html", "01_Trang_Chu_Kham_Pha_Home_Discovery.png", 430, 932),
    ("02_screen_ride_hailing.html", "02_Dat_Xe_Tien_Chuyen_Ride_Hailing.png", 430, 932),
    ("03_screen_delivery.html", "03_Giao_Hang_Nong_San_Hoa_Toc_Delivery.png", 430, 932),
    ("04_screen_food_discovery.html", "04_Kham_Pha_Am_Thuc_Food_Discovery.png", 430, 932),
    ("05_screen_kfc_store.html", "05_Ho_So_Cua_Hang_Quan_An_KFC_Store.png", 430, 932),
    ("06_screen_kfc_food_detail.html", "06_Chi_Tiet_Mon_An_Food_Detail.png", 430, 932),
    ("07_screen_driver_console.html", "07_App_Tai_Xe_Console_Radar_Dieu_Phoi.png", 430, 932),
    ("08_screen_cart_checkout.html", "08_Gio_Hang_Thanh_Toan_Napas_Checkout.png", 430, 932),
    ("09_screen_live_tracking.html", "09_Theo_Doi_Lo_Trinh_Realtime_Tracking.png", 430, 932),
    ("10_screen_order_history.html", "10_Lich_Su_Cuoc_Xe_Don_Hang_History.png", 430, 932),
    ("11_screen_voucher_promotions.html", "11_Kho_Uu_Dai_Voucher_Promotions.png", 430, 932),
    ("12_screen_user_wallet_profile.html", "12_Ca_Nhan_Vi_GO_User_Profile.png", 430, 932),
    ("13_screen_driver_trip_navigation.html", "13_App_Tai_Xe_Dan_Duong_HUD_Navigation.png", 430, 932),
    ("14_screen_driver_wallet_withdrawal.html", "14_App_Tai_Xe_Vi_Thu_Nhap_Rut_Tien_Napas.png", 430, 932),
    ("15_screen_driver_registration.html", "15_App_Tai_Xe_Dang_Ky_Ho_So_Onboarding.png", 430, 932),
    ("16_screen_dispatch_admin_dashboard.html", "16_Trung_Tam_Dieu_Phoi_Admin_Dashboard.png", 1280, 800)
]

os.makedirs(OUTPUT_DIR, exist_ok=True)
print("=== BẮT ĐẦU CHỤP FULL RETINA SCREENSHOTS CHO GOOGLE STUDIO ===")

for filename, out_name, w, h in SCREENS:
    out_path = os.path.join(OUTPUT_DIR, out_name)
    url = f"http://127.0.0.1:8765/{filename}"
    print(f"📸 Đang chụp: {out_name} (Kích thước: {w}x{h} Retina)...")
    cmd = [
        "google-chrome",
        "--headless=new",
        f"--screenshot={out_path}",
        f"--window-size={w},{h}",
        "--force-device-scale-factor=2",
        "--hide-scrollbars",
        "--virtual-time-budget=2500",
        "--no-sandbox",
        url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(out_path):
        size_kb = os.path.getsize(out_path) / 1024
        print(f"   ✓ Xong: {size_kb:.1f} KB")
    else:
        print(f"   ✗ Lỗi khi chụp {filename}: {res.stderr}")

# Copy thêm thư mục ảnh gốc HD từ Stitch
orig_ref_dir = os.path.join(OUTPUT_DIR, "ANH_GOC_STITCH_HD_REFERENCES")
os.makedirs(orig_ref_dir, exist_ok=True)
src_img_dir = os.path.join(BASE_DIR, "00-go-stitch-design-package/images")
if os.path.exists(src_img_dir):
    for f in os.listdir(src_img_dir):
        if f.endswith(("_hd.jpg", ".jpg", ".png")):
            shutil.copy2(os.path.join(src_img_dir, f), os.path.join(orig_ref_dir, f))
    print("✓ Đã copy các ảnh gốc HD tham chiếu từ Google Stitch.")

# Tạo file Prompt & Spec kèm theo cho Google Studio
prompt_file = os.path.join(OUTPUT_DIR, "PROMPT_CHO_GOOGLE_STUDIO_TAO_FULLSTACK_WEB.md")
with open(prompt_file, "w", encoding="utf-8") as f:
    f.write("""# HƯỚNG DẪN PROMPT CHO GOOGLE AI STUDIO (TẠO FULL-STACK WEB)

> **Mục tiêu:** Tải toàn bộ các file ảnh chụp màn hình trong gói này lên Google AI Studio (Gemini 1.5 Pro / 2.0 Flash) và dán prompt dưới đây để mô hình dựng thành ứng dụng Full-Stack Web hoàn chỉnh.

---

## 📝 PROMPT CHUẨN ĐỂ COPY DÁN VÀO GOOGLE AI STUDIO:

```text
Dưới đây là toàn bộ ảnh thiết kế giao diện Retina của hệ thống Siêu ứng dụng Điều phối Vận tải & Sàn Nông sản Tiện chuyến Đắk Lắk Express (GO / DXP) dành cho 2 huyện Krông Pắk & Krông Ana (Đắk Lắk).

Hãy phân tích kỹ từng màn hình (từ màn hình 01 đến 16, đặc biệt là nhóm màn hình Tài xế 07, 13, 14, 15):

1. KIẾN TRÚC FULL-STACK:
- Frontend: Single Page Application (SPA / PWA) responsive 100% trên thiết bị di động, chuẩn màu đỏ GO (#F9372D), nền trắng sáng hiện đại (#FFFFFF / #F8F9FA), dùng Tailwind CSS hoặc CSS modules.
- Backend: RESTful API với cơ chế điều phối thời gian thực, quản lý trạng thái chuyến đi (PENDING -> IN_TRANSIT -> COMPLETED).
- Database Schema: Bảng users (tài xế Ba Cường 47A-528.39, Bảy Nam 47A-481.12), rides (chuyến ghép khách Krông Pắk QL26, Krông Ana TL2 đi Buôn Ma Thuột), products (sầu riêng Ri6 Krông Pắk, bơ booth Buôn Trấp, gà KFC), wallet_transactions (chia cước 84% tài xế nhận, 16% phí sàn, rút tiền Napas 24/7 tức thì).

2. BỘ TÍNH NĂNG TRỌNG TÂM CỦA APP TÀI XẾ:
- Màn hình 07 (Console): Nút bật/tắt nhận cuốc Trực Tuyến xanh ngọc, radar cuốc xe, âm thanh còi hú khi nổ cuốc mới, đếm ngược 30s.
- Màn hình 13 (Dẫn đường): Bảng HUD turn-by-turn rẽ QL26 Km 28, tốc độ hiện tại 52km/h, nút gọi điện thoại nhanh và hoàn thành cuốc xe.
- Màn hình 14 (Ví thu nhập): Thẻ số dư ví 3.73M, form rút tiền tức thì Napas 24/7 về Vietcombank, minh bạch phân chia doanh thu 84% - 16%.
- Màn hình 15 (Đăng ký hồ sơ): Hồ sơ tài xế và kiểm định xe 7 chỗ.
- Tích hợp Trợ lý AI GO Copilot: Tối ưu ghép cuốc khứ hồi chống chạy rỗng, soạn tin nhắn đón khách lịch sự, cảnh báo đoạn đường đông dân cư.

Hãy sinh toàn bộ mã nguồn full-stack hoàn chỉnh, có thể chạy ngay lập tức mà không thiếu bất kỳ thành phần nào!
```
""")

print("✓ Đã tạo file PROMPT_CHO_GOOGLE_STUDIO_TAO_FULLSTACK_WEB.md.")

# Đóng gói thành file ZIP duy nhất
print(f"📦 Đang nén toàn bộ thành file ZIP: {ZIP_DEST}...")
with zipfile.ZipFile(ZIP_DEST, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(OUTPUT_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, OUTPUT_DIR)
            zipf.write(file_path, arcname)

zip_size_mb = os.path.getsize(ZIP_DEST) / (1024 * 1024)
print(f"🎉 THÀNH CÔNG! Đã tạo xong file ZIP: {ZIP_DEST} ({zip_size_mb:.2f} MB)")

