import pygame
from config import (
    FONT_LARGE, FONT_STATUS, FONT_SMALL, FONT_MINI,
    COLOR_BG, COLOR_ROAD, COLOR_TEXT_LIGHT, COLOR_TEXT_DARK,
    COLOR_GOLD, COLOR_MINT, COLOR_BLUE, COLOR_RED, COLOR_CARD_POLICY
)

class GameGuide:
    """Hệ thống hướng dẫn trò chơi Kỷ Nguyên Tiến Hóa"""
    
    GUIDE_CONTENT = {
        "Cách chơi": [
            "MỤC ĐÍCH TRÒ CHƠI",
            "Đưa bầy người nguyên sơ vượt qua các giai đoạn tiến hóa lịch sử,",
            "cải tiến công cụ lao động để xây dựng xã hội thịnh vượng vĩ đại.",
            "",
            "5 HÌNH THÁI KINH TẾ - XÃ HỘI",
            "• Chương 1: Công xã Nguyên thủy",
            "  Săn bắt - hái lượm, duy trì ngọn lửa sưởi ấm.",
            "• Chương 2: Chiếm hữu Nô lệ",
            "  Sử dụng sức lao động của nô lệ xây dựng kỳ quan đền đài.",
            "• Chương 3: Phong kiến",
            "  Thu thuế điền sản nông nghiệp, mở rộng giao thương hàng hải.",
            "• Chương 4: Xã hội Chủ nghĩa",
            "  Công hữu hóa nhà máy, chăm lo phúc lợi, phát triển công bằng.",
            "• Chương 5: Kỷ nguyên Tri thức & Tự động hóa",
            "  Robot gánh vác việc chân tay, thám hiểm thiên hà xa xôi.",
        ],
        "Điều khiển": [
            "CÁC PHÍM TƯƠNG TÁC CHÍNH",
            "• PHÍM MŨI TÊN hoặc WASD: Di chuyển nhân vật Thị trưởng.",
            "",
            "• ĐỨNG Ở GIỮA ĐƯỜNG (Khu khai thác) + Nhấn [SPACE]:",
            "  Trực tiếp lao động để sản xuất tài nguyên (Lương thực, Quặng, Vàng, Tri thức...)",
            "",
            "• ĐỨNG Ở BÊN TRÁI (Cơ sở hạ tầng) + Nhấn [SPACE]:",
            "  Nâng cấp công cụ cải biến Lực lượng sản xuất (Tiến lên đời tiếp theo).",
            "",
            "• ĐỨNG Ở BÊN PHẢI (Kiến trúc Thượng tầng) + Nhấn [1] hoặc [2]:",
            "  Ban hành sắc lệnh chính trị (Quan hệ sản xuất).",
            "",
            "• ĐỨNG Ở GIỮA PHÍA DƯỚI (Qua năm) + Nhấn [SPACE]:",
            "  Bước sang năm mới, nhận sản lượng tự động và đối mặt Biến cố.",
            "",
            "• KHI XẢY RA BIẾN CỐ LỰA CHỌN:",
            "  Nhấn phím [ A ] hoặc [ B ] trên bàn phím để chọn quyết định.",
            "",
            "• PHÍM KHÁC:",
            "  - G: Mở/Đóng Hướng dẫn này | R: Khởi động lại game khi kết thúc.",
        ],
        "Tài nguyên": [
            "TÀI NGUYÊN ĐỘNG THEO CHƯƠNG",
            "• Chương 1: Lương thực (Đạt 200 để chuyển đời) & Lửa sưởi ấm.",
            "  Chú ý: Nếu lửa tắt (0%), năng suất săn bắt tự động giảm mạnh.",
            "",
            "• Chương 2: Lương thực, Quặng (Ore - cần 100), Vàng (cần 150), Nô lệ.",
            "  Chú ý: Nô lệ sẽ ăn lương thực. Nếu thiếu ăn, họ phản kháng dữ dội.",
            "",
            "• Chương 3: Lương thực, Vàng ngân quỹ (cần 800), Thuế suất (%).",
            "  Chú ý: Thuế thu được tính theo tỷ lệ thu hoạch lúa. Thuế cao dân oán hận.",
            "",
            "• Chương 4: Quỹ Phúc Lợi (Cần 1M đ), Bình đẳng (Cần 90%), Thức ăn.",
            "  Chú ý: Quỹ Phúc Lợi có thể nâng cấp cấp số nhân nhờ công nghiệp xanh.",
            "",
            "• Chương 5: Năng lượng sạch, Tri thức, Chỉ số Văn minh (Đạt 100% để THẮNG).",
        ],
        "Cải cách Đời": [
            "NÂNG CẤP LỰC LƯỢNG SẢN XUẤT",
            "Để chuyển sang thời kỳ tiếp theo, đứng vào ô Trái nhấn SPACE:",
            "",
            "• LÊN ĐỜI II (Chiếm hữu Nô lệ):",
            "  Yêu cầu: Lương thực tích lũy >= 200.",
            "",
            "• LÊN ĐỜI III (Phong kiến):",
            "  Yêu cầu: Quặng đồng/sắt >= 100 và Vàng >= 150.",
            "",
            "• LÊN ĐỜI IV (Xã hội Chủ nghĩa):",
            "  Yêu cầu: Vàng trong ngân khố địa chủ >= 800.",
            "",
            "• LÊN ĐỜI V (Tương lai):",
            "  Đạt tự động khi: Quỹ Phúc Lợi >= 1,000,000 và Bình đẳng >= 90%.",
            "",
            "• CHIẾN THẮNG CUỐI CÙNG:",
            "  Đưa Chỉ số Văn minh tại Chương 5 đạt mốc 100%.",
        ],
        "Sắc lệnh chính": [
            "SÁCH LƯỢC QUAN HỆ SẢN XUẤT",
            "Đứng tại ô Phải bấm phím 1 hoặc 2 để ban hành lệnh tương ứng:",
            "",
            "• ĐỜI I: Tiếp củi giữ Lửa (Tốn food) / Rèn gậy săn bắn (Năng suất +5).",
            "• ĐỜI II: Cưỡng bức lao động (Tăng thu, hại nô lệ) / Phát cháo cơm (Giảm phản kháng).",
            "• ĐỜI III: Tăng thuế suất (Thu nhiều vàng, oán hận tăng) / Đắp đê ngăn lũ.",
            "• ĐỜI IV: Cấp quỹ dân sinh (Tăng bình đẳng) / Thi đua sản xuất (Tăng năng suất).",
            "• ĐỜI V: Hợp nhất mạng lưới (Tăng năng lượng) / Phóng tàu vũ trụ (Văn minh +20%).",
        ],
        "Kết thúc game": [
            "ĐIỀU KIỆN KẾT THÚC VÀ KẾT QUẢ",
            "",
            "1. THẮNG LỢI HOÀN TOÀN: VICTORY",
            "   Đạt 100% Chỉ số Văn minh tại Chương 5.",
            "   Xã hội tự động hóa Solarpunk rực rỡ vươn tới các vì sao.",
            "",
            "2. THẤT BẠI NẠN ĐÓI (Chương 1):",
            "   Để Lương thực rơi về mốc <= 0. Bộ lạc tan rã.",
            "",
            "3. THẤT BẠI NỔI LOẠN (Chương 2, 3, 4):",
            "   Để Chỉ số Phản kháng / Bất ổn xã hội chạm ngưỡng 100%.",
            "   Dân chúng nổi dậy lật đổ nhà cầm quyền.",
        ],
        "Mẹo hay": [
            "CHIẾN LƯỢC TIẾN HÓA THÀNH CÔNG",
            "• Hãy tích cực đứng ở khu vực khai thác ở giữa và nhấn SPACE.",
            "  Lao động trực tiếp sẽ sinh ra tài nguyên nhanh hơn đợi qua năm.",
            "",
            "• Đừng quá nôn nóng lên đời mà bỏ quên lòng dân.",
            "  Hãy dùng các sắc lệnh như Phát cơm (Đời 2), Đắp đê (Đời 3),",
            "  Cấp quỹ (Đời 4) để kéo lòng dân trở lại mức an toàn.",
            "",
            "• Ở Đời 4, việc nâng cấp công cụ Xanh, Điện toán đám mây,",
            "  và Robot AI sẽ nhân sản lượng phúc lợi từ +2,000 lên +500,000 mỗi năm.",
            "  Hãy ưu tiên nâng cấp hạ tầng trước khi trích quỹ cấp dân sinh.",
        ],
    }
    
    def __init__(self):
        self.is_visible = False
        self.current_tab = 0
        self.tab_names = list(self.GUIDE_CONTENT.keys())
        self.guide_rect = pygame.Rect(100, 100, 850, 480)
        self.scroll_offset = 0
        
    def toggle_visibility(self):
        self.is_visible = not self.is_visible
        self.scroll_offset = 0
        
    def next_tab(self):
        self.current_tab = (self.current_tab + 1) % len(self.tab_names)
        self.scroll_offset = 0
        
    def prev_tab(self):
        self.current_tab = (self.current_tab - 1) % len(self.tab_names)
        self.scroll_offset = 0
    
    def draw(self, screen):
        if not self.is_visible:
            return
        
        # Vẽ nền tối mờ
        overlay = pygame.Surface((screen.get_width(), screen.get_height()))
        overlay.set_alpha(220)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        # Vẽ hộp chứa guide
        pygame.draw.rect(screen, COLOR_CARD_POLICY, self.guide_rect, border_radius=10)
        pygame.draw.rect(screen, COLOR_GOLD, self.guide_rect, 3, border_radius=10)
        
        # Tiêu đề
        title = FONT_LARGE.render(" CẨM NANG TIẾN HÓA LỊCH SỬ ", True, COLOR_TEXT_DARK)
        title_rect = title.get_rect(center=(self.guide_rect.centerx, self.guide_rect.y + 20))
        screen.blit(title, title_rect)
        
        # Vẽ các thẻ tab
        tab_y = self.guide_rect.y + 45
        tab_height = 25
        tab_width = self.guide_rect.width // len(self.tab_names)
        
        for i, tab_name in enumerate(self.tab_names):
            tab_x = self.guide_rect.x + (i * tab_width)
            tab_rect = pygame.Rect(tab_x, tab_y, tab_width, tab_height)
            
            if i == self.current_tab:
                pygame.draw.rect(screen, COLOR_GOLD, tab_rect)
                text_color = COLOR_TEXT_DARK
            else:
                pygame.draw.rect(screen, COLOR_ROAD, tab_rect)
                text_color = COLOR_TEXT_LIGHT
            
            tab_text = FONT_SMALL.render(tab_name, True, text_color)
            tab_text_rect = tab_text.get_rect(center=tab_rect.center)
            screen.blit(tab_text, tab_text_rect)
        
        # Vùng chứa nội dung
        content_y = self.guide_rect.y + 80
        content_rect = pygame.Rect(
            self.guide_rect.x + 20,
            content_y,
            self.guide_rect.width - 40,
            self.guide_rect.height - 130
        )
        
        current_content = self.GUIDE_CONTENT[self.tab_names[self.current_tab]]
        
        # Vẽ văn bản cuộn được
        y_offset = content_rect.y - self.scroll_offset
        for line in current_content:
            if y_offset + 20 > screen.get_height() - 70:
                break
            
            if y_offset >= content_rect.y:
                if line.isupper() and len(line) > 3:
                    text_surf = FONT_STATUS.render(line, True, COLOR_BLUE)
                elif line.startswith("•") or line.startswith("✓") or line.startswith("  -"):
                    text_surf = FONT_SMALL.render(line, True, COLOR_TEXT_DARK)
                else:
                    text_surf = FONT_SMALL.render(line, True, COLOR_TEXT_DARK)
                screen.blit(text_surf, (content_rect.x, y_offset))
            
            y_offset += 20
        
        # Gợi ý phím cuộn bên dưới
        info_text = "◄ A / D hoặc Mũi tên trái/phải: Đổi tab  |  ▲ W / S hoặc Mũi tên lên/xuống: Cuộn trang  |  G: Đóng Hướng dẫn"
        info_surf = FONT_MINI.render(info_text, True, COLOR_TEXT_LIGHT)
        screen.blit(info_surf, (self.guide_rect.x + 20, self.guide_rect.y + self.guide_rect.height - 35))
        
    def handle_input(self, keys):
        if not self.is_visible:
            return
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.prev_tab()
            pygame.time.wait(200)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.next_tab()
            pygame.time.wait(200)
        
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.scroll_offset = max(0, self.scroll_offset - 8)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            # Giới hạn cuộn tối đa dựa vào chiều dài nội dung
            current_tab_name = self.tab_names[self.current_tab]
            content_len = len(self.GUIDE_CONTENT[current_tab_name])
            max_scroll = max(0, content_len * 20 - 330)
            self.scroll_offset = min(max_scroll, self.scroll_offset + 8)

    def handle_click(self, mouse_pos):
        """Xử lý sự kiện click chuột vào các tab của cẩm nang"""
        if not self.is_visible:
            return False
            
        tab_y = self.guide_rect.y + 45
        tab_height = 25
        tab_width = self.guide_rect.width // len(self.tab_names)
        
        for i, tab_name in enumerate(self.tab_names):
            tab_x = self.guide_rect.x + (i * tab_width)
            tab_rect = pygame.Rect(tab_x, tab_y, tab_width, tab_height)
            if tab_rect.collidepoint(mouse_pos):
                self.current_tab = i
                self.scroll_offset = 0
                return True
        return False
