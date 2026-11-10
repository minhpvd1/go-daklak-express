# Makefile — Đắk Lắk Express (Hệ thống Điều phối Vận tải & Chợ Nông sản)
.PHONY: all gate test open run help open-pdf open-docx

all: gate

# Kiểm định chất lượng toàn diện 17 tiêu chuẩn hệ thống
gate:
	@python3 04-cong-kiem/cong_kiem.py

# Chạy bộ kiểm thử tự động Backend API & Database
test:
	@cd 03-web-app && python3 -m unittest tests/test_api.py

# Khởi chạy máy chủ Backend Production Engine và mở trình duyệt
run:
	@echo "🌐 Khởi chạy máy chủ Đắk Lắk Express tại: http://localhost:8088"
	@xdg-open http://localhost:8088 >/dev/null 2>&1 &
	@cd 03-web-app && python3 server.py

# Mở trực tiếp Web App trên trình duyệt mặc định
open:
	@xdg-open 03-web-app/static/index.html >/dev/null 2>&1 &
	@echo "🚀 Đã mở Ứng dụng Đắk Lắk Express trên trình duyệt!"

# Mở tài liệu hồ sơ gốc PDF / DOCX
open-pdf:
	@xdg-open 00-nguon/Ho_So_Bao_Gia_Giai_Phap_Goi_Xe_Krong_Pak_Krong_Ana.pdf >/dev/null 2>&1 &

open-docx:
	@xdg-open 00-nguon/Ho_So_Bao_Gia_Giai_Phap_Goi_Xe_Krong_Pak_Krong_Ana.docx >/dev/null 2>&1 &

help:
	@echo "Các lệnh khả dụng:"
	@echo "  make gate      - Chạy cổng kiểm định 17 tiêu chí chất lượng toàn diện"
	@echo "  make test      - Chạy bộ kiểm thử tự động Backend API & SQLite"
	@echo "  make run       - Khởi động Production Server và mở Web tại cổng 8088"
	@echo "  make open      - Mở ngay Web App trên trình duyệt"
	@echo "  make open-pdf  - Mở hồ sơ báo giá đề xuất kỹ thuật PDF"
	@echo "  make open-docx - Mở hồ sơ Word DOCX"
