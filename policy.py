import pygame

class Policy:
    def __init__(self, id_code, name, cost_desc, desc, effect_fn):
        self.id_code = id_code
        self.name = name
        self.cost_desc = cost_desc
        self.desc = desc
        self.effect_fn = effect_fn
        self.is_activated = False

class PolicyManager:
    def __init__(self):
        self.zone_infra = pygame.Rect(40, 145, 340, 420)   
        self.zone_policy = pygame.Rect(670, 145, 340, 420)  
        self.active_policies = []
        self._init_all_policies()

    def _init_all_policies(self):
        # Thiết lập hàm thực thi chính sách riêng biệt
        def p1_1(eco):
            if eco.food >= 10:
                eco.food -= 10
                eco.fire = min(100, eco.fire + 50)
                eco.add_log("[SẮC LỆNH] Tiếp thêm củi giúp lửa bùng cháy dữ dội!")
                return True
            return False

        def p1_2(eco):
            if eco.food >= 30:
                eco.food -= 30
                eco.food_income += 5
                eco.add_log("[SẮC LỆNH] Chế tạo gậy gộc săn bắn tốt hơn: Năng suất +5.")
                return True
            return False

        def p2_1(eco):
            # Cưỡng bức lao động
            eco.upheaval_tension = min(100, eco.upheaval_tension + 20)
            eco.food += int(eco.slaves * 0.5)
            eco.ore += int(eco.slaves * 0.5)
            eco.gold += int(eco.slaves * 0.3)
            eco.add_log("[SẮC LỆNH] Ép nô lệ lao động cật lực! Nhận nhiều tài nguyên nhưng phản kháng tăng.")
            return True

        def p2_2(eco):
            if eco.food >= 40:
                eco.food -= 40
                eco.upheaval_tension = max(0, eco.upheaval_tension - 20)
                eco.add_log("[SẮC LỆNH] Phát lương thực đầy đủ cho nô lệ. Độ phản kháng giảm mạnh.")
                return True
            return False

        def p3_1(eco):
            eco.tax_rate = min(80, eco.tax_rate + 10)
            eco.upheaval_tension = min(100, eco.upheaval_tension + 10)
            eco.add_log(f"[SẮC LỆNH] Tăng thuế suất lên {eco.tax_rate}%. Nông dân bất ổn!")
            return True

        def p3_2(eco):
            if eco.gold >= 150:
                eco.gold -= 150
                eco.food_income += 10
                eco.upheaval_tension = max(0, eco.upheaval_tension - 15)
                eco.add_log("[SẮC LỆNH] Đầu tư đắp đê ngăn lũ: Nông nghiệp +10/năm, bất ổn giảm.")
                return True
            return False

        def p4_1(eco):
            if eco.welfare_fund >= 30000:
                eco.welfare_fund -= 30000
                eco.equality = min(100, eco.equality + 15)
                eco.add_log("[SẮC LỆNH] Rút 30,000 Quỹ Phúc lợi hỗ trợ y tế giáo dục. Bình đẳng tăng.")
                return True
            return False

        def p4_2(eco):
            if eco.welfare_fund >= 10000:
                eco.welfare_fund -= 10000
                eco.welfare_income += 12000
                eco.add_log("[SẮC LỆNH] Phát động phong trào thi đua sản xuất: Phúc lợi +12,000/năm.")
                return True
            return False

        def p5_1(eco):
            if eco.knowledge >= 100:
                eco.knowledge -= 100
                eco.energy_income += 30
                eco.add_log("[SẮC LỆNH] Đồng bộ mạng lưới AI tối ưu hóa lưới điện: Năng lượng +30/năm.")
                return True
            return False

        def p5_2(eco):
            if eco.clean_energy >= 200:
                eco.clean_energy -= 200
                eco.civilization_level = min(100, eco.civilization_level + 20)
                eco.add_log("[SẮC LỆNH] Phóng vệ tinh thám hiểm không gian: Văn minh +20%.")
                return True
            return False

        self.policy_db = {
            1: [
                Policy("P1_1", "Tiếp củi giữ Lửa", "10 Lương thực", "Duy trì ngọn lửa sưởi ấm (+50% Lửa)", p1_1),
                Policy("P1_2", "Rèn gậy săn bắn", "30 Lương thực", "Cải tiến công cụ săn bắn (Năng suất +5)", p1_2)
            ],
            2: [
                Policy("P2_1", "Cưỡng bức lao động", "Miễn phí", "Nhận thêm tài nguyên tức thời nhưng Phản kháng +20%", p2_1),
                Policy("P2_2", "Phát cháo phát cơm", "40 Lương thực", "Giảm 20% Độ phản kháng của nô lệ", p2_2)
            ],
            3: [
                Policy("P3_1", "Tăng thuế suất thuế", "Miễn phí", "Thuế +10% (Tăng thu ngân sách, tăng bất ổn +10%)", p3_1),
                Policy("P3_2", "Đắp đê ngăn lũ", "150 Vàng", "Đầu tư hạ tầng nông nghiệp (Sản lượng +10, Bất ổn -15)", p3_2)
            ],
            4: [
                Policy("P4_1", "Cấp quỹ dân sinh", "30,000 Phúc lợi", "Trích Quỹ Phúc lợi hỗ trợ y tế, nhà ở công cộng (Bình đẳng +15%)", p4_1),
                Policy("P4_2", "Thi đua sản xuất", "10,000 Phúc lợi", "Nâng cao năng lực sản xuất (Quỹ Phúc lợi +12k/năm)", p4_2)
            ],
            5: [
                Policy("P5_1", "Hợp nhất mạng lưới", "100 Tri thức", "Tối ưu hóa năng lượng tự động hóa (Năng lượng +30/năm)", p5_1),
                Policy("P5_2", "Phóng tàu vũ trụ", "200 Năng lượng", "Khám phá các hành tinh mới (Văn minh đỉnh cao +20%)", p5_2)
            ]
        }

    def get_policies_for_chapter(self, tech_level):
        return self.policy_db.get(tech_level, [])

    def execute_policy_by_idx(self, idx, eco_state):
        policies = self.get_policies_for_chapter(eco_state.tech_level)
        if 0 <= idx < len(policies):
            p = policies[idx]
            # Gọi hàm thực thi và kiểm tra kết quả
            success = p.effect_fn(eco_state)
            if success:
                # Do chính sách có thể bấm lại nhiều lần để duy trì, ta không đánh dấu khóa vĩnh viễn
                p.is_activated = True
                eco_state.history_timeline.append(f"Năm {eco_state.turn}: Ban hành {p.name}.")
                return "SUCCESS"
        return "INVALID"

    def get_upgrade_info(self, eco_state):
        """Trả về thông tin nâng cấp Lực lượng sản xuất (Cơ sở hạ tầng) hiện tại"""
        lv = eco_state.tech_level
        if lv == 1:
            return {
                "name": "Chế tạo Cung tên & Trồng trọt",
                "desc": "Tích lũy lương thực để định cư, chuyển sang Đời II Chiếm hữu Nô lệ.",
                "cost": "200 Lương thực",
                "can_afford": eco_state.food >= 200
            }
        elif lv == 2:
            return {
                "name": "Rèn sắt & Đúc công cụ sắt",
                "desc": "Nô lệ làm việc không hiệu quả bằng công cụ sắt. Chuyển sang Đời III Phong kiến.",
                "cost": "100 Quặng + 150 Vàng",
                "can_afford": eco_state.ore >= 100 and eco_state.gold >= 150
            }
        elif lv == 3:
            return {
                "name": "Chế tạo Máy hơi nước & Hải trình",
                "desc": "Mở rộng giao thương, cách mạng hóa sức kéo công nghiệp. Chuyển sang Đời IV XHCN.",
                "cost": "800 Vàng",
                "can_afford": eco_state.gold >= 800
            }
        elif lv == 4:
            # Chương 4 có 3 bước nâng cấp để tăng tốc tích lũy Quỹ phúc lợi lên 1,000,000
            if eco_state.welfare_income < 10000:
                return {
                    "name": "Công nghiệp hóa Xanh",
                    "desc": "Thay thế nhà máy cũ bằng khu công-nông nghiệp xanh. Năng suất Phúc lợi +15,000/năm.",
                    "cost": "20,000 Quỹ Phúc lợi",
                    "can_afford": eco_state.welfare_fund >= 20000
                }
            elif eco_state.welfare_income < 50000:
                return {
                    "name": "Mạng lưới Điện toán Đám mây",
                    "desc": "Điều phối sản xuất vĩ mô tránh khủng hoảng thừa. Năng suất Phúc lợi +100,000/năm.",
                    "cost": "150,000 Quỹ Phúc lợi",
                    "can_afford": eco_state.welfare_fund >= 150000
                }
            else:
                return {
                    "name": "Trí tuệ Nhân tạo & Robot tự động",
                    "desc": "Giải phóng lao động chân tay. Năng suất Phúc lợi +500,000/năm.",
                    "cost": "600,000 Quỹ Phúc lợi",
                    "can_afford": eco_state.welfare_fund >= 600000
                }
        elif lv == 5:
            # Chương 5 nâng cấp để kích hoạt sản sinh Tri thức/Năng lượng
            if eco_state.energy_income < 40:
                return {
                    "name": "Trạm điện Mặt trời Không gian",
                    "desc": "Thu hoạch năng lượng sạch ngoài Trái Đất. Sản lượng +50 Năng lượng/năm.",
                    "cost": "150 Tri thức",
                    "can_afford": eco_state.knowledge >= 150
                }
            else:
                return {
                    "name": "Bộ não điện tử nhân loại",
                    "desc": "Hợp nhất AI toàn cầu hỗ trợ sáng tạo tối đa. Sản lượng +50 Tri thức/năm.",
                    "cost": "200 Năng lượng sạch",
                    "can_afford": eco_state.clean_energy >= 200
                }
        return None

    def execute_infra_upgrade(self, eco_state):
        """Thực thi nâng cấp Cơ sở hạ tầng kinh tế kỹ thuật"""
        lv = eco_state.tech_level
        info = self.get_upgrade_info(eco_state)
        if not info or not info["can_afford"]:
            return False

        if lv == 1:
            eco_state.food -= 200
            eco_state.tech_level = 2
            eco_state.food = 50
            eco_state.slaves = 30
            eco_state.gold = 0
            eco_state.ore = 0
            # Thiết lập năng suất đời 2
            eco_state.food_income = 15
            eco_state.ore_income = 10
            eco_state.gold_income = 5
            eco_state.add_log("[NÂNG CẤP] Chuyển dịch lên Chiếm hữu Nô lệ. Nô lệ bắt đầu lao dịch.")
            eco_state.history_timeline.append(f"Năm {eco_state.turn}: Nghiên cứu Nông nghiệp, bước sang thời chiếm hữu nô lệ.")
            
        elif lv == 2:
            eco_state.ore -= 100
            eco_state.gold -= 150
            eco_state.tech_level = 3
            # Thiết lập năng suất đời 3
            eco_state.food_income = 30
            eco_state.ore_income = 15
            eco_state.gold = 100
            eco_state.tax_rate = 20
            eco_state.add_log("[NÂNG CẤP] Công cụ bằng Sắt xuất hiện! Chuyển dịch sang chế độ Phong kiến.")
            eco_state.history_timeline.append(f"Năm {eco_state.turn}: Đúc thành công công cụ sắt, chuyển lên chế độ Phong kiến.")
            
        elif lv == 3:
            eco_state.gold -= 800
            eco_state.tech_level = 4
            # Thiết lập năng suất đời 4
            eco_state.welfare_fund = 0
            eco_state.equality = 50
            eco_state.welfare_income = 2000
            eco_state.food_income = 40
            eco_state.ore_income = 30
            eco_state.add_log("[NÂNG CẤP] Chuyển đổi cách mạng: Thiết lập hình thái Xã hội Chủ nghĩa.")
            eco_state.history_timeline.append(f"Năm {eco_state.turn}: Phát minh Máy hơi nước, thiết lập hình thái Xã hội Chủ nghĩa.")
            
        elif lv == 4:
            # Các bước nâng cấp công nghiệp phụ trong đời 4
            if eco_state.welfare_income < 10000:
                eco_state.welfare_fund -= 20000
                eco_state.welfare_income = 15000
                eco_state.add_log("[NÂNG CẤP] Kích hoạt Công nghiệp hóa Xanh: Năng suất tăng vọt.")
            elif eco_state.welfare_income < 50000:
                eco_state.welfare_fund -= 150000
                eco_state.welfare_income = 100000
                eco_state.add_log("[NÂNG CẤP] Vận hành mạng Điện toán đám mây quốc gia.")
            else:
                eco_state.welfare_fund -= 600000
                eco_state.welfare_income = 500000
                eco_state.add_log("[NÂNG CẤP] Robot và AI tự động hóa hoàn toàn lực lượng sản xuất.")
            eco_state.history_timeline.append(f"Năm {eco_state.turn}: Nâng cấp Lực lượng sản xuất Đời IV.")
            
        elif lv == 5:
            # Các bước nâng cấp trong đời 5
            if eco_state.knowledge >= 150 and eco_state.energy_income < 40:
                eco_state.knowledge -= 150
                eco_state.energy_income = 60
                eco_state.add_log("[NÂNG CẤP] Vận hành Trạm điện Mặt trời Không gian: +60 Năng lượng/năm.")
            elif eco_state.clean_energy >= 200:
                eco_state.clean_energy -= 200
                eco_state.knowledge_income = 50
                eco_state.add_log("[NÂNG CẤP] Bộ não điện tử hợp nhất nhân loại: +50 Tri thức/năm.")
            eco_state.history_timeline.append(f"Năm {eco_state.turn}: Nâng cấp Lực lượng sản xuất Đời V.")
            
        return True