import pygame
import sys
import random
from config import *
from player import Player
from economy import EconomyState
from policy import PolicyManager
from events import EventEngine
from ui import UIEngine

class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("SimSociety 2D: He Thong Mo Phong Bien Chung 4.5")
        self.clock = pygame.time.Clock()
        self.is_fullscreen = False
        self.player = Player()
        self.eco = EconomyState()
        self.policy_box = PolicyManager()
        self.event_system = EventEngine()

        # Căn chỉnh lại tọa độ vùng bấm nút Qua Năm để vừa khít với con đường trung tâm
        self.zone_next_turn = pygame.Rect(412, 570, 220, 50)
        self.game_over_msg = ""
        self.current_hint = ""
        self.running = True

        # KHỞI TẠO DANH SÁCH HẠT KHÓI Ở ĐÂY ĐỂ TRÁNH LỖI ATTRIBUTEERROR
        self.smoke_particles = []

    def check_emergent_endings(self):
        """Cải tiến kiểm tra Ending dựa trên động năng Quán tính Lịch sử tích lũy"""
        avg_support = self.eco.get_average_support()
        
        # ĐẶT ĐIỀU KIỆN SỤP ĐỔ (ENDING 4) LÊN ƯU TIÊN HÀNG ĐẦU
        if avg_support <= 20 or self.eco.gold < -40:
            self.game_over_msg = "ENDING 4: SỤP ĐỔ TOÀN DIỆN (Society Collapse) - Thất bại trong điều hòa mâu thuẫn chính trị."
            self.eco.history_timeline.append("KẾT THÚC: Nhà nước tan rã hoàn toàn do khủng hoảng cực hạn.")
        elif self.eco.tech_level == 3 and avg_support >= 80 and self.eco.gold >= 250:
            self.game_over_msg = "ENDING 1: KỶ NGUYÊN HOÀNG KIM (Utopia AI) - Xã hội phát triển tối ưu toàn diện!"
            self.eco.history_timeline.append("KẾT THÚC: Đạt đến hình thái Utopia xã hội hòa hợp.")
        elif self.eco.tech_level == 3 and self.eco.current_ideology == "Chủ Nghĩa Độc Tài AI (Technocracy)":
            self.game_over_msg = "ENDING 2: ĐỘC TÀI CÔNG NGHỆ (Cyberpunk Dictatorship) - Giới chủ dùng AI kiểm soát xã hội."
            self.eco.history_timeline.append("KẾT THÚC: Quốc gia biến thành xã hội Cyberpunk phân hóa.")
        elif self.eco.revolution_tension >= 30: 
            self.game_over_msg = "ENDING 3: CÁCH MẠNG LAO ĐỘNG (Socialist Revolution) - Công nhân lật đổ ách áp bức của giới chủ!"
            self.eco.history_timeline.append("KẾT THÚC: Cách mạng vô sản bùng nổ giành chính quyền thành công.")

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            # --- BẮT SỰ KIỆN F11 CHUYỂN ĐỔI MÀN HÌNH ---
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    self.is_fullscreen = not self.is_fullscreen
                    if self.is_fullscreen:
                        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
                    else:
                        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  
        
        keys = pygame.key.get_pressed()
        
        # Nếu đã End Game, chỉ bắt duy nhất sự kiện bấm nút R để Reset trò chơi
        if self.game_over_msg:
            if keys[pygame.K_r]: 
                self.__init__()
            return

        self.player.move(keys)
        p_rect = self.player.get_rect()
        on_infra = p_rect.colliderect(self.policy_box.zone_infra)
        on_policy = p_rect.colliderect(self.policy_box.zone_policy)
        on_turn = p_rect.colliderect(self.zone_next_turn)

        # Thanh hướng dẫn nhiệm vụ chiến lược động linh hoạt
        self.current_hint = "NHIỆM VỤ: "
        if self.eco.tech_level == 1:
            if self.eco.gold < 60: self.current_hint += f"Tích lũy đủ 60 Vàng (Hiện có: {self.eco.gold}) để lên đời Công nghiệp. Đứng vào ô hồng để Qua năm."
            else: self.current_hint += "Đủ tiền! Hãy sang ô [CƠ SỞ HẠ TẦNG] bên trái và nhấn SPACE để tiến lên Công nghiệp hóa."
        elif self.eco.tech_level == 2:
            if self.eco.gold < 120: self.current_hint += f"Tích lũy 120 Vàng (Có: {self.eco.gold}) nâng lên AI. Đừng quên ấn phím 2 ở ô Thượng tầng để bật Luật Phúc Lợi cứu lòng dân!"
            else: self.current_hint += "Đủ điều kiện! Hãy sang ô [CƠ SỞ HẠ TẦNG] bên trái nhấn SPACE để tiến thẳng lên Kỷ nguyên AI."
        elif self.eco.tech_level == 3:
            if not self.policy_box.policies[0].is_activated: self.current_hint += "Kinh tế số hoàn thiện! Sang ô Thượng tầng nhấn phím 1 để bật Thuế AI nhằm thu siêu lợi nhuận."
            else: self.current_hint += f"Đang hướng tới Utopia. Hãy cày Ngân sách >= 250 (Có: {self.eco.gold}) và cân bằng Lòng dân phe phái ổn định!"

        if on_infra:
            self.current_hint = "THAO TÁC: Nhấn phím [SPACE] để tiến hành nâng cấp Cơ sở Hạ tầng Kinh tế."
            if keys[pygame.K_SPACE]:
                self.policy_box.execute_infra_upgrade(self.eco)
                pygame.time.wait(200)
        elif on_policy:
            self.current_hint = "THAO TÁC: Nhấn phím [1] để ban hành Thuế AI  |  Nhấn phím [2] để ban hành Luật Phúc Lợi Công Nhân."
            if keys[pygame.K_1]:
                res = self.policy_box.execute_policy_by_id("P1", self.eco)
                if res == "CRISIS_TAX":
                    self.game_over_msg = "KHỦNG HOẢNG BIỆN CHỨNG: Ban hành Luật Thuế Số quá nôn nóng khi hạ tầng thô sơ!"
                    self.eco.history_timeline.append("Năm 1: Thất bại do phá vỡ quy luật biện chứng khách quan.")
                pygame.time.wait(200)
            if keys[pygame.K_2]:
                self.policy_box.execute_policy_by_id("P2", self.eco)
                pygame.time.wait(200)
        elif on_turn:
            self.current_hint = "THAO TÁC: Nhấn phím [SPACE] để bước sang năm lịch sử tiếp theo và nhận tiền sản lượng."
            if keys[pygame.K_SPACE]:
                self.eco.process_next_turn()
                self.event_system.trigger_annual_event(self.eco)
                pygame.time.wait(250)

    def update(self):
        # Chỉ cập nhật kiểm tra Ending khi game đang chạy bình thường
        if not self.game_over_msg:
            self.player.animation_timer += 0.08
            self.check_emergent_endings()

    def render(self):
        """Tái cấu trúc đồ họa: Tạo hai thẻ bài đối xứng cao cấp có hình minh họa bo góc"""
        
        # ==========================================================
        # 1. LỚP PHÔNG NỀN VÀ ĐƯỜNG LỘ TRUNG TÂM (VẼ DƯỚI CÙNG - LAYER 0)
        # ==========================================================
        current_w, current_h = self.screen.get_size()
        self.screen.fill((210, 206, 196)) # Tông nền xám xi măng ấm
        
        # Vẽ khung nền xám của thanh bảng điều khiển phía trên (HUD) cố định ở đỉnh màn hình
        pygame.draw.rect(self.screen, COLOR_ROAD, (0, 0, current_w, 125))
        pygame.draw.rect(self.screen, COLOR_GOLD, (0, 121, current_w, 4))
        
        # Con đường lộ dọc chính giữa
        pygame.draw.rect(self.screen, (75, 80, 85), (current_w//2 - 80, 125, 160, current_h - 125))
        
        # Vạch kẻ đường đứt đoạn màu trắng chạy dọc sát theo chiều cao thực tế
        for y_line in range(130, current_h, 40):
            pygame.draw.rect(self.screen, (240, 240, 240), (current_w//2 - 3, y_line, 6, 20))

        # Trợ giúp vẽ ảnh bo góc nội bộ
        def blit_rounded_image(target_screen, image_path, rect, radius):
            try:
                img = pygame.image.load(image_path).convert_alpha()
                img = pygame.transform.scale(img, (rect.width, rect.height))
                mask = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
                pygame.draw.rect(mask, (255, 255, 255, 255), (0, 0, rect.width, rect.height), border_radius=radius)
                img.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
                target_screen.blit(img, (rect.x, rect.y))
            except Exception as e:
                pygame.draw.rect(target_screen, (170, 175, 180), rect, border_radius=radius)
                import config
                err_txt = config.FONT_MINI.render("[Thiếu ảnh minh họa]", True, (50, 50, 50))
                target_screen.blit(err_txt, (rect.x + rect.width//2 - err_txt.get_width()//2, rect.y + rect.height//2 - 6))

        # ==========================================================
        # 2. LỚP THẺ BÀI ĐỐI XỨNG HAI BÊN (LAYER 1)
        # ==========================================================
        
        # --- THẺ BÀI BÊN TRÁI: CƠ SỞ HẠ TẦNG ---
        self.policy_box.zone_infra.x = 40
        self.policy_box.zone_infra.y = 145
        self.policy_box.zone_infra.width = 340
        self.policy_box.zone_infra.height = 420  
        infra_rect = self.policy_box.zone_infra
        
        pygame.draw.rect(self.screen, (40, 40, 45), (infra_rect.x + 8, infra_rect.y + 8, infra_rect.width, infra_rect.height), border_radius=12)
        pygame.draw.rect(self.screen, (245, 242, 235), infra_rect, border_radius=12)
        pygame.draw.rect(self.screen, COLOR_TEXT_DARK, infra_rect, 3, border_radius=12)
        
        title_infra = FONT_LARGE.render(f"CƠ SỞ HẠ TẦNG (Cấp {self.eco.tech_level})", True, COLOR_TEXT_DARK)
        self.screen.blit(title_infra, (infra_rect.x + infra_rect.width//2 - title_infra.get_width()//2, infra_rect.y + 15))
        
        infra_img_rect = pygame.Rect(infra_rect.x + 15, infra_rect.y + 50, infra_rect.width - 30, 180)
        pygame.draw.rect(self.screen, COLOR_TEXT_DARK, infra_img_rect, 2, border_radius=8) 
        blit_rounded_image(self.screen, r"C:\Users\Khang\OneDrive\Desktop\GAME_MLN\Fábrica_Industrial_Gratuita_Com_Chaminé_PNG___Industrial__Fábrica__Fumaça_PNG_Imagem_para_download_gratuito-removebg-preview.png", infra_img_rect, 8)  
        
        sub_infra = FONT_MED.render(f"Cơ sở hạ tầng (Cấp {self.eco.tech_level})", True, COLOR_TEXT_DARK)
        self.screen.blit(sub_infra, (infra_rect.x + infra_rect.width//2 - sub_infra.get_width()//2, infra_rect.y + 242))
        
        UIEngine.draw_progress_bar(self.screen, infra_rect.x + 25, infra_rect.y + 295, 290, 12, self.eco.unemployment, 100, "Tỷ lệ Thất nghiệp hệ thống", COLOR_RED)
        UIEngine.draw_progress_bar(self.screen, infra_rect.x + 25, infra_rect.y + 350, 290, 12, self.eco.inequality, 100, "Chỉ số Bất bình đẳng thu nhập", COLOR_PINK)
        
        productivity_txt = FONT_MED.render(f"Năng suất vận hành cơ bản: {self.eco.income} Vàng/năm", True, (40, 90, 60))
        self.screen.blit(productivity_txt, (infra_rect.x + 25, infra_rect.y + 400))

        # --- THẺ BÀI BÊN PHẢI: KIẾN TRÚC THƯỢNG TẦNG ---
        self.policy_box.zone_policy.x = 670
        self.policy_box.zone_policy.y = 145
        self.policy_box.zone_policy.width = 340
        self.policy_box.zone_policy.height = 420
        policy_rect = self.policy_box.zone_policy
        
        pygame.draw.rect(self.screen, (40, 40, 45), (policy_rect.x + 8, policy_rect.y + 8, policy_rect.width, policy_rect.height), border_radius=12)
        pygame.draw.rect(self.screen, (245, 242, 235), policy_rect, border_radius=12)
        pygame.draw.rect(self.screen, COLOR_TEXT_DARK, policy_rect, 3, border_radius=12)
        
        title_policy = FONT_LARGE.render("KIẾN TRÚC THƯỢNG TẦNG", True, COLOR_TEXT_DARK)
        self.screen.blit(title_policy, (policy_rect.x + policy_rect.width//2 - title_policy.get_width()//2, policy_rect.y + 15))
        
        policy_img_rect = pygame.Rect(policy_rect.x + 15, policy_rect.y + 50, policy_rect.width - 30, 180)
        pygame.draw.rect(self.screen, COLOR_TEXT_DARK, policy_img_rect, 2, border_radius=8)
        blit_rounded_image(self.screen, r"C:\Users\Khang\OneDrive\Desktop\GAME_MLN\Independence Palace 🇻🇳.jpg", policy_img_rect, 8)
        
        sub_policy = FONT_MED.render("Sách lược điều phối ban sắc lệnh chính trị", True, COLOR_TEXT_DARK)
        self.screen.blit(sub_policy, (policy_rect.x + policy_rect.width//2 - sub_policy.get_width()//2, policy_rect.y + 242))
        
        for idx, p in enumerate(self.policy_box.policies):
            status_text = "[ĐÃ BAN HÀNH]" if p.is_activated else "[CHƯA BAN HÀNH]"
            p_color = (0, 130, 85) if p.is_activated else (110, 110, 115)
            
            item_y = policy_rect.y + 275 + idx * 50
            pygame.draw.rect(self.screen, (232, 228, 218) if not p.is_activated else (215, 238, 222), (policy_rect.x + 15, item_y, policy_rect.width - 30, 42), border_radius=6)
            pygame.draw.rect(self.screen, COLOR_TEXT_DARK, (policy_rect.x + 15, item_y, policy_rect.width - 30, 42), 1, border_radius=6)
            
            lbl_p = FONT_MED.render(f"Phím {idx+1}: {p.name[:16]}..", True, COLOR_TEXT_DARK)
            import config
            lbl_status = config.FONT_MINI.render(status_text, True, p_color)
            
            self.screen.blit(lbl_p, (policy_rect.x + 25, item_y + 12))
            self.screen.blit(lbl_status, (policy_rect.x + policy_rect.width - 130, item_y + 12))

       # ==========================================================
        # 3. LỚP NỀN HUD, BẢNG TIN VÀ THAO TÁC (ĐẨY XUỐNG DƯỚI - LAYER 2)
        # ==========================================================
        on_turn = self.player.get_rect().colliderect(self.zone_next_turn)
        
        # Nút bấm "QUA NĂM TIẾP THEO" (Nằm gọn gàng giữa đường)
        pygame.draw.rect(self.screen, COLOR_SHADOW, (self.zone_next_turn.x+4, self.zone_next_turn.y+4, 220, 50), border_radius=6)
        self.screen.fill(COLOR_PINK if not on_turn else COLOR_GOLD, self.zone_next_turn)
        lbl_turn_btn = FONT_MED.render("QUA NĂM TIẾP THEO", True, COLOR_TEXT_LIGHT if not on_turn else COLOR_TEXT_DARK)
        self.screen.blit(lbl_turn_btn, (self.zone_next_turn.x+36, self.zone_next_turn.y+16))

        # HUD vĩ mô trên đỉnh màn hình
        UIEngine.draw_hud(self.screen, self.eco)
        
        # Các nhãn chữ thông tin góc trái đỉnh
        lbl_year = FONT_LARGE.render(f"NĂM THỨ: {self.eco.turn}", True, (255, 255, 255))
        self.screen.blit(lbl_year, (40, 40)) 
        
        mode_text = "Toàn màn hình (F11)" if self.is_fullscreen else "Chế độ Cửa sổ (F11)"
        lbl_mode = FONT_MINI.render(f"Chế độ: {mode_text}", True, (160, 160, 165))
        self.screen.blit(lbl_mode, (40, 75)) 
        
        if self.event_system.current_event:
            lbl_ev = FONT_STATUS.render(f"BIẾN CỐ: {self.event_system.current_event['name']}", True, COLOR_RED)
            self.screen.blit(lbl_ev, (40, 100))

        # ----------------------------------------------------------
        # PANEL TRÁI: BẢN TIN THỊ TRƯỜNG VĨ MÔ (Dưới Thẻ Cơ sở hạ tầng)
        # ----------------------------------------------------------
        log_rect = pygame.Rect(40, 580, 340, 80)
        pygame.draw.rect(self.screen, (20, 20, 22), log_rect, border_radius=8)
        pygame.draw.rect(self.screen, (70, 70, 75), log_rect, 2, border_radius=8) 
        
        lbl_log_title = FONT_MED.render("[ BẢN TIN THỊ TRƯỜNG VĨ MÔ ]", True, COLOR_GOLD)
        self.screen.blit(lbl_log_title, (log_rect.x + 15, log_rect.y + 10))
        
        # Trích xuất 2 dòng log mới nhất để hiển thị vừa vặn trong khung
        for i, log_str in enumerate(self.eco.logs[-2:]):
            lbl_log = FONT_SMALL.render(log_str, True, COLOR_TEXT_LIGHT)
            self.screen.blit(lbl_log, (log_rect.x + 15, log_rect.y + 35 + i * 20))


        # ----------------------------------------------------------
        # PANEL PHẢI: CHỈ THỊ / THAO TÁC (Dưới Thẻ Thượng tầng)
        # ----------------------------------------------------------
        if self.current_hint:
            hint_rect = pygame.Rect(670, 580, 340, 80)
            pygame.draw.rect(self.screen, (20, 20, 22), hint_rect, border_radius=8)
            
            # Đổi màu viền dựa trên tính chất cảnh báo: Nhiệm vụ (Vàng) vs Thao tác (Xanh Mint)
            is_task = "NHIỆM VỤ" in self.current_hint
            border_color = COLOR_GOLD if is_task else COLOR_MINT
            pygame.draw.rect(self.screen, border_color, hint_rect, 2, border_radius=8)
            
            lbl_hint_title = FONT_MED.render("[ CHỈ THỊ CHIẾN LƯỢC ]" if is_task else "[ HƯỚNG DẪN THAO TÁC ]", True, border_color)
            self.screen.blit(lbl_hint_title, (hint_rect.x + 15, hint_rect.y + 10))
            
            # Xóa chữ tiền tố cũ để tiết kiệm không gian
            raw_text = self.current_hint.replace("NHIỆM VỤ: ", "").replace("THAO TÁC: ", "")
            lines = []
            
            # Thuật toán ngắt dòng thông minh (Word-Wrap)
            if "|" in raw_text:
                lines = [line.strip() for line in raw_text.split("|")]
            else:
                words = raw_text.split(' ')
                current_line = ""
                for word in words:
                    if FONT_SMALL.size(current_line + word)[0] < 310: # 310 là chiều rộng tối đa an toàn của text
                        current_line += word + " "
                    else:
                        lines.append(current_line)
                        current_line = word + " "
                if current_line:
                    lines.append(current_line)
            
            # In ra các dòng đã được ngắt (Tối đa hiển thị 2 dòng)
            for i, line_text in enumerate(lines[:2]):
                lbl_hint_text = FONT_SMALL.render(line_text.strip(), True, COLOR_TEXT_LIGHT)
                self.screen.blit(lbl_hint_text, (hint_rect.x + 15, hint_rect.y + 35 + i * 20))
        # ==========================================================
        # 4. LỚP NHÂN VẬT THỊ TRƯỞNG TRÊN CÙNG TUYỆT ĐỐI (LAYER 3)
        # ==========================================================
        # Di chuyển nhân vật xuống cuối cùng để vẽ đè lên tất cả HUD và các dải panel chữ phía trên
        if not self.game_over_msg:
            self.player.draw(self.screen)

        # ==========================================================
        # 5. MÀN HÌNH KẾT THÚC (GAME OVER OVERLAY)
        # ==========================================================
        if self.game_over_msg:
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(255)
            overlay.fill((15, 15, 18))
            self.screen.blit(overlay, (0, 0))
            is_fail = "4" in self.game_over_msg or "CRISIS" in self.game_over_msg
            title_surf = FONT_LARGE.render(self.game_over_msg, True, COLOR_RED if is_fail else COLOR_MINT)
            self.screen.blit(title_surf, (WIDTH//2 - title_surf.get_width()//2, 80))
            lbl_timeline_title = FONT_STATUS.render("[ BIÊN NIÊN SỬ TRIỀU ĐẠI QUẢN TRỊ CỦA BẠN ]", True, COLOR_GOLD)
            self.screen.blit(lbl_timeline_title, (100, 160))
            for idx, history_line in enumerate(self.eco.history_timeline[-10:]): 
                hist_surf = FONT_MED.render(f"• {history_line}", True, COLOR_TEXT_LIGHT)
                self.screen.blit(hist_surf, (120, 200 + idx * 30))
            restart_surf = FONT_STATUS.render("Nhấn phím [ R ] để khởi động lại guồng quay của bánh xe Lịch sử", True, COLOR_GOLD)
            self.screen.blit(restart_surf, restart_surf.get_rect(center=(WIDTH // 2, 560)))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_input()
            self.update()
            self.render()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = GameManager()
    game.run()