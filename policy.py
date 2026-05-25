from config import COLOR_MINT, COLOR_TEXT_DARK

class Policy:
    def __init__(self, id_code, name, cost, req_tech, effects, desc):
        self.id_code = id_code
        self.name = name
        self.cost = cost
        self.req_tech = req_tech
        self.effects = effects
        self.desc = desc
        self.is_activated = False

class PolicyManager:
    def __init__(self):
        # Chuyển kích thước Box lên rộng 340 để hiển thị thoải mái chữ tiếng Việt
        import pygame
        self.zone_infra = pygame.Rect(60, 160, 340, 200)   
        self.zone_policy = pygame.Rect(650, 160, 340, 200)  
        
        self.policies = [
            Policy(
                "P1", "Thuế Livestream & AI Shop", 40, 3,
                {"income": 30, "capitalist_support": 15, "worker_support": -15, "inequality": 5},
                "Tăng thu nhập ở Đời III nhưng đẩy cao mâu thuẫn giai cấp lao động."
            ),
            Policy(
                "P2", "Luật Phúc Lợi Công Nhân", 35, 1,
                {"income": -5, "capitalist_support": -20, "worker_support": 25, "inequality": -15},
                "Bảo vệ nghiệp đoàn, giảm bất bình đẳng nhưng giới chủ phản kháng rút vốn."
            )
        ]

    def execute_infra_upgrade(self, eco_state):
        if eco_state.tech_level == 1 and eco_state.gold >= 60:
            eco_state.gold -= 60
            eco_state.tech_level = 2
            eco_state.income += 15
            eco_state.add_log("[NEWS] Cơ sở Hạ tầng chuyển sang Công nghiệp hóa.")
            eco_state.history_timeline.append(f"Năm {eco_state.turn}: Cải cách nâng cấp lên Hạ tầng Công nghiệp.")
            return True
        elif eco_state.tech_level == 2 and eco_state.gold >= 120:
            eco_state.gold -= 120
            eco_state.tech_level = 3
            eco_state.income += 35
            eco_state.unemployment += 10
            eco_state.add_log("[NEWS] Đạt đỉnh cao hạ tầng: Kỷ nguyên AI & Kinh tế tri thức.")
            eco_state.history_timeline.append(f"Năm {eco_state.turn}: Chuyển mình vượt bậc lên Kỷ nguyên AI.")
            return True
        return False

    def execute_policy_by_id(self, policy_id, eco_state):
        for p in self.policies:
            if p.id_code == policy_id and not p.is_activated:
                if eco_state.gold >= p.cost:
                    eco_state.gold -= p.cost
                    p.is_activated = True
                    
                    if p.id_code == "P1" and eco_state.tech_level < 3:
                        return "CRISIS_TAX"
                    
                    eco_state.income += p.effects.get("income", 0)
                    eco_state.worker_support += p.effects.get("worker_support", 0)
                    eco_state.capitalist_support += p.effects.get("capitalist_support", 0)
                    eco_state.inequality += p.effects.get("inequality", 0)
                    
                    eco_state.add_log(f"[POLICY] Ban hành luật pháp: {p.name}")
                    eco_state.history_timeline.append(f"Năm {eco_state.turn}: Ban hành {p.name}.")
                    return "SUCCESS"
        return "INVALID"