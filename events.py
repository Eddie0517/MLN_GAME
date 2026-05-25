import random

class EventEngine:
    def __init__(self):
        self.current_event = None
        self.pool = [
            {
                "name": "Khủng hoảng Tài chính",
                "desc": "Kinh tế toàn cầu suy thoái, cắt giảm nhân sự lớn.",
                "eff_income": -12, "eff_work": -10, "eff_cap": -15, "eff_unemp": 15, "eff_ineq": 5
            },
            {
                "name": "Bùng nổ Startup Số",
                "desc": "Gia tăng dòng vốn đầu tư công nghệ vào giới chủ.",
                "eff_income": 18, "eff_work": -5, "eff_cap": 20, "eff_unemp": -5, "eff_ineq": 10
            },
            {
                "name": "Đình công Giai cấp",
                "desc": "Công nhân bãi công yêu cầu tối ưu phúc lợi lao động.",
                "eff_income": -15, "eff_work": 25, "eff_cap": -20, "eff_unemp": 0, "eff_ineq": -10
            }
        ]

    def trigger_annual_event(self, eco_state):
        # 50% Xác suất nổ ra biến cố ngẫu nhiên để tăng tính Uncertainty cho game
        if random.random() < 0.50:
            self.current_event = random.choice(self.pool)
            eco_state.income += self.current_event["eff_income"]
            eco_state.worker_support += self.current_event["eff_work"]
            eco_state.capitalist_support += self.current_event["eff_cap"]
            eco_state.unemployment += self.current_event["eff_unemp"]
            eco_state.inequality += self.current_event["eff_ineq"]
            eco_state.add_log(f"[BIẾN CỐ] Xảy ra thiên tai/sự kiện: {self.current_event['name']}")
            eco_state.history_timeline.append(f"Năm {eco_state.turn}: Đối mặt biến cố {self.current_event['name']}.")
        else:
            self.current_event = None