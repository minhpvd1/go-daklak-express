#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HỆ THỐNG ĐIỀU PHỐI VẬN TẢI & NÔNG SẢN TIỆN CHUYẾN ĐẮK LẮK EXPRESS (DXP)
Backend Production Engine & Web Server (Krông Pắk & Krông Ana)
Tích hợp FOSTA LLM Copilot cho Tài Xế Mobile.
"""

import os
import sys
import json
import time
import sqlite3
import threading
from datetime import datetime
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import urllib.parse

# Thêm đường dẫn toolbox để nạp fosta_llm_engine
TOOLBOX_DIR = os.path.expanduser("~/.gemini/config/engines/toolbox")
if TOOLBOX_DIR not in sys.path:
    sys.path.insert(0, TOOLBOX_DIR)

try:
    from fosta_llm_engine import FostaClient, resolve_model
    FOSTA_AVAILABLE = True
except Exception:
    FOSTA_AVAILABLE = False

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
DB_PATH = os.path.join(BASE_DIR, "dxp_production.db")
DB_LOCK = threading.Lock()

# ==============================================================================
# KHỞI TẠO & SEED CƠ SỞ DỮ LIỆU SQLITE THỰC ĐỊA
# ==============================================================================

def init_database():
    with DB_LOCK:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        # 1. Bảng users
        c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            full_name TEXT NOT NULL,
            phone TEXT UNIQUE NOT NULL,
            district TEXT,
            balance REAL DEFAULT 0,
            rating REAL DEFAULT 5.0,
            avatar TEXT,
            created_at TEXT NOT NULL
        )
        ''')

        # 2. Bảng drivers
        c.execute('''
        CREATE TABLE IF NOT EXISTS drivers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            vehicle_type TEXT NOT NULL,
            license_plate TEXT NOT NULL,
            lat REAL NOT NULL,
            lng REAL NOT NULL,
            is_online INTEGER DEFAULT 1,
            is_busy INTEGER DEFAULT 0,
            completed_trips INTEGER DEFAULT 0,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        ''')

        # 3. Bảng rides
        c.execute('''
        CREATE TABLE IF NOT EXISTS rides (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            customer_phone TEXT NOT NULL,
            origin_name TEXT NOT NULL,
            origin_lat REAL,
            origin_lng REAL,
            destination_name TEXT NOT NULL,
            destination_lat REAL,
            destination_lng REAL,
            ride_type TEXT DEFAULT 'carpool',
            seats INTEGER DEFAULT 1,
            distance_km REAL,
            price REAL NOT NULL,
            driver_id INTEGER,
            status TEXT DEFAULT 'PENDING',
            notes TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            FOREIGN KEY(driver_id) REFERENCES drivers(id)
        )
        ''')

        # 4. Bảng orders
        c.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_code TEXT UNIQUE NOT NULL,
            customer_name TEXT NOT NULL,
            customer_phone TEXT NOT NULL,
            delivery_address TEXT NOT NULL,
            district TEXT NOT NULL,
            total_amount REAL NOT NULL,
            shipping_fee REAL DEFAULT 15000,
            payment_method TEXT DEFAULT 'VIETQR',
            payment_status TEXT DEFAULT 'UNPAID',
            order_status TEXT DEFAULT 'PENDING',
            qr_payload TEXT,
            assigned_driver_id INTEGER,
            created_at TEXT NOT NULL
        )
        ''')

        # 5. Bảng wallet_transactions
        c.execute('''
        CREATE TABLE IF NOT EXISTS wallet_transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            balance_after REAL NOT NULL,
            reference_id TEXT,
            notes TEXT,
            created_at TEXT NOT NULL
        )
        ''')

        # 6. Bảng products (Sàn nông sản & ẩm thực)
        c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            seller_name TEXT NOT NULL,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            unit TEXT NOT NULL,
            rating REAL DEFAULT 5.0,
            image TEXT,
            district TEXT,
            created_at TEXT NOT NULL
        )
        ''')

        # Seed dữ liệu mẫu thực tế nếu chưa có
        c.execute("SELECT COUNT(*) FROM users")
        if c.fetchone()[0] == 0:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Users
            users_data = [
                ("driver", "Ba Cường", "0914528391", "Krông Pắk", 3730000.0, 4.96, "assets/s2_vehicle_suv.png", now),
                ("driver", "Bảy Nam", "0984811234", "Krông Ana", 2150000.0, 4.92, "assets/s2_vehicle_sedan.png", now),
                ("driver", "Văn Tuấn", "0908892445", "Buôn Ma Thuột", 850000.0, 4.88, "assets/s3_shipper_bike.png", now),
                ("customer", "Chị Lan Ea Kly", "0945112233", "Krông Pắk", 250000.0, 5.0, "", now),
                ("customer", "Anh Hùng Buôn Trấp", "0912889900", "Krông Ana", 500000.0, 5.0, "", now),
                ("seller", "HTX Sầu Riêng Krông Pắk", "0918776655", "Krông Pắk", 15200000.0, 4.98, "", now),
                ("dispatcher", "Tổng Đài DXP Trung Tâm", "19004726", "Buôn Ma Thuột", 0.0, 5.0, "", now)
            ]
            c.executemany("INSERT INTO users (role, full_name, phone, district, balance, rating, avatar, created_at) VALUES (?,?,?,?,?,?,?,?)", users_data)

            # Drivers
            drivers_data = [
                (1, "car_7", "47A-528.39", 12.6714, 108.2889, 1, 0, 184), # Ba Cường (Phước An)
                (2, "car_4", "47A-481.12", 12.4833, 108.0167, 1, 0, 126), # Bảy Nam (Buôn Trấp)
                (3, "bike", "47B1-892.44", 12.6667, 108.0333, 1, 0, 92)    # Văn Tuấn (BMT)
            ]
            c.executemany("INSERT INTO drivers (user_id, vehicle_type, license_plate, lat, lng, is_online, is_busy, completed_trips) VALUES (?,?,?,?,?,?,?,?)", drivers_data)

            # Products
            products_data = [
                ("HTX Sầu Riêng Krông Pắk", "Sầu Riêng Ri6 Chín Cây (Loại 1)", "nong_san", 85000.0, "kg", 4.95, "assets/s4_food_banhtrang.jpg", "Krông Pắk", now),
                ("HTX Sầu Riêng Krông Pắk", "Sầu Riêng Dona Xuất Khẩu", "nong_san", 110000.0, "kg", 5.0, "assets/s4_food_banhtrang.jpg", "Krông Pắk", now),
                ("Vựa Bơ Buôn Trấp", "Bơ Booth Đắk Lắk Sáp Dẻo", "nong_san", 45000.0, "kg", 4.88, "assets/s4_food_cake.jpg", "Krông Ana", now),
                ("KFC Vietnam BMT", "Combo Gà Rán Giòn Cay + Khoai Tây", "am_thuc", 89000.0, "combo", 4.9, "assets/s6_hero_detail.jpg", "Buôn Ma Thuột", now),
                ("Quán Gà Đồi Buôn Trấp", "Gà Nướng Cơm Lam Krông Ana", "am_thuc", 220000.0, "con", 4.96, "assets/s5_post_bucket.jpg", "Krông Ana", now)
            ]
            c.executemany("INSERT INTO products (seller_name, title, category, price, unit, rating, image, district, created_at) VALUES (?,?,?,?,?,?,?,?,?)", products_data)

            # Sample Rides
            rides_data = [
                ("Chị H'Mai", "0934112233", "Chợ Phước An, Krông Pắk", 12.6714, 108.2889, "Bệnh Viện Vùng Tây Nguyên, BMT", 12.6680, 108.0550, "carpool", 2, 34.5, 340000.0, 1, "IN_TRANSIT", "Khách mang kèm 1 thùng sầu riêng gửi xe", now, now),
                ("Bác Năm", "0912445566", "UBND Xã Ea Kly, Krông Pắk", 12.6820, 108.3100, "Ngã 6 Buôn Ma Thuột", 12.6667, 108.0333, "carpool", 1, 38.0, 120000.0, None, "PENDING", "Đón lúc 10h15 sáng", now, now),
                ("Anh Tuấn", "0987332211", "TT. Buôn Trấp, Krông Ana", 12.4833, 108.0167, "Đại Học Tây Nguyên, BMT", 12.6550, 108.0280, "carpool", 1, 26.0, 85000.0, None, "PENDING", "Tiện chuyến đi khám bệnh", now, now)
            ]
            c.executemany("INSERT INTO rides (customer_name, customer_phone, origin_name, origin_lat, origin_lng, destination_name, destination_lat, destination_lng, ride_type, seats, distance_km, price, driver_id, status, notes, created_at, updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rides_data)

            # Wallet transactions
            wallet_data = [
                (1, "TRIP_EARNING", 285600.0, 3730000.0, "RIDE_001", "Cước cuốc xe Phước An - BV Vùng (84%)", now),
                (1, "PLATFORM_FEE", -54400.0, 3444400.0, "RIDE_001", "Phí nền tảng DXP (16%)", now)
            ]
            c.executemany("INSERT INTO wallet_transactions (user_id, type, amount, balance_after, reference_id, notes, created_at) VALUES (?,?,?,?,?,?,?)", wallet_data)

        conn.commit()
        conn.close()


# ==============================================================================
# HTTP REQUEST HANDLER (REST API + PWA STATIC FILES)
# ==============================================================================

class DXPHTTPRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    def _send_json(self, data, status_code=200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        # 1. API Health
        if path == "/api/health":
            self._send_json({"status": "ok", "system": "DXP-KrongPak-KrongAna", "time": datetime.now().isoformat()})
            return

        # 2. API Bootstrap
        if path == "/api/bootstrap":
            with DB_LOCK:
                conn = sqlite3.connect(DB_PATH)
                conn.row_factory = sqlite3.Row
                c = conn.cursor()
                c.execute("SELECT * FROM users")
                users = [dict(r) for r in c.fetchall()]
                c.execute("SELECT d.*, u.full_name, u.phone, u.district, u.balance, u.rating FROM drivers d JOIN users u ON d.user_id = u.id")
                drivers = [dict(r) for r in c.fetchall()]
                c.execute("SELECT * FROM products")
                products = [dict(r) for r in c.fetchall()]
                c.execute("SELECT * FROM rides WHERE status = 'PENDING'")
                rides = [dict(r) for r in c.fetchall()]
                conn.close()

            self._send_json({
                "users": users,
                "drivers": drivers,
                "products": products,
                "pending_rides": rides
            })
            return

        # 3. API Danh sách chuyến xe
        if path == "/api/rides":
            qs = urllib.parse.parse_qs(parsed.query)
            status_filter = qs.get("status", [None])[0]
            driver_filter = qs.get("driver_id", [None])[0]

            with DB_LOCK:
                conn = sqlite3.connect(DB_PATH)
                conn.row_factory = sqlite3.Row
                c = conn.cursor()
                query = "SELECT * FROM rides WHERE 1=1"
                params = []
                if status_filter:
                    query += " AND status = ?"
                    params.append(status_filter)
                if driver_filter:
                    query += " AND driver_id = ?"
                    params.append(driver_filter)
                query += " ORDER BY id DESC"
                c.execute(query, params)
                rides = [dict(r) for r in c.fetchall()]
                conn.close()

            self._send_json({"rides": rides, "total": len(rides)})
            return

        # 4. API Thông tin tài xế & ví
        if path == "/api/driver/current":
            with DB_LOCK:
                conn = sqlite3.connect(DB_PATH)
                conn.row_factory = sqlite3.Row
                c = conn.cursor()
                # Mặc định lấy tài xế Ba Cường (ID 1)
                c.execute("SELECT d.*, u.full_name, u.phone, u.district, u.balance, u.rating FROM drivers d JOIN users u ON d.user_id = u.id WHERE d.id = 1")
                row = c.fetchone()
                driver = dict(row) if row else {}
                c.execute("SELECT * FROM rides WHERE driver_id = 1 AND status = 'IN_TRANSIT'")
                active_ride = c.fetchone()
                driver["active_ride"] = dict(active_ride) if active_ride else None
                conn.close()

            self._send_json(driver)
            return

        if path == "/api/wallet":
            with DB_LOCK:
                conn = sqlite3.connect(DB_PATH)
                conn.row_factory = sqlite3.Row
                c = conn.cursor()
                c.execute("SELECT balance FROM users WHERE id = 1")
                bal = c.fetchone()[0]
                c.execute("SELECT * FROM wallet_transactions WHERE user_id = 1 ORDER BY id DESC LIMIT 10")
                txs = [dict(r) for r in c.fetchall()]
                conn.close()

            self._send_json({
                "balance": bal,
                "driver_share_pct": 84,
                "platform_fee_pct": 16,
                "transactions": txs
            })
            return

        # Route mặc định phục vụ static files (index.html, driver.html, v.v.)
        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        content_len = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_len).decode("utf-8") if content_len > 0 else "{}"
        try:
            payload = json.loads(body)
        except Exception:
            payload = {}

        # 1. Bật/tắt trạng thái nhận cuốc của tài xế
        if path == "/api/drivers/1/toggle-online" or path == "/api/driver/toggle-online":
            with DB_LOCK:
                conn = sqlite3.connect(DB_PATH)
                c = conn.cursor()
                c.execute("UPDATE drivers SET is_online = CASE WHEN is_online = 1 THEN 0 ELSE 1 END WHERE id = 1")
                c.execute("SELECT is_online FROM drivers WHERE id = 1")
                new_state = c.fetchone()[0]
                conn.commit()
                conn.close()

            self._send_json({"success": True, "is_online": bool(new_state), "message": "Đã đổi trạng thái trực tuyến!"})
            return

        # 2. Khách đặt cuốc xe mới
        if path == "/api/rides":
            customer_name = payload.get("customer_name", "Khách vãng lai")
            customer_phone = payload.get("customer_phone", "0900000000")
            origin = payload.get("origin_name", "TT. Phước An")
            destination = payload.get("destination_name", "TP. Buôn Ma Thuột")
            price = float(payload.get("price", 150000))
            distance = float(payload.get("distance_km", 30))
            ride_type = payload.get("ride_type", "carpool")
            seats = int(payload.get("seats", 1))
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with DB_LOCK:
                conn = sqlite3.connect(DB_PATH)
                c = conn.cursor()
                c.execute('''
                INSERT INTO rides (customer_name, customer_phone, origin_name, destination_name, distance_km, price, ride_type, seats, status, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'PENDING', ?, ?)
                ''', (customer_name, customer_phone, origin, destination, distance, price, ride_type, seats, now, now))
                ride_id = c.lastrowid
                conn.commit()
                conn.close()

            self._send_json({"success": True, "ride_id": ride_id, "message": "Đã tạo cuốc xe mới!"}, status_code=201)
            return

        # 3. Mô phỏng nổ cuốc xe mới (Simulate Ride)
        if path == "/api/rides/simulate":
            routes = [
                ("Chị H'Mai Krông Pắk", "0945667788", "Chợ Phước An, QL26", 12.6714, 108.2889, "Bệnh Viện Thiện Hạnh BMT", 12.6900, 108.0600, 32.0, 240000.0, "carpool", 1, "Ghép 1 khách lên viện tái khám"),
                ("Anh Long Buôn Trấp", "0918223344", "Bến đò Buôn Trấp, Krông Ana", 12.4833, 108.0167, "Sân Bay Buôn Ma Thuột", 12.6680, 108.1200, 30.5, 310000.0, "private", 4, "Bao xe 4 chỗ đi máy bay"),
                ("Bác Ba Ea Yông", "0977112233", "Ngã 3 Ea Yông, QL26", 12.6750, 108.2500, "Bến xe Liên tỉnh Đắk Lắk", 12.6600, 108.0400, 28.0, 180000.0, "carpool", 2, "Gửi kèm 2 thùng sầu riêng Ri6")
            ]
            import random
            choice = random.choice(routes)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with DB_LOCK:
                conn = sqlite3.connect(DB_PATH)
                c = conn.cursor()
                c.execute('''
                INSERT INTO rides (customer_name, customer_phone, origin_name, origin_lat, origin_lng, destination_name, destination_lat, destination_lng, distance_km, price, ride_type, seats, notes, status, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'PENDING', ?, ?)
                ''', (choice[0], choice[1], choice[2], choice[3], choice[4], choice[5], choice[6], choice[7], choice[8], choice[9], choice[10], choice[11], choice[12], now, now))
                ride_id = c.lastrowid
                conn.commit()
                conn.close()

            self._send_json({"success": True, "ride_id": ride_id, "ride": {
                "id": ride_id, "customer_name": choice[0], "origin_name": choice[2], "destination_name": choice[5], "price": choice[9], "notes": choice[12]
            }}, status_code=201)
            return

        # 4. Tài xế nhận cuốc xe (Accept Ride)
        if path.startswith("/api/rides/") and path.endswith("/accept"):
            try:
                ride_id = int(path.split("/")[3])
            except Exception:
                ride_id = payload.get("ride_id")

            driver_id = payload.get("driver_id", 1)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with DB_LOCK:
                conn = sqlite3.connect(DB_PATH)
                c = conn.cursor()
                c.execute("SELECT status FROM rides WHERE id = ?", (ride_id,))
                row = c.fetchone()
                if not row or row[0] != "PENDING":
                    conn.close()
                    self._send_json({"success": False, "message": "Cuốc xe đã được tài xế khác nhận hoặc không tồn tại!"}, status_code=400)
                    return

                c.execute("UPDATE rides SET status = 'IN_TRANSIT', driver_id = ?, updated_at = ? WHERE id = ?", (driver_id, now, ride_id))
                c.execute("UPDATE drivers SET is_busy = 1 WHERE id = ?", (driver_id,))
                c.execute("SELECT * FROM rides WHERE id = ?", (ride_id,))
                conn.row_factory = sqlite3.Row
                c2 = conn.cursor()
                c2.execute("SELECT * FROM rides WHERE id = ?", (ride_id,))
                updated_ride = dict(c2.fetchone())
                conn.commit()
                conn.close()

            self._send_json({"success": True, "ride": updated_ride, "message": "Đã nhận cuốc xe thành công!"})
            return

        # 5. Hoàn thành cuốc xe (Complete Ride & Phân chia 84% - 16%)
        if path.startswith("/api/rides/") and path.endswith("/complete"):
            try:
                ride_id = int(path.split("/")[3])
            except Exception:
                ride_id = payload.get("ride_id")

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with DB_LOCK:
                conn = sqlite3.connect(DB_PATH)
                conn.row_factory = sqlite3.Row
                c = conn.cursor()
                c.execute("SELECT * FROM rides WHERE id = ?", (ride_id,))
                ride = c.fetchone()
                if not ride:
                    conn.close()
                    self._send_json({"success": False, "message": "Không tìm thấy cuốc xe!"}, status_code=404)
                    return

                total_fare = ride["price"]
                driver_earning = round(total_fare * 0.84, 0)
                platform_fee = round(total_fare * 0.16, 0)
                driver_id = ride["driver_id"] or 1

                # Cập nhật số dư tài xế (User ID 1)
                c.execute("SELECT balance FROM users WHERE id = ?", (driver_id,))
                current_bal = c.fetchone()[0]
                new_bal = current_bal + driver_earning

                c.execute("UPDATE users SET balance = ? WHERE id = ?", (new_bal, driver_id))
                c.execute("UPDATE rides SET status = 'COMPLETED', updated_at = ? WHERE id = ?", (now, ride_id))
                c.execute("UPDATE drivers SET is_busy = 0, completed_trips = completed_trips + 1 WHERE id = ?", (driver_id,))

                # Ghi sổ ví
                c.execute('''
                INSERT INTO wallet_transactions (user_id, type, amount, balance_after, reference_id, notes, created_at)
                VALUES (?, 'TRIP_EARNING', ?, ?, ?, ?, ?)
                ''', (driver_id, driver_earning, new_bal, f"RIDE_{ride_id}", f"Thu nhập cuốc xe #{ride_id} (84%)", now))

                conn.commit()
                conn.close()

            self._send_json({
                "success": True,
                "fare": total_fare,
                "driver_earning": driver_earning,
                "platform_fee": platform_fee,
                "new_balance": new_bal,
                "message": f"Hoàn thành cuốc xe! Thu nhập thực nhận +{driver_earning:,.0f}đ (84%)"
            })
            return

        # 6. Rút tiền nhanh VietQR Napas 24/7
        if path == "/api/wallet/withdraw":
            amount = float(payload.get("amount", 500000))
            bank = payload.get("bank", "Vietcombank")
            account_no = payload.get("account_no", "1028472910")
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with DB_LOCK:
                conn = sqlite3.connect(DB_PATH)
                c = conn.cursor()
                c.execute("SELECT balance FROM users WHERE id = 1")
                current_bal = c.fetchone()[0]
                if current_bal < amount:
                    conn.close()
                    self._send_json({"success": False, "message": "Số dư ví không đủ để rút!"}, status_code=400)
                    return

                new_bal = current_bal - amount
                c.execute("UPDATE users SET balance = ? WHERE id = 1", (new_bal,))
                c.execute('''
                INSERT INTO wallet_transactions (user_id, type, amount, balance_after, reference_id, notes, created_at)
                VALUES (1, 'WITHDRAW', ?, ?, ?, ?, ?)
                ''', (-amount, new_bal, f"W_{int(time.time())}", f"Rút tiền Napas 24/7 về {bank} ({account_no})", now))
                conn.commit()
                conn.close()

            self._send_json({
                "success": True,
                "amount": amount,
                "new_balance": new_bal,
                "transfer_time": "Tức thì (Napas 247)",
                "message": f"Đã chuyển thành công {amount:,.0f}đ về tài khoản ngân hàng của anh!"
            })
            return

        # 7. TRỢ LÝ AI TÀI XẾ "GO COPILOT" (FOSTA LLM TÍCH HỢP)
        if path == "/api/driver/ai-copilot":
            prompt = payload.get("prompt", "").strip()
            complexity = payload.get("complexity", "standard") # astra, sol, luna
            context = payload.get("context", {})

            if not prompt:
                self._send_json({"success": False, "message": "Thiếu câu hỏi prompt"}, status_code=400)
                return

            system_instruction = (
                "Bạn là 'GO Copilot' — Trợ lý AI thực chiến đồng hành cùng các bác tài xế 2 huyện Krông Pắk & Krông Ana (Đắk Lắk).\n"
                "Nhiệm vụ:\n"
                "1. Tối ưu ghép cuốc khứ hồi (chống chạy xe rỗng chiều về từ BMT về Phước An / Buôn Trấp).\n"
                "2. Gợi ý giá cước chở nông sản (sầu riêng Ri6, Dona, bơ booth) kèm khách.\n"
                "3. Soạn tin nhắn khách hàng lịch sự, nhã nhặn, tôn trọng khách.\n"
                "4. Cảnh báo tốc độ trên QL26 (đoạn qua chợ Ea Yông, Ea Phê) và Tỉnh lộ 2 (dốc Buôn Trấp).\n"
                "Trả lời súc tích, ngắn gọn, thiết thực, nói thẳng vào vấn đề cho bác tài đang lái xe."
            )

            response_text = ""
            model_used = "fosta-llm"
            is_fallback = False
            latency = 45.0

            if FOSTA_AVAILABLE:
                try:
                    client = FostaClient()
                    res_content, fb, lat = client.smart_execute(
                        prompt=prompt,
                        task_type=complexity,
                        system_prompt=system_instruction
                    )
                    if not fb and res_content:
                        response_text = res_content
                        model_used = resolve_model(complexity)
                        latency = lat
                    else:
                        is_fallback = True
                except Exception:
                    is_fallback = True
            else:
                is_fallback = True

            # Chế độ Fallback thông minh cục bộ nếu FOSTA hết token hoặc chưa gắn key
            if is_fallback or not response_text:
                model_used = "dxp-local-failover"
                p_lower = prompt.lower()
                if "ghép" in p_lower or "khứ hồi" in p_lower:
                    response_text = (
                        "💡 [Gợi ý ghép cuốc chiều về QL26]: Anh Ba Cường đang trả khách tại BV Vùng Tây Nguyên. "
                        "Hiện có 2 khách ở Chợ Đầu Mối Tân Hòa muốn về TT. Phước An (đón sau 15 phút, giá 120k/ghế). "
                        "Kèm 1 thùng sầu riêng gửi về Km 38. Bác tài ghép luôn để đầy xe khứ hồi, thu thêm +340.000đ!"
                    )
                elif "tin nhắn" in p_lower or "soạn" in p_lower:
                    response_text = (
                        "📱 [Tin nhắn gửi khách]: 'Dạ em là Ba Cường tài xế GO Đắk Lắk Express (xe 7 chỗ 47A-528.39). "
                        "Em đang trên đường đến đón chị tại Chợ Phước An, khoảng 7 phút nữa em có mặt. Chị chuẩn bị giúp em nhé ạ!'"
                    )
                elif "tốc độ" in p_lower or "công an" in p_lower or "đường" in p_lower:
                    response_text = (
                        "⚠️ [Cảnh báo lộ trình QL26]: Đoạn qua Ea Kly và Ea Yông giới hạn 50km/h khu đông dân cư. "
                        "Đường đẹp, mặt đường khô ráo, chú ý xe máy qua đường tại chợ chiều Phước An!"
                    )
                else:
                    response_text = (
                        f"🤖 [GO Copilot]: Đã tiếp nhận yêu cầu: '{prompt}'. Tuyến đường Krông Pắk - Krông Ana hiện lưu thông thông suốt. "
                        "Hệ thống tự động ưu tiên nổ các cuốc xe ghép có giá trị cao nhất cho anh!"
                    )

            self._send_json({
                "success": True,
                "reply": response_text,
                "model_used": model_used,
                "is_fallback": is_fallback,
                "latency_ms": latency
            })
            return

        # Endpoint không tồn tại
        self._send_json({"error": "Endpoint not found"}, status_code=404)


# ==============================================================================
# HÀM CHÍNH KHỞI CHẠY SERVER
# ==============================================================================

def run_server(port=8765):
    init_database()
    server_address = ('', port)
    httpd = ThreadingHTTPServer(server_address, DXPHTTPRequestHandler)
    print(f"🚀 [DXP PRODUCTION SERVER] Đang chạy tại http://localhost:{port}")
    print(f"📱 App Tài Xế Mobile:  http://localhost:{port}/driver.html")
    print(f"🖥️ Portal Tổng Hợp:   http://localhost:{port}/index.html")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Đang dừng server...")
        httpd.server_close()


if __name__ == "__main__":
    p = 8765
    if len(sys.argv) > 1:
        try:
            p = int(sys.argv[1])
        except ValueError:
            pass
    run_server(p)

