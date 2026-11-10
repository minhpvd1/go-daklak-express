# INDEX — 12-dieu-phoi-goi-xe-krong-pak-krong-ana

> **Hệ sinh thái Nền tảng Điều phối Vận tải & Chợ Nông sản Tiện chuyến Krông Pắk – Krông Ana – TP. Buôn Ma Thuột**  
> Mô hình kiến trúc giao thoa công nghệ: **Grab × TikTok Shop × Shopee Mall**

---

## 🗂️ CẤU TRÚC PHÂN KHU BẬC THẦY (WORKSPACE DIRECTORY MAP)

| Thư mục / Tệp tin | Vai trò kỹ thuật & Nội dung cốt lõi |
|:---|:---|
| [`00-spec/`](file:///home/minh/30-cong-viec/12-dieu-phoi-goi-xe-krong-pak-krong-ana/00-spec/) | **Bộ Spec Bậc Thầy (Rank S+):** Brainstorming thực địa 2 huyện (`01_BRAINSTORMING_AND_DISCOVERY.md`) & Master Specification kỹ thuật đầy đủ (`02_MASTER_SPECIFICATION_RANK_S.md`). |
| [`00-nguon/`](file:///home/minh/30-cong-viec/12-dieu-phoi-goi-xe-krong-pak-krong-ana/00-nguon/) | **Kho tài liệu gốc:** File Word DOCX, PDF đề xuất kỹ thuật 4 phân hệ WBS & Dự toán kinh phí. |
| [`01-nghien-cuu/`](file:///home/minh/30-cong-viec/12-dieu-phoi-goi-xe-krong-pak-krong-ana/01-nghien-cuu/) | **Báo cáo nghiên cứu UX/UI:** Phân tích ma trận đối chiếu nền tảng Grab, TikTok Shop, Shopee. |
| [`02-giao-dien-prompts/`](file:///home/minh/30-cong-viec/12-dieu-phoi-goi-xe-krong-pak-krong-ana/02-giao-dien-prompts/) | **Bộ Master Prompts Rank S+:** 7 Prompt chi tiết (Markdown + JSON) chuẩn 9 khối master. |
| [`03-web-app/`](file:///home/minh/30-cong-viec/12-dieu-phoi-goi-xe-krong-pak-krong-ana/03-web-app/) | **Hệ thống Full Production:** Backend `server.py` đa luồng, SQLite `dxp_production.db`, Web App trung tâm `static/index.html` và App Tài Xế GO chuyên dụng `static/driver.html`. |
| [`03-web-demo/`](file:///home/minh/30-cong-viec/12-dieu-phoi-goi-xe-krong-pak-krong-ana/03-web-demo/) | **Mockup Demo:** Giao diện tĩnh kiểm tra visual ban đầu. |
| [`04-cong-kiem/`](file:///home/minh/30-cong-viec/12-dieu-phoi-goi-xe-krong-pak-krong-ana/04-cong-kiem/) | **Cổng kiểm định chất lượng (`cong_kiem.py`):** 19 tiêu chí nghiệm thu tự động đạt chuẩn 100% (`rc=0`). |
| [`Makefile`](file:///home/minh/30-cong-viec/12-dieu-phoi-goi-xe-krong-pak-krong-ana/Makefile) | **Bộ lệnh tự động:** `make gate`, `make test`, `make open`, `make run`. |
| [`STATUS.md`](file:///home/minh/30-cong-viec/12-dieu-phoi-goi-xe-krong-pak-krong-ana/STATUS.md) | **Bảng trạng thái thực nghiệm:** Tiến độ, số đo 19 cổng kiểm, lịch sử nâng cấp. |
| [`README.md`](file:///home/minh/30-cong-viec/12-dieu-phoi-goi-xe-krong-pak-krong-ana/README.md) | **Cẩm nang vận hành & Giới thiệu tổng quan dự án.** |

