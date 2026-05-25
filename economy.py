class EconomyState:
    def __init__(self):
        self.turn = 1
        self.gold = 100
        self.income = 15
        self.tech_level = 1  # 1: Nông nghiệp, 2: Công nghiệp, 3: Kinh tế số & AI
        
        # Chỉ số kinh tế xã hội phức hợp
        self.unemployment = 10
        self.inequality = 20
        
        # Nhóm lợi ích phe phái (Factions)
        self.worker_support = 70
        self.capitalist_support = 60
        
        # --- TÍNH NĂNG MỚI: QUÁN TÍNH LỊCH SỬ & ÁP LỰC NGẦM (HISTORICAL MOMENTUM) ---
        self.revolution_tension = 0  # Điểm tích lũy căng thẳng cách mạng
        self.capital_flight_risk = 0 # Nguy cơ giới chủ rút vốn đầu tư khỏi quốc gia
        self.current_ideology = "Dân Chủ Xã Hội"
        
        # Hệ thống lưu vết lịch sử (Timeline History)
        self.history_timeline = ["Năm 1: Khởi đầu mô hình Dân Chủ Xã Hội."]
        self.logs = ["Hệ thống khởi tạo thành công. Chào mừng Thị trưởng!"]

    def add_log(self, text):
        self.logs.append(text)
        if len(self.logs) > 4: self.logs.pop(0)

    def get_average_support(self):
        return int((self.worker_support + self.capitalist_support) / 2)

    def update_ideology_engine(self):
        """TÍNH NĂNG MỚI: Động cơ nhận diện Hệ tư tưởng tự động (Ideology Engine)"""
        old_ideology = self.current_ideology
        
        if self.tech_level == 3 and self.capitalist_support >= 75 and self.worker_support <= 40:
            self.current_ideology = "Chủ Nghĩa Độc Tài AI (Technocracy)"
        elif self.worker_support >= 75 and self.capitalist_support <= 40:
            self.current_ideology = "Chủ Nghĩa Xã Hội Thắp Sáng"
        elif self.capitalist_support >= 75 and self.worker_support >= 50:
            self.current_ideology = "Chủ Nghĩa Tư Bản Tự Do"
        else:
            self.current_ideology = "Dân Chủ Xã Hội"
            
        if old_ideology != self.current_ideology:
            self.add_log(f"[HỆ TƯ TƯỞNG] Xã hội dịch chuyển sang: {self.current_ideology}")
            self.history_timeline.append(f"Năm {self.turn}: Chuyển dịch tư tưởng thành {self.current_ideology}.")

    def apply_simulation_feedback_loops(self):
        """Mở rộng Feedback Loops: Thêm cơ chế tích tụ áp lực ngầm và phản công phe phái"""
        # 1. Automation Loop
        if self.tech_level == 3:
            self.unemployment = min(100, self.unemployment + 4)
            self.add_log("[ALERT] Tự động hóa bằng AI làm gia tăng Thất nghiệp!")

        # 2. Quán tính lịch sử: Tích lũy căng thẳng khi Bất bình đẳng / Thất nghiệp kéo dài
        if self.inequality > 50 or self.unemployment > 35:
            self.revolution_tension += 4  # Căng thẳng tích tụ, không mất đi ngay lập tức
            self.add_log(f"[WARN] Căng thẳng xã hội đang tích tụ (Tension: {self.revolution_tension})!")
        else:
            self.revolution_tension = max(0, self.revolution_tension - 2) # Giảm nhẹ nếu quản lý tốt

        # 3. Áp lực phản kháng (Counter-Pressure): Giới chủ rút vốn (Capital Flight) khi bị ép quá mạnh
        if self.worker_support > 80 and self.capitalist_support < 35:
            self.capital_flight_risk += 5
            self.income = max(5, self.income - 4) # Giới chủ đình trệ sản xuất, kéo sụt thu nhập quốc gia
            self.add_log("[NEWS] Giới Tư Bản cắt giảm đầu tư để phản đối chính sách thiên vị Công nhân!")
        else:
            self.capital_flight_risk = max(0, self.capital_flight_risk - 3)

    def process_next_turn(self):
        self.turn += 1
        self.gold += self.income
        
        self.apply_simulation_feedback_loops()
        self.update_ideology_engine()
        
        # Đảm bảo các chỉ số nằm trong biên an toàn
        self.worker_support = max(0, min(100, self.worker_support))
        self.capitalist_support = max(0, min(100, self.capitalist_support))
        self.unemployment = max(0, min(100, self.unemployment))
        self.inequality = max(0, min(100, self.inequality))