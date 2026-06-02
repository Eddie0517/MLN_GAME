import pygame
from config import FONT_STATUS, FONT_SMALL, FONT_MINI, FONT_LARGE, COLOR_ROAD, COLOR_GOLD, COLOR_RED, COLOR_TEXT_DARK, COLOR_TEXT_LIGHT, COLOR_BLUE, COLOR_GOLD_SOFT, COLOR_MINT_SOFT

class UIEngine:
    guide_button_rect = pygame.Rect(965, 15, 60, 30)
    
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
        lbl = FONT_SMALL.render(f"{label_text}: {value}%", True, COLOR_TEXT_DARK if y > 120 else (220, 220, 220))
        screen.blit(lbl, (x, y - 18))
        
        pygame.draw.rect(screen, COLOR_ROAD, (x, y, width, height), border_radius=3)
        if max_value > 0:
            fill_width = int((value / max_value) * width)
        else:
            fill_width = 0
        fill_width = max(0, min(width, fill_width))
        pygame.draw.rect(screen, bar_color, (x, y, fill_width, height), border_radius=3)

    @staticmethod
    def draw_hud(screen, eco_state):
        import config
        # 1. Chọn màu sắc chủ đề dựa theo chương
        ch_colors = {
            1: config.COLOR_CH1,
            2: config.COLOR_CH2,
            3: config.COLOR_CH3,
            4: config.COLOR_CH4,
            5: config.COLOR_CH5
        }
        theme_color = ch_colors.get(eco_state.tech_level, config.COLOR_GOLD)
        
        # Vẽ thanh màu mỏng trên đỉnh
        pygame.draw.rect(screen, theme_color, (0, 0, screen.get_width(), 8))
        
        # Hiển thị chương hiện tại (Hàng 1)
        lbl_ch = FONT_LARGE.render(f"CHƯƠNG {eco_state.tech_level}: {eco_state.get_chapter_name().upper()}", True, COLOR_GOLD_SOFT)
        screen.blit(lbl_ch, (25, 18))
        
        # Dòng phụ mô tả hệ tư tưởng (Hàng 2)
        lbl_ideo = FONT_MINI.render(f"Hệ tư tưởng xã hội: {eco_state.current_ideology}", True, (180, 180, 180))
        screen.blit(lbl_ideo, (25, 52))

        # Hiển thị tài nguyên phụ tại hàng 2
        if eco_state.tech_level == 1:
            lbl_res = FONT_STATUS.render(f"Lương thực trữ: {eco_state.food} quả", True, config.COLOR_GOLD_SOFT)
        elif eco_state.tech_level == 2:
            lbl_res = FONT_STATUS.render(f"Vàng: {eco_state.gold} | Quặng: {eco_state.ore} | Nô lệ: {eco_state.slaves}", True, config.COLOR_GOLD_SOFT)
        elif eco_state.tech_level == 3:
            lbl_res = FONT_STATUS.render(f"Ngân quỹ: {eco_state.gold} Vàng", True, config.COLOR_GOLD_SOFT)
        elif eco_state.tech_level == 4:
            lbl_res = FONT_STATUS.render(f"Quỹ Phúc Lợi: {eco_state.welfare_fund:,}đ", True, config.COLOR_MINT_SOFT)
        elif eco_state.tech_level == 5:
            lbl_res = FONT_STATUS.render(f"Năng lượng: {eco_state.clean_energy} | Tri thức: {eco_state.knowledge}", True, config.COLOR_MINT_SOFT)
        
        screen.blit(lbl_res, (420, 48))
            
        # Hiển thị Năm thứ tại Hàng 2
        lbl_year = FONT_STATUS.render(f"Năm thứ: {eco_state.turn}", True, COLOR_TEXT_LIGHT)
        screen.blit(lbl_year, (850, 48))

        # 2. VẼ THANH TIẾN TRÌNH (Hàng 3)
        unrest = eco_state.upheaval_tension
        if eco_state.tech_level == 1:
            # Chương 1: Hiện mức lửa sưởi ấm
            UIEngine.draw_progress_bar(screen, 25, 96, 350, 12, eco_state.fire, 100, "Ngọn Lửa Sưởi Ấm", config.COLOR_GOLD)
        elif eco_state.tech_level == 5:
            # Chương 5: Hiện mức văn minh chiến thắng
            UIEngine.draw_progress_bar(screen, 25, 96, 350, 12, eco_state.civilization_level, 100, "Tiến Trình Văn Minh Đỉnh Cao", config.COLOR_MINT)
        else:
            # Đời 2, 3, 4: Hiện phản kháng/bất ổn
            label = "Độ Phản Kháng Nô Lệ" if eco_state.tech_level == 2 else ("Độ Bất Ổn Nông Dân" if eco_state.tech_level == 3 else "Độ Bất Ổn Xã Hội")
            UIEngine.draw_progress_bar(screen, 25, 96, 350, 12, unrest, 100, label, config.COLOR_RED)
        
    @staticmethod
    def draw_guide_button(screen):
        """Vẽ nút Guide ở góc phải trên cùng"""
        button_rect = UIEngine.guide_button_rect
        pygame.draw.rect(screen, COLOR_GOLD, button_rect, border_radius=5)
        pygame.draw.rect(screen, COLOR_RED, button_rect, 2, border_radius=5)
        
        button_text = FONT_SMALL.render("Guide", True, COLOR_TEXT_DARK)
        text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, text_rect)
        return button_rect