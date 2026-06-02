# Kỷ Nguyên Tiến Hóa (The Age of Evolution)
### *Mô Phỏng Biện Chứng Lịch Sử & Các Hình Thái Kinh Tế - Xã Hội*

**Kỷ Nguyên Tiến Hóa** là một trò chơi mô phỏng phát triển xã hội được xây dựng bằng Python và Pygame. Người chơi sẽ vào vai Thị trưởng/Người dẫn dắt xã hội đưa loài người nguyên thủy vượt qua 5 hình thái kinh tế - xã hội lịch sử, cải tiến lực lượng sản xuất và thiết lập quan hệ sản xuất phù hợp để vươn tới đỉnh cao văn minh Solarpunk.

---

## 🎨 Giao diện & Hình ảnh mới
Giao diện trên đỉnh (HUD) được tinh chỉnh hiện đại và đối xứng 3 hàng thông tin trực quan:
* **Hàng 1**: Chương lịch sử hiện tại và Nút xem cẩm nang **Guide**.
* **Hàng 2**: Hệ tư tưởng xã hội hiện tại, chỉ số tài nguyên động và **Năm thứ**.
* **Hàng 3**: Thanh trạng thái tiến trình (Độ lớn ngọn lửa / Độ bất ổn / Độ phản kháng / Tiến trình văn minh).

---

## 🎮 Hướng dẫn điều khiển
### Di chuyển
* Sử dụng các phím **WASD** hoặc **Mũi tên** để di chuyển nhân vật.

### Tương tác các Khu vực (Đứng vào ô tương ứng trên bản đồ)
1. **Đứng ở giữa đường (Khu vực khai thác)**:
   * Nhấn giữ hoặc bấm liên tục **[SPACE]** để trực tiếp lao động sản xuất tài nguyên (Lương thực, Quặng, Vàng, Tri thức...).
2. **Đứng ở bên trái (Thẻ Cơ sở hạ tầng)**:
   * Nhấn **[SPACE]** để nâng cấp cải tiến công cụ và hạ tầng (Lực lượng sản xuất) khi đủ điều kiện.
3. **Đứng ở bên phải (Thẻ Kiến trúc Thượng tầng)**:
   * Nhấn phím **[1]** hoặc **[2]** để ban hành các sắc lệnh chính trị (Quan hệ sản xuất).
4. **Đứng ở giữa phía dưới (Nút Qua năm)**:
   * Nhấn **[SPACE]** để bước sang năm mới, nhận sản lượng tự động và đối mặt với các Biến cố ngẫu nhiên.

### Sự kiện biến cố
* Khi xuất hiện hộp thoại Biến cố lịch sử, nhấn phím **[ A ]** hoặc **[ B ]** trên bàn phím để đưa ra quyết định.

### Cẩm nang Hướng dẫn (Guide)
* Nhấn **[ G ]** hoặc **[ ESC ]** để Mở / Đóng.
* Khi cẩm nang đang mở:
  * **Click chuột trái trực tiếp** vào các tab cẩm nang hoặc dùng phím **A/D (Trái/Phải)** để chuyển trang.
  * Nhấn giữ phím **W/S (Lên/Xuống)** để cuộn nội dung.

---

## 📜 5 Chương Tiến Hóa Lịch Sử
1. **Chương I: Công xã Nguyên thủy**
   * *Nhiệm vụ*: Tích lũy đủ **200 Lương thực**.
   * *Thách thức*: Ngọn lửa sưởi ấm giảm dần qua mỗi năm, lửa tắt sẽ làm giảm mạnh năng suất săn bắt tự động.
2. **Chương II: Chiếm hữu Nô lệ**
   * *Nhiệm vụ*: Thu thập **100 Quặng** và **150 Vàng**.
   * *Thách thức*: Quản lý lương thực nuôi nô lệ. Nếu thiếu đói, độ phản kháng tăng lên. Chạm mốc 100% sẽ xảy ra khởi nghĩa lật đổ chế độ (Thất bại).
3. **Chương III: Phong kiến**
   * *Nhiệm vụ*: Thu hoạch **800 Vàng** thuế.
   * *Thách thức*: Điều chỉnh thuế suất nông nghiệp phù hợp. Thuế cao tăng ngân sách nhanh nhưng đẩy độ bất ổn nông dân lên cao.
4. **Chương IV: Xã hội Chủ nghĩa**
   * *Nhiệm vụ*: Tích lũy **1.000.000đ Quỹ Phúc lợi** và giữ chỉ số **Bình đẳng >= 90%**.
   * *Thách thức*: Phân chia phúc lợi công cộng và thi đua sản xuất công nghiệp xanh cân bằng lòng dân.
5. **Chương V: Kỷ nguyên Tri thức & Tự động hóa (Solarpunk)**
   * *Nhiệm vụ*: Nghiên cứu năng lượng sạch, tri thức và tăng **Chỉ số Văn minh đạt 100%** để Chiến thắng.
   * *Đặc trưng*: Không còn áp bức, robot gánh vác mọi việc chân tay, xã hội phát triển cực thịnh.

---

## 🛠️ Các cải tiến kỹ thuật & hiệu năng gần đây
* **Cơ chế Image Caching**: Đã tối ưu hóa bộ nhớ đệm hình ảnh cho các hình ảnh hạ tầng chương (`intro_chapter1` -> `5`). Tránh việc đọc tệp từ đĩa cứng và co giãn (scale) liên tục mỗi khung hình, giúp game vận hành mượt mà ở **60 FPS** ổn định.
* **Hỗ trợ định dạng ảnh đa dạng**: Game tự động quét và load các ảnh với các đuôi `.png`, `.jpg`, `.jpeg`, `.webp` (cả chữ thường và chữ hoa) giúp người chơi dễ dàng thêm ảnh mà không cần chuyển đổi định dạng.
* **Bộ hồi chiêu Không chặn (Non-blocking Cooldowns)**: Thay thế toàn bộ các lệnh đứng hình `pygame.time.wait()` bằng bộ đếm hồi chiêu theo số khung hình trong vòng lặp `update`. Giờ đây nhân vật di chuyển không còn bị giật lag khi đang khai thác hay bấm nút.

---

## 🚀 Hướng dẫn chạy game
1. Cài đặt thư viện Pygame:
   ```bash
   pip install pygame
   ```
2. Khởi chạy trò chơi bằng lệnh:
   ```bash
   python main.py
   ```
