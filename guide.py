import pygame
from config import (
    FONT_LARGE, FONT_STATUS, FONT_SMALL, FONT_MINI,
    COLOR_BG, COLOR_ROAD, COLOR_TEXT_LIGHT, COLOR_TEXT_DARK,
    COLOR_GOLD, COLOR_MINT, COLOR_BLUE, COLOR_RED, COLOR_CARD_POLICY
)

class GameGuide:
    """Hệ thống hướng dẫn trò chơi với nội dung chi tiết"""
    
    # Nội dung guide được chia thành các tab
    GUIDE_CONTENT = {
        "Cách chơi": [
            "MỤC ĐÍCH TRÒ CHƠI",
            "Điều hành đất nước thông qua các quyết định chính sách",
            "và nâng cấp công nghệ để đạt tới Kỷ nguyên Utopia.",
            "",
            "CÁC GIAI ĐOẠN PHÁT TRIỂN",
            "• Giai đoạn 1: Nông nghiệp (Công nghiệp hóa)",
            "  Tích lũy 60 Vàng → Nâng cấp tại [CƠ SỞ HẠ TẦNG]",
            "",
            "• Giai đoạn 2: Công nghiệp (Kỷ nguyên AI)",
            "  Tích lũy 120 Vàng → Nâng cấp tại [CƠ SỞ HẠ TẦNG]",
            "",
            "• Giai đoạn 3: Kỷ nguyên AI (Utopia)",
            "  Đạt 250 Vàng + Lòng dân cân bằng → Chiến thắng!",
        ],
        "Điều khiển": [
            "CÁC PHÍM ĐIỀU KHIỂN",
            "• PHÍM MŨI TÊN: Di chuyển nhân vật",
            "• SPACE: Tương tác tại vị trí hiện tại",
            "  - Ở [CƠ SỞ HẠ TẦNG]: Nâng cấp công nghệ",
            "  - Ở [LUẬT PHÁP]: Tương tác với chính sách",
            "  - Ở [QUA NĂM]: Bước sang năm tiếp theo",
            "",
            "• PHÍM 1: Ban hành Thuế AI (tại ô Thượng tầng)",
            "• PHÍM 2: Ban hành Luật Phúc Lợi (tại ô Thượng tầng)",
            "• R: Khởi động lại game (khi game over)",
            "• G: Mở/Đóng guide (hướng dẫn này)",
        ],
        "Tài nguyên": [
            "CÁC TÀI NGUYÊN CHÍNH",
            "1. VÀNG (Gold):",
            "   - Tài nguyên chính của quốc gia",
            "   - Dùng để nâng cấp công nghệ",
            "   - Nhận thêm mỗi năm từ năng suất",
            "",
            "2. LÒNG DÂN CÁC PHE PHÁI:",
            "   - Công nhân (Xanh): Ủng hộ các chính sách công nhân",
            "   - Giới chủ (Đỏ): Ủng hộ các chính sách kinh tế",
            "   - Cần giữ lòng dân cân bằng để tránh sụp đổ",
            "",
            "3. NĂNG SUẤT:",
            "   - Lượng Vàng nhận được mỗi năm",
            "   - Tăng khi nâng cấp công nghệ",
            "   - Phụ thuộc vào hệ tư tưởng hiện tại",
        ],
        "Chính sách": [
            "CÁC CHÍNH SÁCH KHUYẾT THÊ",
            "",
            "1. THUẾ AI (Phím 1):",
            "   - Yêu cầu: Ở giai đoạn Kỷ nguyên AI trở lên",
            "   - Tác dụng: +60 Vàng ngay lập tức",
            "   - Phản ứng: Giới chủ tăng 5%, Công nhân giảm 5%",
            "   - Chú ý: Không được dùng ở giai đoạn Nông nghiệp!",
            "",
            "2. LUẬT PHÚC LỢI CÔNG NHÂN (Phím 2):",
            "   - Tác dụng: Công nhân +8%, năng suất -5",
            "   - Hiệu quả: Ổn định lòng dân công nhân",
            "   - Chi phí: Giảm năng suất mỗi năm",
            "   - Khi nào dùng: Khi lòng dân công nhân quá thấp",
            "",
            "3. NÂNG CẤP CƠ SỞ HẠ TẦNG (SPACE):",
            "   - Yêu cầu: Đủ Vàng theo giai đoạn",
            "   - Tác dụng: Nâng công nghệ lên cấp tiếp theo",
            "   - Tăng năng suất hàng năm",
        ],
        "Hệ tư tưởng": [
            "CÁC HỆ TƯ TƯỞNG VÀ TÍNH CHẤT",
            "",
            "1. CHỦ NGHĨA TƯƠI MỚI (Early):",
            "   - Năng suất: Bình thường",
            "   - Lòng dân: Cân bằng",
            "",
            "2. TƯ BẢN CÔNG NGHIỆP:",
            "   - Năng suất: Cao (Giới chủ hưởng lợi)",
            "   - Lòng dân: Giới chủ ↑, Công nhân ↓",
            "",
            "3. XÃ HỘI CHỦ NGHĨA KHOA HỌC:"
            "   - Năng suất: Bình thường (Công nhân hưởng lợi)",
            "   - Lòng dân: Công nhân ↑, Giới chủ ↓",
            "",
            "4. CHỦ NGHĨA ĐỘC TÀI AI (Technocracy):",
            "   - Năng suất: Rất cao (Máy tính quyết định)",
            "   - Lòng dân: Cả hai phe phái giảm",
            "",
            "5. UTOPIA TƯ TƯ TƯỞNG:",
            "   - Năng suất: Cực cao",
            "   - Lòng dân: Cả hai phe phái hài lòng",
        ],
        "Kết thúc trò chơi": [
            "4 KẾT THÚC CHÍNH",
            "",
            "1. ENDING 1: KỶ NGUYÊN HOÀNG KIM (Utopia AI)",
            "   Điều kiện: Tech Lv3 + Gold ≥250 + Lòng dân ≥80%",
            "   Kết quả: CHIẾN THẮNG - Xã hội hoàn hảo",
            "",
            "2. ENDING 2: ĐỘC TÀI CÔNG NGHỆ (Cyberpunk)",
            "   Điều kiện: Tech Lv3 + Hệ tư tưởng Technocracy",
            "   Kết quả: THUA - Người giàu kiểm soát tất cả",
            "",
            "3. ENDING 3: CÁCH MẠNG LAO ĐỘNG",
            "   Điều kiện: Sức căng cách mạng ≥30",
            "   Kết quả: THUA - Công nhân lật đổ chế độ",
            "",
            "4. ENDING 4: SỤP ĐỔ TOÀN DIỆN",
            "   Điều kiện: Lòng dân <20% hoặc Gold < -40",
            "   Kết quả: THUA - Nhà nước tan rã",
        ],
        "Mẹo chơi": [
            "CÁC MẸO VÀ CHIẾN LƯỢC",
            "",
            "1. GIAI ĐOẠN SỚM:",
            "   • Cân bằng lòng dân các phe phái",
            "   • Tích lũy Vàng ổn định, không vội nâng cấp",
            "   • Tránh ban hành quá nhiều chính sách mạnh",
            "",
            "2. GIAI ĐOẠN GIỮA (Công nghiệp):",
            "   • Dùng Luật Phúc Lợi khi lòng dân công nhân thấp",
            "   • Tiếp tục tích lũy Vàng",
            "   • Chuẩn bị cho giai đoạn AI",
            "",
            "3. GIAI ĐOẠN CUỐI (AI):",
            "   • Bật Thuế AI để tăng Vàng nhanh",
            "   • Dùng Phúc Lợi cân bằng lòng dân",
            "   • Đạt đủ Vàng và lòng dân để chiến thắng",
            "",
            "4. TRÁNH CÁC SAI LẦM:",
            "   Không dùng Thuế AI ở giai đoạn sớm",
            "   Không để lòng dân một phe phái quá thấp",
            "   Không quên cân bằng các chỉ số",
        ],
    }
    
    def __init__(self):
        self.is_visible = False
        self.current_tab = 0
        self.tab_names = list(self.GUIDE_CONTENT.keys())
        self.guide_rect = pygame.Rect(100, 100, 850, 480)
        self.scroll_offset = 0
        self.max_scroll = 0
        
    def toggle_visibility(self):
        """Bật/Tắt hiển thị guide"""
        self.is_visible = not self.is_visible
        self.scroll_offset = 0
        
    def next_tab(self):
        """Sang tab tiếp theo"""
        self.current_tab = (self.current_tab + 1) % len(self.tab_names)
        self.scroll_offset = 0
        
    def prev_tab(self):
        """Quay lại tab trước"""
        self.current_tab = (self.current_tab - 1) % len(self.tab_names)
        self.scroll_offset = 0
    
    def draw(self, screen):
        """Vẽ guide lên màn hình"""
        if not self.is_visible:
            return
        
        # Vẽ nền mờ
        overlay = pygame.Surface((screen.get_width(), screen.get_height()))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        # Vẽ hộp guide
        pygame.draw.rect(screen, COLOR_CARD_POLICY, self.guide_rect, border_radius=10)
        pygame.draw.rect(screen, COLOR_GOLD, self.guide_rect, 3, border_radius=10)
        
        # Vẽ tiêu đề
        title = FONT_LARGE.render(f" HƯỚNG DẪN CHƠI ", True, COLOR_TEXT_DARK)
        title_rect = title.get_rect(center=(self.guide_rect.centerx, self.guide_rect.y + 20))
        screen.blit(title, title_rect)
        
        # Vẽ các tab
        tab_y = self.guide_rect.y + 45
        tab_height = 25
        tab_width = self.guide_rect.width // len(self.tab_names)
        
        for i, tab_name in enumerate(self.tab_names):
            tab_x = self.guide_rect.x + (i * tab_width)
            tab_rect = pygame.Rect(tab_x, tab_y, tab_width, tab_height)
            
            # Highlight tab hiện tại
            if i == self.current_tab:
                pygame.draw.rect(screen, COLOR_GOLD, tab_rect)
                text_color = COLOR_TEXT_DARK
            else:
                pygame.draw.rect(screen, COLOR_ROAD, tab_rect)
                text_color = COLOR_TEXT_LIGHT
            
            tab_text = FONT_SMALL.render(tab_name, True, text_color)
            tab_text_rect = tab_text.get_rect(center=tab_rect.center)
            screen.blit(tab_text, tab_text_rect)
        
        # Vẽ nội dung guide
        content_y = self.guide_rect.y + 80
        content_rect = pygame.Rect(
            self.guide_rect.x + 10,
            content_y,
            self.guide_rect.width - 20,
            self.guide_rect.height - 110
        )
        
        # Lấy nội dung tab hiện tại
        current_content = self.GUIDE_CONTENT[self.tab_names[self.current_tab]]
        
        # Vẽ nội dung
        y_offset = content_rect.y - self.scroll_offset
        for line in current_content:
            if y_offset + 20 > screen.get_height() - 50:
                break
            
            if y_offset >= content_rect.y:
                # Chọn màu và font dựa trên nội dung
                if line.startswith("【"):
                    text = FONT_STATUS.render(line, True, COLOR_BLUE)
                elif line.startswith("•") or line.startswith("✓") or line.startswith("✗"):
                    text = FONT_SMALL.render(line, True, COLOR_TEXT_DARK)
                elif line.startswith("1.") or line.startswith("2.") or line.startswith("3.") or line.startswith("4.") or line.startswith("5."):
                    text = FONT_STATUS.render(line, True, COLOR_BLUE)
                else:
                    text = FONT_SMALL.render(line, True, COLOR_TEXT_DARK)
                
                screen.blit(text, (content_rect.x + 5, y_offset))
            
            y_offset += 18
        
        # Vẽ thông tin điều khiển ở dưới
        info_text = [
            "◄ Mũi tên trái/phải hoặc A/D: Chuyển tab",
            "Lên/xuống hoặc W/S: Cuộn nội dung",
            "G: Đóng guide",
        ]
        
        info_y = screen.get_height() - 65
        for i, info in enumerate(info_text):
            info_surface = FONT_MINI.render(info, True, COLOR_TEXT_LIGHT)
            screen.blit(info_surface, (self.guide_rect.x + 10, info_y + (i * 18)))
        
    def handle_input(self, keys):
        """Xử lý input khi guide đang mở"""
        if not self.is_visible:
            return
        
        # Chuyển tab
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.prev_tab()
            pygame.time.wait(200)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.next_tab()
            pygame.time.wait(200)
        
        # Cuộn nội dung
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.scroll_offset = max(0, self.scroll_offset - 20)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.scroll_offset += 20
