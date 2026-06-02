import pygame
import sys
import random
import math
import os
import asyncio
from config import *
from player import Player
from economy import EconomyState
from policy import PolicyManager
from events import EventEngine
from ui import UIEngine
from guide import GameGuide

NARRATIVES = {
    1: {
        "title": "CHƯƠNG 1: BÌNH MINH CỦA BẦY NGƯỜI",
        "subtitle": "(Thời Kỳ Công Xã Nguyên Thủy)",
        "text": [
            "Thế giới thuở sơ khai là một thực tại tàn khốc. Con người sinh ra tay trắng,",
            "không móng vuốt, không sức mạnh thể chất vượt trội.",
            "Giữa thiên nhiên vĩ đại và khắc nghiệt, kẻ đi săn đơn độc cũng chính là con mồi...",
            "",
            "Nhưng bước ngoặt đã đến khi họ phát hiện ra sức mạnh của sự gắn kết.",
            "Sống thành nhóm, cùng làm, cùng chia sẻ — cuộc sống Săn bắt - Hái lượm hình thành.",
            "Khi công cụ lao động chỉ là những hòn đá thô sơ, sự bình đẳng là cách duy nhất",
            "để tất cả cùng sống sót qua mùa đông hoang sơ."
        ]
    },
    2: {
        "title": "CHƯƠNG 2: XIỀNG XÍCH VÀ CƠ NGHIỆP",
        "subtitle": "(Thời Kỳ Chiếm Hữu Nô Lệ)",
        "text": [
            "Khi công cụ sản xuất tiến bộ, con người tạo ra nhiều của cải hơn nhu cầu tối thiểu.",
            "Sự dư thừa sinh ra lòng tham và ham muốn tích lũy tư hữu.",
            "Kẻ mạnh chiếm đoạt tư liệu sản xuất, biến kẻ yếu thành công cụ lao động biết nói.",
            "Xã hội phân hóa, xiềng xích của chế độ Chiếm hữu Nô lệ ra đời.",
            "",
            "Đó là một vết sẹo đau đớn trong lịch sử nhân loại,",
            "nhưng lại chính là bệ phóng cơ bắp để xây dựng nên những kỳ quan đền đài vĩ đại đầu tiên."
        ]
    },
    3: {
        "title": "CHƯƠNG 3: ĐẤT ĐAI VÀ LÃNH ĐỊA",
        "subtitle": "(Thời Kỳ Phong Kiến)",
        "text": [
            "Sự cưỡng bức thân xác nô lệ không thể tồn tại mãi khi hiệu suất chạm trần.",
            "Với những công cụ bằng sắt nhọn bén, đất đai bỗng hóa thành vàng ròng.",
            "Con người nhận ra: Thay vì trói buộc cơ thể nhau, việc làm chủ Đất đai",
            "mới là quyền lực tối thượng. Chế độ phong kiến được thiết lập.",
            "",
            "Người lao động giờ đây được trao một chút tự do, có mảnh ruộng riêng để cày cấy,",
            "tạo nên một động lực sản xuất mạnh mẽ chưa từng có trong lịch sử."
        ]
    },
    4: {
        "title": "CHƯƠNG 4: KỶ NGUYÊN HÀI HÒA VÀ CÔNG HỮU",
        "subtitle": "(Thời Kỳ Xã Hội Chủ Nghĩa)",
        "text": [
            "Khi những cuộc khủng hoảng thừa của thời đại trước đẩy xã hội vào mâu thuẫn bất ổn,",
            "nhân loại nhận ra: Lợi nhuận không nên tập trung vào tay một số ít người tư bản,",
            "mà phải thuộc về toàn thể cộng đồng lao động công hữu.",
            "",
            "Một hình thái mới ra đời — nơi các nhà máy, hầm mỏ và tư liệu sản xuất lớn",
            "thuộc sở hữu chung của toàn xã hội. Không còn cảnh người bóc lột người,",
            "con người giờ đây làm việc theo năng lực và hưởng thành quả theo đúng công sức đóng góp."
        ]
    },
    5: {
        "title": "CHƯƠNG 5: THẾ GIỚI NGÀY MAI",
        "subtitle": "(Kỷ Nguyên Tri Thức & Tự Động Hóa)",
        "text": [
            "Khi lực lượng sản xuất đạt đến đỉnh cao, máy móc và trí tuệ nhân tạo",
            "đã gánh vác toàn bộ lao động chân tay nặng nhọc. Sự khan hiếm vật chất lùi vào quá khứ.",
            "Con người không còn phải bán sức lao động để sinh tồn nữa,",
            "mà tự do phát triển tư duy, nghệ thuật, triết học và khoa học sáng tạo.",
            "",
            "Tài sản lớn nhất giờ đây là Tri thức chung của nhân loại.",
            "Nhân loại chính thức bước vào kỷ nguyên của sự tự do và tiến bộ tuyệt đối."
        ]
    },
    6: {
        "title": "BIÊN NIÊN SỬ HOÀN THÀNH: ĐỈNH CAO VĂN MINH",
        "subtitle": "(Hành trình tiến hóa vĩ đại)",
        "text": [
            "Lịch sử không phải là một đường thẳng tình cờ,",
            "mà là một hành trình tiến hóa tất yếu của công cụ lao động và tư duy biện chứng.",
            "Từ hòn đá thô sơ thuở hồng hoang đến những bộ não điện tử không gian,",
            "con người đã tự viết nên số phận của mình qua chính hoạt động lao động thực tiễn.",
            "",
            "Và hành trình vươn ra các thiên hà xa xôi kia... chưa bao giờ dừng lại!",
            "",
            "CHÚC MỪNG! BẠN ĐÃ ĐƯA NHÂN LOẠI ĐẾN ĐỈNH CAO VĂN MINH."
        ]
    }
}

