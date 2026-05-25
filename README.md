# 🎮 SimSociety 2D: Hệ Thống Mô Phỏng Biến Chứng 4.5

**SimSociety 2D** là một trò chơi mô phỏng chính trị và kinh tế theo thời gian thực, nơi bạn đóng vai trò một nhà lãnh đạo quốc gia cố gắng cân bằng các lực lượng xã hội đối lập để xây dựng xã hội lý tưởng.

![Game Screenshot](./assets/screenshot.png)

## 📋 Mục Lục

- [Tính Năng](#tính-năng)
- [Yêu Cầu Hệ Thống](#yêu-cầu-hệ-thống)
- [Cài Đặt & Chạy](#cài-đặt--chạy)
- [Cách Chơi](#cách-chơi)
- [Cơ Chế Trò Chơi](#cơ-chế-trò-chơi)
- [Các Kết Thúc (Endings)](#các-kết-thúc-endings)
- [Cấu Trúc Dự Án](#cấu-trúc-dự-án)
- [Kiến Trúc Hệ Thống](#kiến-trúc-hệ-thống)
- [Phát Triển & Đóng Góp](#phát-triển--đóng-góp)

---

## 🌟 Tính Năng

### Cơ Bản
- ✅ **Mô Phỏng Kinh Tế Thực Tế**: Quản lý ngân sách, thu nhập hàng năm, và tài chính quốc gia
- ✅ **Hệ Thống Phe Phái**: Cân bằng lợi ích của Công Nhân vs. Chủ Tư Bản
- ✅ **Nâng Cấp Công Nghệ**: 3 giai đoạn phát triển (Nông Nghiệp → Công Nghiệp → AI)
- ✅ **Chính Sách Động Lực**: Ban hành luật lệ để ảnh hưởng tới xã hội
- ✅ **Biến Cố Ngẫu Nhiên**: Khủng hoảng tài chính, khởi nghiệp số, cuộc đình công

### Nâng Cao
- 🎭 **Hệ Thống Ý Thức Hình Thái**: 4 hình thái chính trị xuất hiện dựa trên cân bằng phe phái
- 📊 **Chỉ Số Xã Hội**: Theo dõi thất nghiệp, bất bình đẳng, căng thẳng cách mạng
- 🏛️ **Lịch Sử Triều Đại**: Ghi lại các sự kiện lịch sử trong quá trình chơi
- 🎯 **4 Kết Thúc Riêng Biệt**: Utopia, Độc Tài Công Nghệ, Cách Mạng, hoặc Sụp Đổ
- 🎨 **Giao Diện Retro Premium**: Thiết kế UI hiện đại với cảm giác retro

---

## 💻 Yêu Cầu Hệ Thống

### Bắt Buộc
- **Python**: 3.8+
- **Pygame**: 2.0+
- **OS**: Windows, macOS, hoặc Linux

### Tùy Chọn
- **Git**: Để clone dự án

---

## 🚀 Cài Đặt & Chạy

### 1. Clone Repository
```bash
git clone https://github.com/Eddie0517/MLN_GAME.git
cd MLN_GAME
```

### 2. Tạo Virtual Environment (Khuyến Nghị)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Cài Đặt Dependencies
```bash
pip install pygame
```

### 4. Chạy Game
```bash
python main.py
```

### Chế Độ Toàn Màn Hình
- Nhấn **F11** để bật/tắt chế độ toàn màn hình

---

## 🎮 Cách Chơi

### Điều Khiển Cơ Bản

| Phím | Hành Động |
|------|-----------|
| **Arrow Keys** hoặc **WASD** | Di chuyển nhân vật |
| **SPACE** | Tương tác với khu vực hiện tại |
| **1** | Ban hành Thuế AI (khi ở ô Thượng Tầng) |
| **2** | Ban hành Luật Phúc Lợi Công Nhân (khi ở ô Thượng Tầng) |
| **F11** | Bật/Tắt toàn màn hình |
| **R** | Khởi động lại trò chơi (khi kết thúc) |

### Khu Vực Chính

**Bên Trái - CƠ SỞ HẠ TẦNG**
- Nâng cấp cơ sở hạ tầng kinh tế để tăng công nghệ
- Xem các chỉ số thất nghiệp & bất bình đẳng
- Chi phí nâng cấp tăng theo giai đoạn

**Giữa - NÚT QUA NĂM**
- Bước sang năm tiếp theo để nhận thu nhập
- Kích hoạt biến cố ngẫu nhiên
- Cập nhật tất cả các chỉ số kinh tế

**Bên Phải - KIẾN TRÚC THƯỢNG TẦNG**
- Ban hành các chính sách để ảnh hưởng tới xã hội
- Xem trạng thái kích hoạt của từng chính sách
- Mỗi chính sách có hiệu ứng khác nhau

---

## 🎯 Cơ Chế Trò Chơi

### Hệ Thống Phe Phái

Xã hội được chia thành 2 phe chính:
- **👷 Công Nhân**: Quan tâm đến phúc lợi, quyền lợi, bình đẳng
- **💼 Chủ Tư Bản**: Quan tâm đến lợi nhuận, hiệu suất, đổi mới

### Giai Đoạn Công Nghệ

```
Level 1 (Nông Nghiệp)
  ↓ Cần 60 Vàng
Level 2 (Công Nghiệp)
  ↓ Cần 120 Vàng
Level 3 (AI/Số)
  ↓ Mục tiêu cuối cùng
```

### Chỉ Số Kinh Tế

| Chỉ Số | Mô Tả | Ảnh Hưởng |
|--------|-------|----------|
| **Gold** | Ngân sách quốc gia (có thể âm = nợ) | Khả năng ban hành chính sách |
| **Income** | Thu nhập hàng năm từ sản xuất | Tăng khi nâng tech level |
| **Unemployment** | Tỷ lệ thất nghiệp (%) | Tăng với automation, giảm với chính sách |
| **Inequality** | Chỉ số bất bình đẳng thu nhập | Ảnh hưởng tới căng thẳng cách mạng |
| **Revolution Tension** | Áp lực xã hội (0-∞) | Đạt 30 = Kết thúc 3 |

### Các Chính Sách

**P1: Thuế Livestream & AI Shop** (Yêu cầu Tech 3)
- Chi phí: 40 Vàng
- Hiệu ứng: +15 Hỗ trợ Chủ Tư Bản, -15 Hỗ trợ Công Nhân
- Ý tưởng: Chính sách ủng hộ công nghệ

**P2: Luật Phúc Lợi Công Nhân** (Yêu cầu Tech 1+)
- Chi phí: 35 Vàng
- Hiệu ứng: +25 Hỗ trợ Công Nhân, -20 Hỗ trợ Chủ Tư Bản
- Ý tưởng: Chính sách bảo vệ lao động

### Ý Thức Hình Thái (Tự Động Phát Hiện)

```
Dân Chủ Xã Hội (Mặc định)
  ↓ (Cân bằng tương đối)

Chủ Nghĩa Tư Bản Tự Do
  (Cả 2 phe hỗ trợ cao)

Chủ Nghĩa Xã Hội Thắp Sáng
  (Công Nhân hỗ trợ cao)

Chủ Nghĩa Độc Tài AI (Technocracy)
  (Tech cao + Chủ Tư Bản hỗ trợ cao)
```

### Biến Cố Ngẫu Nhiên (50% mỗi năm)

1. **Khủng Hoảng Tài Chính** ⚠️
   - Giảm income, tăng unemployment
   
2. **Bùng Nổ Startup Số** 🚀
   - Tăng income, tăng tech support
   
3. **Đình Công Giai Cấp** ✊
   - Tăng căng thẳng cách mạng, ảnh hưởng tới income

---

## 🎬 Các Kết Thúc (Endings)

Trò chơi kết thúc khi một trong các điều kiện dưới được đáp ứng:

### ❌ ENDING 4: SỤP ĐỔ TOÀN DIỆN (Thất Bại) [ƯUTIÊN #1]
**Điều kiện**: 
- Lòng dân trung bình ≤ 20% HOẶC Ngân sách < -40 Vàng

**Mô Tả**: Nhà nước tan rã hoàn toàn do khủng hoảng cực hạn. Sự kiểm soát xã hội bị mất hoàn toàn.

---

### 🌈 ENDING 1: KỶ NGUYÊN HOÀNG KIM (Utopia AI) (Chiến Thắng Tuyệt Vời) ⭐
**Điều kiện**:
- Tech Level = 3
- Lòng dân trung bình ≥ 80%
- Ngân sách ≥ 250 Vàng

**Mô Tả**: Xã hội phát triển tối ưu toàn diện! Bạn đã tạo ra một utopia hiện đại nơi công nghệ phục vụ nhân loại, không ai bị bỏ lại phía sau.

---

### 🤖 ENDING 2: ĐỘC TÀI CÔNG NGHỆ (Cyberpunk Dictatorship) (Chiến Thắng Buồn)
**Điều kiện**:
- Tech Level = 3
- Ý Thức Hình Thái = "Chủ Nghĩa Độc Tài AI (Technocracy)"

**Mô Tả**: Giới chủ dùng AI kiểm soát xã hội. Xã hội trở thành một megatropolis cyberpunk phân hóa cao, nơi giàu sống trong tháp chọc trời còn nghèo sống dưới lòng đất.

---

### ✊ ENDING 3: CÁCH MẠNG LAO ĐỘNG (Socialist Revolution)
**Điều kiện**:
- Căng Thẳng Cách Mạng ≥ 30

**Mô Tả**: Công nhân lật đổ ách áp bức của giới chủ! Cách mạng vô sản bùng nổ giành chính quyền thành công. Nền kinh tế được tái cấu trúc theo nguyên tắc xã hội.

---

## 📁 Cấu Trúc Dự Án

```
MLN_GAME/
├── main.py                           # Game Manager chính - vòng lặp game
├── config.py                         # Cấu hình toàn cầu (màn hình, font, màu)
├── player.py                         # Lớp Player - điều khiển nhân vật
├── economy.py                        # Lớp EconomyState - mô phỏng kinh tế
├── policy.py                         # Lớp PolicyManager - quản lý chính sách
├── events.py                         # Lớp EventEngine - hệ thống biến cố
├── ui.py                             # Lớp UIEngine - rendering UI
├── player.png                        # Sprite nhân vật
├── .gitignore                        # Git ignore rules
├── README.md                         # File này
└── assets/
    ├── Fábrica_Industrial...png     # Hình ảnh nhà máy
    ├── Independence Palace.jpg       # Hình ảnh cung độc lập
    └── LA IA EN UNIVERSO.jpg        # Hình ảnh AI
```

---

## 🏗️ Kiến Trúc Hệ Thống

### Sơ Đồ Thành Phần

```
                    GameManager (main.py)
                           |
        ┌──────────────────┼──────────────────┐
        |                  |                  |
    Player           EconomyState         PolicyManager
    (Điều khiển)    (Mô phỏng)           (Chính sách)
        |                  |                  |
        └──────────────────┼──────────────────┘
                           |
                    EventEngine
                  (Biến cố ngẫu nhiên)
                           |
                       UIEngine
                      (Rendering)
```

### Luồng Dữ Liệu Mỗi Frame

```
1. handle_input()      → Xử lý keyboard input
2. update()            → Cập nhật game state
3. check_endings()     → Kiểm tra điều kiện kết thúc
4. render()            → Vẽ 5 lớp hình ảnh
5. flip()              → Cập nhật display
6. tick(FPS)           → Giới hạn ở 60 FPS
```

### Các Lớp Rendering

| Layer | Mục Đích | Độ Sâu |
|-------|----------|--------|
| 0 | Phông nền & đường trung tâm | Thấp nhất |
| 1 | 2 thẻ bài (Cơ Sở Hạ Tầng & Thượng Tầng) | - |
| 2 | HUD, nút bấm, thông tin | - |
| 3 | Nhân vật người chơi | - |
| 4 | Game Over Overlay | Cao nhất |

---

## 👨‍💻 Phát Triển & Đóng Góp

### Yêu Cầu Phát Triển
```bash
pip install pygame
```

### Cấu Trúc Mã

**Quy ước Mã**:
- Tên biến: `snake_case`
- Tên lớp: `PascalCase`
- Tên hàm: `snake_case`
- Hằng số: `UPPERCASE`
- Bình luận: Tiếng Việt, giải thích TÍNH ĐẶC BIỆT

**Màu Sắc Hệ Thống** (config.py):
```python
COLOR_GOLD = (255, 191, 0)      # Vàng hoàng gia
COLOR_MINT = (0, 230, 160)      # Xanh bạc hà
COLOR_PINK = (255, 64, 129)     # Hồng
COLOR_RED = (235, 60, 60)       # Đỏ
```

### Thêm Tính Năng Mới

**Ví dụ: Thêm Chính Sách Mới**

1. Chỉnh sửa `policy.py`:
```python
self.policies = [
    Policy("P1", "Tên Chính Sách", 50, {...}),  # Thêm dòng này
]
```

2. Cập nhật `main.py`:
```python
elif keys[pygame.K_3]:
    self.policy_box.execute_policy_by_id("P3", self.eco)
```

### Gỡ Lỗi

**Chế độ Debug** (thêm vào main.py):
```python
print(f"DEBUG - Gold: {self.eco.gold}, Tech: {self.eco.tech_level}")
print(f"DEBUG - Player: ({self.player.x}, {self.player.y})")
```

---

## 🐛 Báo Cáo Lỗi

Nếu gặp vấn đề:

1. Kiểm tra các file ảnh tồn tại
2. Cập nhật Pygame: `pip install --upgrade pygame`
3. Chạy lại game
4. Mở issue trên GitHub nếu lỗi vẫn tiếp tục

---

## 📝 Ghi Chú Kỹ Thuật

### Cơ Chế Biến Cố

```python
# 50% xác suất mỗi năm
if random() < 0.50:
    random_event = choice(EVENT_POOL)
    apply_event_effects()
```

### Hệ Thống Ý Thức Hình Thái

Ý thức hình thái được xác định bằng:
```
worker_support vs capitalist_support
```

### Cơ Chế Lợi Nhuận Kinh Tế

```
gold += income
income = BASE_INCOME * (1 + tech_bonus)
tech_level → income_multiplier
```

### Căng Thẳng Cách Mạng

```
Tăng khi:
- worker_support < 40
- inequality > 70
- unemployment > 50
- Biến cố xấu

Giảm khi:
- Chính sách phúc lợi được ban hành
- worker_support tăng cao
```

---

## 📚 Tài Liệu Tham Khảo

- **Pygame Docs**: https://www.pygame.org/docs/
- **Python 3.8+**: https://www.python.org/
- **Git Guide**: https://git-scm.com/doc

---

## 📜 Giấy Phép

Dự án này được phát hành dưới giấy phép **MIT**.

---

## ✨ Lưu Ý Tác Giả

**SimSociety 2D** được tạo như một thí nghiệm trong **mô phỏng xã hội phức tạp**, kết hợp:
- Lý thuyết kinh tế
- Động lực học xã hội
- Lý thuyết trò chơi
- Thiết kế giao diện người dùng hiện đại

Mục tiêu: Giáo dục và giải trí thông qua mô phỏng các lựa chọn chính trị-kinh tế thực tế.

---

## 🤝 Liên Hệ & Hỗ Trợ

- **GitHub**: https://github.com/Eddie0517/MLN_GAME
- **Issues**: Báo cáo lỗi hoặc yêu cầu tính năng
- **Discussions**: Thảo luận về trò chơi

---

**Cảm ơn bạn đã chơi SimSociety 2D! 🎮🌍**

Hãy cố gắng phạt ít nhất một trong bốn kết thúc để hoàn thành trò chơi!

---

*Cập nhật lần cuối: 2026-05-25*
