import pygame
from config import FONT_STATUS, FONT_SMALL, FONT_MINI, COLOR_ROAD, COLOR_GOLD, COLOR_RED, COLOR_TEXT_DARK, COLOR_TEXT_LIGHT, COLOR_BLUE, COLOR_GOLD_SOFT, COLOR_MINT_SOFT

class UIEngine:
    guide_button_rect = pygame.Rect(970, 25, 60, 30)
    
    @staticmethod
    def wrap_text(text, font, max_width):
        """Ngắt text tự động dựa trên chiều rộng"""
        words = text.split(' ')
        lines = []
        current_line = ""
        
        for word in words:
            test_line = current_line + word + " "
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line.strip())
                current_line = word + " "
        
        if current_line:
            lines.append(current_line.strip())
        
        return lines
    
    @staticmethod
    def draw_progress_bar(screen, x, y, width, height, value, max_value, label_text, bar_color):
        lbl = FONT_SMALL.render(f"{label_text}: {value}%", True, COLOR_TEXT_DARK if y > 120 else (200, 200, 200))
        screen.blit(lbl, (x, y - 18))
        
        pygame.draw.rect(screen, COLOR_ROAD, (x, y, width, height), border_radius=3)
        fill_width = int((value / max_value) * width)
        fill_width = max(0, min(width, fill_width))
        pygame.draw.rect(screen, bar_color, (x, y, fill_width, height), border_radius=3)

    @staticmethod
    def draw_hud(screen, eco_state):
        # 1. HIỂN THỊ HỆ TƯ TƯỞNG (Góc trái trên cùng)
        lbl_ideo = FONT_STATUS.render(f"Hệ Tư Tưởng: {eco_state.current_ideology}", True, COLOR_BLUE)
        screen.blit(lbl_ideo, (25, 25))

        # 2. VẼ CÁC THANH TIẾN TRÌNH PHE PHÁI (Căn giữa Top Bar)
        UIEngine.draw_progress_bar(screen, 380, 25, 140, 12, eco_state.worker_support, 100, "Giai cấp Công nhân", (0, 200, 255))
        UIEngine.draw_progress_bar(screen, 380, 65, 140, 12, eco_state.capitalist_support, 100, "Giới Chủ Tư Bản", (255, 100, 100))

        # 3. SẮP XẾP LẠI NGÂN SÁCH & NĂNG SUẤT (Dùng màu dịu mắt mới, thẳng hàng góc phải)
        import config
        lbl_money = FONT_STATUS.render(f"Ngân sách: {eco_state.gold} Vàng", True, config.COLOR_GOLD_SOFT)
        lbl_income = FONT_STATUS.render(f"Năng suất: +{eco_state.income}/năm", True, config.COLOR_MINT_SOFT)
        screen.blit(lbl_money, (760, 25))
        screen.blit(lbl_income, (760, 60))
        
        # Phần vẽ Bản tin đã được di dời sang Layer 2 của main.py để tối ưu kiến trúc đồ họa
    
    @staticmethod
    def draw_guide_button(screen):
        """Vẽ nút Guide ở góc phải trên cùng"""
        button_rect = UIEngine.guide_button_rect
        
        # Vẽ nền nút
        pygame.draw.rect(screen, COLOR_GOLD, button_rect, border_radius=5)
        pygame.draw.rect(screen, COLOR_RED, button_rect, 2, border_radius=5)
        
        # Vẽ text nút
        button_text = FONT_SMALL.render("Guide", True, COLOR_TEXT_DARK)
        text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, text_rect)
        
        return button_rect