class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ky Nguyen Tien Hoa (The Age of Evolution) - Mo Phong Bien Chung")
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.eco = EconomyState()
        self.policy_box = PolicyManager()
        self.event_system = EventEngine()
        self.guide = GameGuide()

        # Căn chỉnh vị trí các khu vực tương tác trên đường lộ trung tâm
        self.zone_next_turn = pygame.Rect(415, 570, 220, 50)
        self.zone_resource = pygame.Rect(415, 290, 220, 100) # Khu vực khai thác mới
        
        self.game_over_msg = ""
        self.current_hint = ""
        self.running = True
        
        # Biến quản lý Lời dẫn / Cắt cảnh (Intro Cutscene)
        self.in_intro = True
        self.intro_chapter = 1
        self.last_chapter = 1
        
        self.image_cache = {}
        self.action_cooldown = 0
        
        # Phục vụ hiệu ứng khai thác tài nguyên
        self.harvest_popups = []  # Lưu các popup hiển thị số lượng vừa cộng
        
    def check_emergent_endings(self):
        """Kiểm tra điều kiện kết thúc game hoặc khủng hoảng"""
        # Tránh kiểm tra khi đang chạy Intro
        if self.in_intro:
            return
            
        avg_support = self.eco.get_average_support()
        
        # 1. Khủng hoảng sụp đổ xã hội (Tension quá cao hoặc bị đói rã bầy)
        if self.eco.tech_level in [2, 3, 4]:
            if self.eco.upheaval_tension >= 100:
                self.game_over_msg = f"THẤT BẠI: Khởi nghĩa bùng nổ lật đổ chế độ tại Chương {self.eco.tech_level}!"
                self.eco.history_timeline.append("KẾT THÚC: Bất ổn dân chúng chạm đỉnh gây sụp đổ thể chế.")
                return

        # 2. Hết lương thực chết đói ở Chương 1
        if self.eco.tech_level == 1 and self.eco.food <= 0:
            self.game_over_msg = "THẤT BẠI: Bộ tộc nguyên thủy của bạn bị xóa sổ do nạn đói rét!"
            self.eco.history_timeline.append("KẾT THÚC: Bộ tộc tan rã vì đói khát.")
            return

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                # Nếu Guide đang mở, xử lý phím điều khiển Guide và không thực hiện các phím game chính
                if self.guide.is_visible:
                    if event.key == pygame.K_g or event.key == pygame.K_ESCAPE:
                        self.guide.toggle_visibility()
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        self.guide.prev_tab()
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        self.guide.next_tab()
                    continue
                
                # 1. Nếu đang xem Lời dẫn Intro, ấn SPACE để bỏ qua vào game
                if self.in_intro:
                    if event.key == pygame.K_SPACE:
                        if self.intro_chapter == 6:
                            # Đã thắng game, reset
                            self.__init__()
                        else:
                            self.in_intro = False
                    return
                
                # 2. Phím G mở/đóng Guide hướng dẫn
                if event.key == pygame.K_g:
                    self.guide.toggle_visibility()
                    
                # 3. Phím R reset trò chơi khi game over
                if self.game_over_msg:
                    if event.key == pygame.K_r:
                        self.__init__()
                    return

                # 4. Khi đang xảy ra Biến cố có lựa chọn, ép người chơi chọn phím A hoặc B
                if self.event_system.current_event:
                    if event.key == pygame.K_a:
                        self.event_system.resolve_event('A', self.eco)
                    elif event.key == pygame.K_b:
                        self.event_system.resolve_event('B', self.eco)
                    return
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    # Nếu Guide đang mở, kiểm tra xem có click vào các tab hay click ra ngoài để đóng không
                    if self.guide.is_visible:
                        # Kiểm tra xem có click vào các tab trong guide không
                        if self.guide.handle_click(mouse_pos):
                            continue
                        # Hoặc click vào nút Guide để đóng
                        if UIEngine.guide_button_rect.collidepoint(mouse_pos):
                            self.guide.toggle_visibility()
                            continue
                    else:
                        if UIEngine.guide_button_rect.collidepoint(mouse_pos) and not self.in_intro:
                            self.guide.toggle_visibility()

        # Nếu Guide đang mở, xử lý cuộn trang bằng phím đè rồi thoát
        if self.guide.is_visible:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.guide.scroll_offset = max(0, self.guide.scroll_offset - 8)
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                current_tab_name = self.guide.tab_names[self.guide.current_tab]
                content_len = len(self.guide.GUIDE_CONTENT[current_tab_name])
                max_scroll = max(0, content_len * 20 - 330)
                self.guide.scroll_offset = min(max_scroll, self.guide.scroll_offset + 8)
            return

        if self.in_intro or self.game_over_msg:
            return

        # Đọc tổ hợp phím di chuyển nhân vật
        keys = pygame.key.get_pressed()
        self.player.move(keys)
        
        p_rect = self.player.get_rect()
        on_infra = p_rect.colliderect(self.policy_box.zone_infra)
        on_policy = p_rect.colliderect(self.policy_box.zone_policy)
        on_resource = p_rect.colliderect(self.zone_resource)
        on_turn = p_rect.colliderect(self.zone_next_turn)

        # Thiết lập các gợi ý chỉ thị cho người chơi tùy thuộc chương
        self.current_hint = "CHỈ THỊ: "
        ch = self.eco.tech_level
        if ch == 1:
            self.current_hint += f"Tích lũy 200 Lương thực để lên đời II. Đứng vào khu vực khai thác ở giữa và nhấn [SPACE] để săn bắt/hái quả."
        elif ch == 2:
            self.current_hint += f"Cần 100 Quặng và 150 Vàng để đúc công cụ sắt lên đời III. Khai thác ở giữa để nhận tài nguyên."
        elif ch == 3:
            self.current_hint += f"Tích lũy 800 Vàng để phát minh Máy hơi nước lên đời IV. Chú ý thu thuế từ ruộng đất qua năm hoặc nhấn SPACE ở giữa."
        elif ch == 4:
            self.current_hint += f"Đạt Quỹ Phúc Lợi >= 1M và Bình đẳng >= 90% để lên Đời V. Bấm SPACE nâng cấp cơ sở hạ tầng tăng vọt năng suất!"
        elif ch == 5:
            self.current_hint += f"Nghiên cứu nâng cấp Trạm điện và Bộ não AI. Đưa chỉ số văn minh đạt 100% để GIÀNH CHIẾN THẮNG."

        # Xử lý khi đứng trên các vùng tương tác
        if on_infra:
            up_info = self.policy_box.get_upgrade_info(self.eco)
            if up_info:
                self.current_hint = f"NÂNG CẤP: {up_info['name']} (Phí: {up_info['cost']}). Nhấn [SPACE] để nâng cấp Lực lượng sản xuất."
                if keys[pygame.K_SPACE] and self.action_cooldown == 0:
                    success = self.policy_box.execute_infra_upgrade(self.eco)
                    if success:
                        # Tạo hiệu ứng nổ nhẹ
                        self.harvest_popups.append({"txt": "NÂNG CẤP THÀNH CÔNG!", "x": self.player.x, "y": self.player.y - 40, "timer": 60, "color": COLOR_MINT})
                    self.action_cooldown = 15  # Cooldown 250ms
            else:
                self.current_hint = "CƠ SỞ HẠ TẦNG: Đã đạt mức tối đa của thời kỳ này."
                
        elif on_policy:
            policies = self.policy_box.get_policies_for_chapter(self.eco.tech_level)
            if policies:
                self.current_hint = f"SÁCH LƯỢC: Nhấn [1] để ra lệnh '{policies[0].name}' | Nhấn [2] để ra lệnh '{policies[1].name}'"
                if keys[pygame.K_1] and self.action_cooldown == 0:
                    res = self.policy_box.execute_policy_by_idx(0, self.eco)
                    if res == "SUCCESS":
                        self.harvest_popups.append({"txt": "BAN HÀNH CHÍNH SÁCH 1", "x": self.player.x, "y": self.player.y - 40, "timer": 60, "color": COLOR_BLUE})
                    self.action_cooldown = 12  # Cooldown 200ms
                elif keys[pygame.K_2] and self.action_cooldown == 0:
                    res = self.policy_box.execute_policy_by_idx(1, self.eco)
                    if res == "SUCCESS":
                        self.harvest_popups.append({"txt": "BAN HÀNH CHÍNH SÁCH 2", "x": self.player.x, "y": self.player.y - 40, "timer": 60, "color": COLOR_BLUE})
                    self.action_cooldown = 12  # Cooldown 200ms
            else:
                self.current_hint = "KIẾN TRÚC THƯỢNG TẦNG: Không có chính sách nào khả dụng."
                
        elif on_resource:
            self.current_hint = "KHAI THÁC: Nhấn giữ hoặc bấm liên tục [SPACE] để trực tiếp khai thác tài sản xã hội."
            if keys[pygame.K_SPACE] and self.action_cooldown == 0:
                # Thực hiện khai thác dựa theo đời
                txt_gain = ""
                color_gain = COLOR_GOLD
                if ch == 1:
                    self.eco.food += 10
                    self.eco.fire = min(100, self.eco.fire + 5) # Khai thác sưởi thêm lửa
                    txt_gain = "+10 Lương thực, +5% Lửa"
                    color_gain = COLOR_GOLD_SOFT
                elif ch == 2:
                    self.eco.food += 4
                    self.eco.ore += 5
                    self.eco.gold += 3
                    txt_gain = "+4 Thức ăn, +5 Quặng, +3 Vàng"
                    color_gain = COLOR_GOLD
                elif ch == 3:
                    self.eco.food += 5
                    self.eco.gold += 15
                    txt_gain = "+5 Thức ăn, +15 Vàng thuế"
                    color_gain = COLOR_CH3
                elif ch == 4:
                    # Tăng trưởng quy mô theo năng suất phúc lợi hiện tại
                    gain_welfare = int(2000 * (self.eco.welfare_income / 2000))
                    self.eco.welfare_fund += gain_welfare
                    self.eco.food += 10
                    txt_gain = f"+10 Thức ăn, +{gain_welfare:,} Quỹ Phúc lợi"
                    color_gain = COLOR_MINT
                elif ch == 5:
                    self.eco.knowledge += 15
                    self.eco.clean_energy += 15
                    txt_gain = "+15 Tri thức, +15 Năng lượng sạch"
                    color_gain = COLOR_CH5
                
                # Thêm popup hiển thị
                self.harvest_popups.append({
                    "txt": txt_gain,
                    "x": self.player.x + random.randint(-20, 20),
                    "y": self.player.y - 30,
                    "timer": 45,
                    "color": color_gain
                })
                self.action_cooldown = 9  # Cooldown 150ms
                
        elif on_turn:
            self.current_hint = "QUA NĂM: Nhấn phím [SPACE] để kết thúc năm cũ, tiến bước vào năm mới và kích hoạt biến cố."
            if keys[pygame.K_SPACE] and self.action_cooldown == 0:
                self.eco.process_next_turn()
                # Kích hoạt sự kiện
                self.event_system.trigger_annual_event(self.eco)
                self.harvest_popups.append({"txt": "NĂM MỚI BẮT ĐẦU!", "x": WIDTH//2, "y": HEIGHT//2, "timer": 70, "color": COLOR_GOLD})
                self.action_cooldown = 18  # Cooldown 300ms

    def update(self):
        if self.action_cooldown > 0:
            self.action_cooldown -= 1

        if self.in_intro:
            return
            
        # Kiểm tra chuyển chương tự động của Chương 4 -> Chương 5
        if self.eco.tech_level == 4:
            if self.eco.welfare_fund >= 1000000 and self.eco.equality >= 90:
                self.eco.tech_level = 5
                # Reset và cài đặt tài nguyên cho Chương 5
                self.eco.clean_energy = 50
                self.eco.knowledge = 50
                self.eco.civilization_level = 5
                self.eco.energy_income = 20
                self.eco.knowledge_income = 15
                self.eco.add_log("[NÂNG CẤP CHUYỂN DỊCH] Tiến lên Kỷ nguyên Tri thức & Tự động hóa!")
        
        # 1. Cập nhật nhịp hoạt ảnh nhân vật
        if not self.game_over_msg:
            self.player.animation_timer += 0.08
            self.check_emergent_endings()
            
        # 2. Kiểm tra nếu Tech Level đổi từ lần trước để kích hoạt Intro
        if self.eco.tech_level != self.last_chapter:
            self.in_intro = True
            self.intro_chapter = self.eco.tech_level
            self.last_chapter = self.eco.tech_level
            
        # 3. Thắng game hoàn toàn tại Chương 5
        if self.eco.tech_level == 5 and self.eco.civilization_level >= 100:
            if self.intro_chapter != 6:
                self.in_intro = True
                self.intro_chapter = 6  # Ending screen
                self.game_over_msg = "VICTORY: BẠN ĐÃ ĐƯA NHÂN LOẠI ĐẾN ĐỈNH CAO VĂN MINH."
                
        # 4. Cập nhật các popup bay lên rồi mờ đi
        for p in self.harvest_popups[:]:
            p["y"] -= 1.2
            p["timer"] -= 1
            if p["timer"] <= 0:
                self.harvest_popups.remove(p)

    def render(self):
        # ==========================================================
        # TRƯỜNG HỢP 1: MÀN HÌNH NARRATOR INTRO (CHỮ CHẠY TÊN NỀN TỐI)
        # ==========================================================
        if self.in_intro:
            self.screen.fill((10, 10, 12))
            intro_data = NARRATIVES.get(self.intro_chapter, NARRATIVES[1])
            
            # Vẽ tiêu đề lớn
            title_surf = FONT_LARGE.render(intro_data["title"], True, COLOR_GOLD)
            sub_surf = FONT_STATUS.render(intro_data["subtitle"], True, COLOR_MINT_SOFT)
            
            self.screen.blit(title_surf, (WIDTH//2 - title_surf.get_width()//2, 80))
            self.screen.blit(sub_surf, (WIDTH//2 - sub_surf.get_width()//2, 115))
            
            # Vẽ các dòng lời dẫn truyện
            y_offset = 180
            for line in intro_data["text"]:
                line_surf = FONT_STATUS.render(line, True, COLOR_TEXT_LIGHT)
                self.screen.blit(line_surf, (WIDTH//2 - line_surf.get_width()//2, y_offset))
                y_offset += 32
                
            # Gợi ý bấm phím
            prompt_str = "Nhấn phím [ SPACE ] để khởi động bánh xe Lịch sử..." if self.intro_chapter != 6 else "Nhấn [ SPACE ] để quay lại vĩ độ thời gian nguyên sơ..."
            prompt_surf = FONT_STATUS.render(prompt_str, True, COLOR_MINT)
            self.screen.blit(prompt_surf, (WIDTH//2 - prompt_surf.get_width()//2, HEIGHT - 100))
            
            pygame.display.flip()
            return

        # ==========================================================
        # TRƯỜNG HỢP 2: GAMEPLAY CHÍNH
        # ==========================================================
        # 1. Nền đường lộ và xám xi măng ấm
        self.screen.fill((210, 206, 196))
        
        # Bảng HUD Top Bar
        pygame.draw.rect(self.screen, COLOR_ROAD, (0, 0, WIDTH, 125))
        pygame.draw.rect(self.screen, COLOR_GOLD, (0, 121, WIDTH, 4))
        
        # Vẽ con đường lộ dọc trung tâm
        pygame.draw.rect(self.screen, (75, 80, 85), (WIDTH//2 - 80, 125, 160, HEIGHT - 125))
        for y_line in range(130, HEIGHT, 40):
            pygame.draw.rect(self.screen, (240, 240, 240), (WIDTH//2 - 3, y_line, 6, 20))

        # Tìm file ảnh phù hợp với các định dạng khác nhau (png, jpg, jpeg, webp)
        def get_chapter_image_path(chapter_num):
            for ext in ['.png', '.jpg', '.jpeg', '.webp', '.PNG', '.JPG', '.JPEG', '.WEBP']:
                path = f"intro_chapter{chapter_num}{ext}"
                if os.path.exists(path):
                    return path
            return f"intro_chapter{chapter_num}.png" # Mặc định nếu không tìm thấy

        # Phép vẽ ảnh bo góc an toàn, hỗ trợ placeholder nếu thiếu ảnh
        def blit_rounded_image(target_screen, image_path, rect, radius, label):
            try:
                # Kiểm tra cache
                cache_key = (image_path, rect.width, rect.height)
                if cache_key in self.image_cache:
                    target_screen.blit(self.image_cache[cache_key], (rect.x, rect.y))
                    return

                if not os.path.exists(image_path):
                    raise FileNotFoundError
                img = pygame.image.load(image_path).convert_alpha()
                img = pygame.transform.scale(img, (rect.width, rect.height))
                mask = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
                pygame.draw.rect(mask, (255, 255, 255, 255), (0, 0, rect.width, rect.height), border_radius=radius)
                img.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
                
                # Lưu vào cache
                self.image_cache[cache_key] = img
                target_screen.blit(img, (rect.x, rect.y))
            except Exception:
                # Vẽ khung màu xám thanh lịch
                pygame.draw.rect(target_screen, (160, 165, 170), rect, border_radius=radius)
                pygame.draw.rect(target_screen, COLOR_TEXT_DARK, rect, 2, border_radius=radius)
                err_txt = FONT_MINI.render(f"[Ảnh: {label}]", True, (40, 40, 40))
                target_screen.blit(err_txt, (rect.x + rect.width//2 - err_txt.get_width()//2, rect.y + rect.height//2 - 6))

        # ==========================================================
        # 2. THẺ BÀI PHÍA BÊN TRÁI: CƠ SỞ HẠ TẦNG (HẠ TẦNG SẢN XUẤT)
        # ==========================================================
        infra_rect = self.policy_box.zone_infra
        pygame.draw.rect(self.screen, (40, 40, 45), (infra_rect.x + 8, infra_rect.y + 8, infra_rect.width, infra_rect.height), border_radius=12)
        pygame.draw.rect(self.screen, (245, 242, 235), infra_rect, border_radius=12)
        pygame.draw.rect(self.screen, COLOR_TEXT_DARK, infra_rect, 3, border_radius=12)
        
        title_infra = FONT_LARGE.render("CƠ SỞ HẠ TẦNG", True, COLOR_TEXT_DARK)
        self.screen.blit(title_infra, (infra_rect.x + infra_rect.width//2 - title_infra.get_width()//2, infra_rect.y + 15))
        
        infra_img_rect = pygame.Rect(infra_rect.x + 15, infra_rect.y + 50, infra_rect.width - 30, 150)
        infra_img_path = get_chapter_image_path(self.eco.tech_level)
        blit_rounded_image(self.screen, infra_img_path, infra_img_rect, 8, os.path.basename(infra_img_path))
        
        # Vẽ các chỉ số sản xuất đặc trưng của từng chương
        y_stats = infra_rect.y + 215
        ch = self.eco.tech_level
        if ch == 1:
            lbl_food = FONT_MED.render(f"• Lương thực tích lũy: {self.eco.food} / 200", True, COLOR_TEXT_DARK)
            lbl_fire = FONT_MED.render(f"• Độ lớn ngọn lửa: {self.eco.fire}%", True, COLOR_TEXT_DARK)
            lbl_income = FONT_MED.render(f"• Năng suất săn bắn: +{self.eco.food_income}/năm", True, (40, 90, 60))
            self.screen.blit(lbl_food, (infra_rect.x + 25, y_stats))
            self.screen.blit(lbl_fire, (infra_rect.x + 25, y_stats + 30))
            self.screen.blit(lbl_income, (infra_rect.x + 25, y_stats + 60))
            
            # Thanh tiến trình
            UIEngine.draw_progress_bar(self.screen, infra_rect.x + 25, y_stats + 125, 290, 10, self.eco.food, 200, "Định cư nông nghiệp", COLOR_BLUE)
            
        elif ch == 2:
            lbl_food = FONT_MED.render(f"• Lương thực dự trữ: {self.eco.food}", True, COLOR_TEXT_DARK)
            lbl_ore = FONT_MED.render(f"• Quặng khai thác: {self.eco.ore} / 100", True, COLOR_TEXT_DARK)
            lbl_gold = FONT_MED.render(f"• Tiền vàng tích lũy: {self.eco.gold} / 150", True, COLOR_TEXT_DARK)
            lbl_slaves = FONT_MED.render(f"• Số lượng Nô lệ: {self.eco.slaves} người", True, COLOR_TEXT_DARK)
            lbl_prod = FONT_MED.render(f"• Tổng thu nhập sản lượng từ nô lệ", True, (40, 90, 60))
            self.screen.blit(lbl_food, (infra_rect.x + 25, y_stats))
            self.screen.blit(lbl_ore, (infra_rect.x + 25, y_stats + 25))
            self.screen.blit(lbl_gold, (infra_rect.x + 25, y_stats + 50))
            self.screen.blit(lbl_slaves, (infra_rect.x + 25, y_stats + 75))
            self.screen.blit(lbl_prod, (infra_rect.x + 25, y_stats + 105))
            
            # Thanh tiến trình
            UIEngine.draw_progress_bar(self.screen, infra_rect.x + 25, y_stats + 145, 290, 10, self.eco.ore, 100, "Thu thập quặng đúc sắt", COLOR_RED)
            
        elif ch == 3:
            lbl_food = FONT_MED.render(f"• Lương thực dư thừa: {self.eco.food}", True, COLOR_TEXT_DARK)
            lbl_gold = FONT_MED.render(f"• Vàng trong ngân khố: {self.eco.gold} / 800", True, COLOR_TEXT_DARK)
            lbl_tax = FONT_MED.render(f"• Thuế suất Phong kiến: {self.eco.tax_rate}%", True, COLOR_TEXT_DARK)
            lbl_prod = FONT_MED.render(f"• Nông nghiệp thu hoạch cơ bản: +{40 + self.eco.food_income}/năm", True, (40, 90, 60))
            self.screen.blit(lbl_food, (infra_rect.x + 25, y_stats))
            self.screen.blit(lbl_gold, (infra_rect.x + 25, y_stats + 30))
            self.screen.blit(lbl_tax, (infra_rect.x + 25, y_stats + 60))
            self.screen.blit(lbl_prod, (infra_rect.x + 25, y_stats + 90))
            
            UIEngine.draw_progress_bar(self.screen, infra_rect.x + 25, y_stats + 145, 290, 10, self.eco.gold, 800, "Hải trình phong kiến", COLOR_GOLD)
            
        elif ch == 4:
            lbl_welf = FONT_MED.render(f"• Quỹ Phúc lợi: {self.eco.welfare_fund:,} / 1M đ", True, COLOR_TEXT_DARK)
            lbl_eq = FONT_MED.render(f"• Chỉ số Bình đẳng: {self.eco.equality}% / 90%", True, COLOR_TEXT_DARK)
            lbl_food = FONT_MED.render(f"• Lương thực dự trữ: {self.eco.food}", True, COLOR_TEXT_DARK)
            lbl_prod = FONT_MED.render(f"• Năng suất công nghiệp: +{self.eco.welfare_income:,}/năm", True, (40, 90, 60))
            self.screen.blit(lbl_welf, (infra_rect.x + 25, y_stats))
            self.screen.blit(lbl_eq, (infra_rect.x + 25, y_stats + 30))
            self.screen.blit(lbl_food, (infra_rect.x + 25, y_stats + 60))
            self.screen.blit(lbl_prod, (infra_rect.x + 25, y_stats + 90))
            
            UIEngine.draw_progress_bar(self.screen, infra_rect.x + 25, y_stats + 145, 290, 10, self.eco.welfare_fund, 1000000, "Tích lũy quỹ phúc lợi công hữu", COLOR_MINT)
            
        elif ch == 5:
            lbl_nrg = FONT_MED.render(f"• Năng lượng sạch: {self.eco.clean_energy}", True, COLOR_TEXT_DARK)
            lbl_kno = FONT_MED.render(f"• Tri thức tích lũy: {self.eco.knowledge}", True, COLOR_TEXT_DARK)
            lbl_civ = FONT_MED.render(f"• Chỉ số Văn minh: {self.eco.civilization_level}%", True, COLOR_TEXT_DARK)
            lbl_prod = FONT_MED.render(f"• Tự động sinh: +{self.eco.energy_income} N.Lượng, +{self.eco.knowledge_income} T.Thức", True, (40, 90, 60))
            self.screen.blit(lbl_nrg, (infra_rect.x + 25, y_stats))
            self.screen.blit(lbl_kno, (infra_rect.x + 25, y_stats + 30))
            self.screen.blit(lbl_civ, (infra_rect.x + 25, y_stats + 60))
            self.screen.blit(lbl_prod, (infra_rect.x + 25, y_stats + 90))
            
            UIEngine.draw_progress_bar(self.screen, infra_rect.x + 25, y_stats + 145, 290, 10, self.eco.civilization_level, 100, "Mức độ Văn minh tối thượng", COLOR_BLUE)

        # ==========================================================
        # 3. THẺ BÀI BÊN PHẢI: KIẾN TRÚC THƯỢNG TẦNG (SẮC LỆNH CHÍNH TRỊ)
        # ==========================================================
        policy_rect = self.policy_box.zone_policy
        pygame.draw.rect(self.screen, (40, 40, 45), (policy_rect.x + 8, policy_rect.y + 8, policy_rect.width, policy_rect.height), border_radius=12)
        pygame.draw.rect(self.screen, (245, 242, 235), policy_rect, border_radius=12)
        pygame.draw.rect(self.screen, COLOR_TEXT_DARK, policy_rect, 3, border_radius=12)
        
        title_policy = FONT_LARGE.render("KIẾN TRÚC THƯỢNG TẦNG", True, COLOR_TEXT_DARK)
        self.screen.blit(title_policy, (policy_rect.x + policy_rect.width//2 - title_policy.get_width()//2, policy_rect.y + 15))
        
        policy_img_rect = pygame.Rect(policy_rect.x + 15, policy_rect.y + 50, policy_rect.width - 30, 80)
        blit_rounded_image(self.screen, "Independence Palace 🇻🇳.jpg", policy_img_rect, 8, "Independence Palace 🇻🇳.jpg")
        
        # Liệt kê chính sách khả dụng
        p_list = self.policy_box.get_policies_for_chapter(self.eco.tech_level)
        y_policy_item = policy_rect.y + 140
        for idx, p in enumerate(p_list):
            pygame.draw.rect(self.screen, (232, 228, 218), (policy_rect.x + 15, y_policy_item, policy_rect.width - 30, 68), border_radius=6)
            pygame.draw.rect(self.screen, COLOR_TEXT_DARK, (policy_rect.x + 15, y_policy_item, policy_rect.width - 30, 68), 1, border_radius=6)
            
            lbl_name = FONT_MED.render(f"Phím {idx+1}: {p.name}", True, COLOR_TEXT_DARK)
            lbl_cost = FONT_MINI.render(f"Chi phí: {p.cost_desc}", True, COLOR_RED)
            lbl_desc = FONT_MINI.render(p.desc, True, (60, 60, 60))
            
            self.screen.blit(lbl_name, (policy_rect.x + 25, y_policy_item + 6))
            self.screen.blit(lbl_cost, (policy_rect.x + 25, y_policy_item + 24))
            self.screen.blit(lbl_desc, (policy_rect.x + 25, y_policy_item + 42))
            
            y_policy_item += 76

        # Thông tin nâng cấp Lực lượng sản xuất
        up_info = self.policy_box.get_upgrade_info(self.eco)
        if up_info:
            pygame.draw.rect(self.screen, (215, 230, 245), (policy_rect.x + 15, y_policy_item, policy_rect.width - 30, 100), border_radius=6)
            pygame.draw.rect(self.screen, COLOR_BLUE, (policy_rect.x + 15, y_policy_item, policy_rect.width - 30, 100), 1, border_radius=6)
            
            lbl_up_t = FONT_STATUS.render("[ CẢI CÁCH HẠ TẦNG KINH TẾ ]", True, COLOR_BLUE)
            lbl_up_n = FONT_SMALL.render(f"Nâng cấp: {up_info['name']}", True, COLOR_TEXT_DARK)
            lbl_up_c = FONT_MINI.render(f"Yêu cầu: {up_info['cost']}", True, COLOR_RED if not up_info['can_afford'] else (0, 120, 50))
            lbl_up_d = FONT_MINI.render(f"Mô tả: {up_info['desc'][:46]}..", True, (70, 70, 70))
            
            self.screen.blit(lbl_up_t, (policy_rect.x + 25, y_policy_item + 6))
            self.screen.blit(lbl_up_n, (policy_rect.x + 25, y_policy_item + 28))
            self.screen.blit(lbl_up_c, (policy_rect.x + 25, y_policy_item + 48))
            self.screen.blit(lbl_up_d, (policy_rect.x + 25, y_policy_item + 68))
        else:
            pygame.draw.rect(self.screen, (230, 245, 235), (policy_rect.x + 15, y_policy_item, policy_rect.width - 30, 60), border_radius=6)
            lbl_max = FONT_MED.render("Lực lượng sản xuất đạt cực thịnh!", True, (0, 120, 50))
            self.screen.blit(lbl_max, (policy_rect.x + 25, y_policy_item + 20))

        # ==========================================================
        # 4. KHU VỰC TRUNG TÂM: ĐƯỜNG LỘ VÀ CÁC Ô TƯƠNG TÁC
        # ==========================================================
        on_turn = self.player.get_rect().colliderect(self.zone_next_turn)
        on_resource = self.player.get_rect().colliderect(self.zone_resource)

        # Nút bấm "QUA NĂM TIẾP THEO" (Giữa đường phía dưới)
        pygame.draw.rect(self.screen, COLOR_SHADOW, (self.zone_next_turn.x+4, self.zone_next_turn.y+4, 220, 50), border_radius=6)
        self.screen.fill(COLOR_PINK if not on_turn else COLOR_GOLD, self.zone_next_turn)
        pygame.draw.rect(self.screen, COLOR_TEXT_DARK, self.zone_next_turn, 2, border_radius=6)
        lbl_turn_btn = FONT_MED.render("QUA NĂM TIẾP THEO", True, COLOR_TEXT_LIGHT if not on_turn else COLOR_TEXT_DARK)
        self.screen.blit(lbl_turn_btn, (self.zone_next_turn.x+36, self.zone_next_turn.y+16))

        # Ô "KHU VỰC KHAI THÁC" (Giữa đường phía trên)
        pygame.draw.rect(self.screen, COLOR_SHADOW, (self.zone_resource.x+4, self.zone_resource.y+4, 220, 100), border_radius=8)
        
        # Chọn màu sắc cho khu vực khai thác dựa trên chương
        harvest_colors = {
            1: (180, 140, 100), # Nâu gỗ
            2: (170, 175, 180), # Xám kim loại
            3: (218, 165, 32),  # Vàng đồng cỏ
            4: (240, 140, 140), # Đỏ hồng nhạt
            5: (140, 220, 240)  # Xanh lam nhạt
        }
        res_color = harvest_colors.get(self.eco.tech_level, (100, 200, 150))
        
        self.screen.fill(res_color if not on_resource else COLOR_MINT, self.zone_resource)
        pygame.draw.rect(self.screen, COLOR_TEXT_DARK, self.zone_resource, 2, border_radius=8)
        
        # Chữ của ô khai thác tài nguyên
        lbl_res_t = FONT_STATUS.render("KHU VỰC KHAI THÁC", True, COLOR_TEXT_DARK)
        
        labels_ch = {
            1: "Săn bắn & Hái lượm",
            2: "Nô dịch mỏ quặng",
            3: "Cày ruộng địa chủ",
            4: "Sản xuất XHCN",
            5: "Tổng hợp tri thức AI"
        }
        lbl_res_desc = FONT_SMALL.render(labels_ch.get(self.eco.tech_level, ""), True, (50, 50, 50))
        lbl_res_cmd = FONT_MINI.render("[ SPACE ĐỂ KHAI THÁC ]", True, COLOR_TEXT_DARK if on_resource else (70, 70, 70))
        
        self.screen.blit(lbl_res_t, (self.zone_resource.x + 18, self.zone_resource.y + 15))
        self.screen.blit(lbl_res_desc, (self.zone_resource.x + 36, self.zone_resource.y + 42))
        self.screen.blit(lbl_res_cmd, (self.zone_resource.x + 40, self.zone_resource.y + 68))

        # HUD vĩ mô trên đỉnh màn hình
        UIEngine.draw_hud(self.screen, self.eco)
        UIEngine.draw_guide_button(self.screen)

        # ==========================================================
        # 5. DẢI BẢN TIN VÀ HƯỚNG DẪN Ở DƯỚI CÙNG
        # ==========================================================
        # Panel Trái: Bản tin thị trường vĩ mô
        log_rect = pygame.Rect(40, 575, 340, 105)
        pygame.draw.rect(self.screen, (20, 20, 22), log_rect, border_radius=8)
        pygame.draw.rect(self.screen, (70, 70, 75), log_rect, 2, border_radius=8) 
        
        lbl_log_title = FONT_MED.render("[ BIÊN NIÊN SỬ XÃ HỘI ]", True, COLOR_GOLD)
        self.screen.blit(lbl_log_title, (log_rect.x + 15, log_rect.y + 8))
        
        log_y_offset = log_rect.y + 30
        for log_str in self.eco.logs[-3:]:
            wrapped_lines = UIEngine.wrap_text(log_str, FONT_SMALL, 310)
            for line in wrapped_lines[:1]:
                if log_y_offset + 15 < log_rect.y + log_rect.height:
                    lbl_log = FONT_SMALL.render(line, True, COLOR_TEXT_LIGHT)
                    self.screen.blit(lbl_log, (log_rect.x + 15, log_y_offset))
                    log_y_offset += 20

        # Panel Phải: Chỉ thị hoặc hướng dẫn
        if self.current_hint:
            hint_rect = pygame.Rect(670, 575, 340, 105)
            pygame.draw.rect(self.screen, (20, 20, 22), hint_rect, border_radius=8)
            
            is_task = "CHỈ THỊ" in self.current_hint or "NÂNG CẤP" in self.current_hint
            border_color = COLOR_GOLD if is_task else COLOR_MINT
            pygame.draw.rect(self.screen, border_color, hint_rect, 2, border_radius=8)
            
            lbl_hint_title = FONT_MED.render("[ CHỈ THỊ CHIẾN LƯỢC ]" if is_task else "[ HƯỚNG DẪN THAO TÁC ]", True, border_color)
            self.screen.blit(lbl_hint_title, (hint_rect.x + 15, hint_rect.y + 8))
            
            raw_text = self.current_hint.replace("CHỈ THỊ: ", "").replace("HƯỚNG DẪN: ", "").replace("NÂNG CẤP: ", "").replace("SÁCH LƯỢC: ", "").replace("KHAI THÁC: ", "").replace("QUA NĂM: ", "")
            lines = UIEngine.wrap_text(raw_text, FONT_SMALL, 310)
            for i, line_text in enumerate(lines[:3]):
                lbl_hint_text = FONT_SMALL.render(line_text, True, COLOR_TEXT_LIGHT)
                self.screen.blit(lbl_hint_text, (hint_rect.x + 15, hint_rect.y + 30 + i * 18))

        # Vẽ các popup cộng tài nguyên nổi lên
        for p in self.harvest_popups:
            txt_surf = FONT_SMALL.render(p["txt"], True, p["color"])
            self.screen.blit(txt_surf, (p["x"] - txt_surf.get_width()//2, p["y"]))

        # Vẽ Nhân vật Thị trưởng
        if not self.game_over_msg:
            self.player.draw(self.screen)

        # ==========================================================
        # 6. HIỂN THỊ CÁC PANEL TRÙM: EVENT MODAL / GAME OVER
        # ==========================================================
        
        # --- CHI TIẾT SỰ KIỆN LỰA CHỌN A/B ---
        if self.event_system.current_event:
            ev = self.event_system.current_event
            
            # Khung mờ đen phủ nhẹ
            modal_overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            modal_overlay.fill((0, 0, 0, 180))
            self.screen.blit(modal_overlay, (0, 0))
            
            # Vẽ Box biến cố ở trung tâm
            m_w, m_h = 560, 320
            m_x, m_y = WIDTH//2 - m_w//2, HEIGHT//2 - m_h//2
            
            pygame.draw.rect(self.screen, (25, 25, 30), (m_x + 6, m_y + 6, m_w, m_h), border_radius=10)
            pygame.draw.rect(self.screen, (45, 45, 50), (m_x, m_y, m_w, m_h), border_radius=10)
            pygame.draw.rect(self.screen, COLOR_GOLD, (m_x, m_y, m_w, m_h), 2, border_radius=10)
            
            lbl_ev_t = FONT_LARGE.render(f"BIẾN CỐ LỊCH SỬ: {ev['name'].upper()}", True, COLOR_GOLD)
            self.screen.blit(lbl_ev_t, (m_x + 20, m_y + 20))
            
            # Ngắt dòng mô tả biến cố
            ev_desc_lines = UIEngine.wrap_text(ev["desc"], FONT_STATUS, m_w - 40)
            desc_y = m_y + 60
            for line in ev_desc_lines:
                lbl_line = FONT_STATUS.render(line, True, COLOR_TEXT_LIGHT)
                self.screen.blit(lbl_line, (m_x + 20, desc_y))
                desc_y += 24
                
            # Khung vẽ hai lựa chọn
            y_choices = m_y + 130
            # Hộp Lựa chọn A
            pygame.draw.rect(self.screen, (35, 35, 40), (m_x + 20, y_choices, m_w - 40, 52), border_radius=6)
            pygame.draw.rect(self.screen, COLOR_MINT, (m_x + 20, y_choices, m_w - 40, 52), 1, border_radius=6)
            lbl_opt_a = FONT_SMALL.render(ev["choice_a"], True, COLOR_TEXT_LIGHT)
            self.screen.blit(lbl_opt_a, (m_x + 30, y_choices + 18))
            
            # Hộp Lựa chọn B
            pygame.draw.rect(self.screen, (35, 35, 40), (m_x + 20, y_choices + 62, m_w - 40, 52), border_radius=6)
            pygame.draw.rect(self.screen, COLOR_PINK, (m_x + 20, y_choices + 62, m_w - 40, 52), 1, border_radius=6)
            lbl_opt_b = FONT_SMALL.render(ev["choice_b"], True, COLOR_TEXT_LIGHT)
            self.screen.blit(lbl_opt_b, (m_x + 30, y_choices + 80))
            
            lbl_tip = FONT_SMALL.render("Nhấn phím [ A ] hoặc [ B ] trên bàn phím để lựa chọn hành động.", True, COLOR_GOLD_SOFT)
            self.screen.blit(lbl_tip, (m_x + m_w//2 - lbl_tip.get_width()//2, m_y + m_h - 32))

        # --- MÀN HÌNH GAME OVER / KẾT THÚC ---
        if self.game_over_msg:
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.fill((15, 15, 18))
            self.screen.blit(overlay, (0, 0))
            
            is_fail = "THẤT BẠI" in self.game_over_msg
            
            title_color = COLOR_RED if is_fail else COLOR_MINT
            title_text = self.game_over_msg
            
            lines_title = UIEngine.wrap_text(title_text, FONT_STATUS, WIDTH - 200)
            t_y = 60
            for t_line in lines_title:
                t_surf = FONT_STATUS.render(t_line, True, title_color)
                self.screen.blit(t_surf, (WIDTH//2 - t_surf.get_width()//2, t_y))
                t_y += 30
            
            lbl_timeline_title = FONT_STATUS.render("[ BIÊN NIÊN SỬ QUẢN TRỊ CỦA BẠN ]", True, COLOR_GOLD)
            self.screen.blit(lbl_timeline_title, (100, t_y + 30))
            
            y_hist = t_y + 65
            for idx, history_line in enumerate(self.eco.history_timeline[-9:]): 
                hist_surf = FONT_MED.render(f"• {history_line}", True, COLOR_TEXT_LIGHT)
                self.screen.blit(hist_surf, (120, y_hist))
                y_hist += 28
                
            restart_surf = FONT_STATUS.render("Nhấn phím [ R ] để khởi động lại guồng quay của bánh xe Lịch sử", True, COLOR_GOLD)
            self.screen.blit(restart_surf, restart_surf.get_rect(center=(WIDTH // 2, HEIGHT - 80)))

        # Luôn vẽ Guide lên trên cùng nếu đang mở
        self.guide.draw(self.screen)
        pygame.display.flip()

    async def run(self):
        while self.running:
            self.handle_input()
            self.update()
            self.render()
            self.clock.tick(FPS)
            await asyncio.sleep(0)
        pygame.quit()
        sys.exit()

async def main():
    game = GameManager()
    await game.run()

if __name__ == "__main__":
    asyncio.run(main())