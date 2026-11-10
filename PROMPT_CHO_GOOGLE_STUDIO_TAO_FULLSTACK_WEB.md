# HƯỚNG DẪN PROMPT CHO GOOGLE AI STUDIO (TẠO FULL-STACK WEB)

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
