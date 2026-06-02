class EconomyState:
    def __init__(self):
        self.turn = 1
        self.tech_level = 1  # 1: Công xã Nguyên thủy, 2: Chiếm hữu Nô lệ, 3: Phong kiến, 4: XHCN, 5: Thế giới ngày mai
        self.upheaval_tension = 0  # Chỉ số Bất ổn / Phản kháng (%)
        
        # --- TÀI NGUYÊN ĐỘNG THEO CHƯƠNG ---
        # Chương 1
        self.food = 50
        self.fire = 100      # Phần trăm duy trì lửa (%)
        
        # Chương 2
        self.ore = 0         # Khoáng sản (đồng/sắt)
        self.gold = 0        # Vàng (Ngân sách)
        self.slaves = 30     # Lực lượng nô lệ (đơn vị)
        
        # Chương 3
        self.tax_rate = 20   # Thuế suất (%)
        
        # Chương 4
        self.welfare_fund = 0  # Quỹ Phúc lợi Công cộng
        self.equality = 50     # Chỉ số Bình đẳng Xã hội (%)
        
        # Chương 5
        self.clean_energy = 0   # Năng lượng sạch
        self.knowledge = 0      # Tri thức
        self.civilization_level = 0 # Chỉ số văn minh (%)
        
        # Năng suất sản xuất cơ bản hàng năm (Income)
        self.food_income = 15
        self.ore_income = 0
        self.gold_income = 0
        self.welfare_income = 2000
        self.energy_income = 0
        self.knowledge_income = 0
        
        # Chỉ số lịch sử
        self.history_timeline = ["Năm 1: Khởi đầu Công xã Nguyên thủy bình đẳng."]
        self.logs = ["Xã hội nguyên thủy hoang sơ bắt đầu. Hãy tích lũy lương thực!"]
        
        # Thuộc tính tương thích ngược tránh lỗi AttributeError
        self.unemployment = 0
        self.inequality = 0
        self.worker_support = 70
        self.capitalist_support = 60
        self.current_ideology = "Công xã Nguyên thủy"

    def add_log(self, text):
        self.logs.append(text)
        if len(self.logs) > 4: 
            self.logs.pop(0)

    def get_average_support(self):
        """Trả về lòng dân trung bình, tương đương 100 - chỉ số phản kháng/bất ổn"""
        return 100 - self.upheaval_tension

    def get_chapter_name(self):
        names = {
            1: "Công xã Nguyên thủy",
            2: "Chiếm hữu Nô lệ",
            3: "Phong kiến",
            4: "Xã hội Chủ nghĩa",
            5: "Kỷ nguyên Tri thức & Tự động hóa"
        }
        return names.get(self.tech_level, "Không xác định")

    def apply_simulation_feedback_loops(self):
        """Tính toán biến động chỉ số hàng năm dựa trên hình thái xã hội"""
        if self.tech_level == 1:
            self.current_ideology = "Công xã Nguyên thủy"
            self.upheaval_tension = 0
            self.worker_support = 100
            self.capitalist_support = 100
            
            # Đốt củi sưởi ấm giảm dần
            self.fire = max(0, self.fire - 15)
            if self.fire == 0:
                self.add_log("[CẢNH BÁO] Lửa đã tắt! Năng suất săn hái giảm mạnh.")
                
        elif self.tech_level == 2:
            self.current_ideology = "Chiếm hữu Nô lệ"
            self.worker_support = 100 - self.upheaval_tension
            self.capitalist_support = 80
            
            # Tiêu thụ lương thực bởi nô lệ
            food_needed = self.slaves
            if self.food < food_needed:
                self.upheaval_tension = min(100, self.upheaval_tension + 15)
                self.slaves = max(10, self.slaves - 5)
                self.add_log("[WARN] Thiếu lương thực! Nô lệ đói khát và phản kháng mạnh mẽ.")
            else:
                self.food -= food_needed
                # Nếu được ăn no, phản kháng giảm nhẹ
                self.upheaval_tension = max(0, self.upheaval_tension - 4)
                
        elif self.tech_level == 3:
            self.current_ideology = "Phong kiến"
            # Lòng dân phụ thuộc thuế
            self.worker_support = max(0, 100 - int(self.tax_rate * 1.5))
            self.capitalist_support = 70
            
            # Độ bất ổn tương tác với thuế suất
            if self.tax_rate > 35:
                self.upheaval_tension = min(100, self.upheaval_tension + 8)
                self.add_log("[WARN] Sưu thuế quá nặng làm nông dân oán hận!")
            else:
                self.upheaval_tension = max(0, self.upheaval_tension - 3)
                
        elif self.tech_level == 4:
            self.current_ideology = "Xã hội Chủ nghĩa"
            # Càng bình đẳng lòng dân càng cao
            self.worker_support = self.equality
            self.capitalist_support = max(0, 100 - self.equality)
            
            # Bất ổn giảm khi bình đẳng tăng
            self.upheaval_tension = max(0, int(100 - self.equality))
            
            # Kích thích sản xuất xã hội chủ nghĩa
            self.welfare_fund += self.welfare_income
            
        elif self.tech_level == 5:
            self.current_ideology = "Kỷ nguyên Tri thức & Tự động hóa"
            self.upheaval_tension = 0
            self.worker_support = 100
            self.capitalist_support = 100
            
            # Chuyển đổi năng lượng sạch và tri thức thành mức độ văn minh
            civ_gain = int((self.clean_energy + self.knowledge) / 100)
            self.civilization_level = min(100, self.civilization_level + max(1, civ_gain))

    def process_next_turn(self):
        self.turn += 1
        
        # Thu hoạch tài nguyên hàng năm
        if self.tech_level == 1:
            if self.fire > 0:
                self.food += self.food_income
                self.add_log(f"[NĂM MỚI] Săn bắn thu hoạch được {self.food_income} Lương thực.")
            else:
                gained = max(2, self.food_income // 3)
                self.food += gained
                self.add_log(f"[NĂM MỚI] Lửa tắt. Chỉ săn được {gained} Lương thực.")
                
        elif self.tech_level == 2:
            # Năng suất từ nô lệ
            earned_food = int(self.slaves * 0.5)
            earned_ore = int(self.slaves * 0.3)
            earned_gold = int(self.slaves * 0.2)
            
            self.food += earned_food
            self.ore += earned_ore
            self.gold += earned_gold
            self.add_log(f"[NĂM MỚI] Nô lệ sản xuất: +{earned_food} Thức ăn, +{earned_ore} Quặng, +{earned_gold} Vàng.")
            
        elif self.tech_level == 3:
            # Sản xuất nông nghiệp phong kiến
            base_harvest = 40 + self.food_income
            tax_gold = int(base_harvest * (self.tax_rate / 100))
            
            self.food += (base_harvest - tax_gold)
            self.gold += tax_gold
            self.ore += self.ore_income
            self.add_log(f"[NĂM MỚI] Nông dân nộp thuế bao gồm: +{tax_gold} Vàng. Giữ lại ăn: +{base_harvest - tax_gold} Thức ăn.")
            
        elif self.tech_level == 4:
            # Năng suất công nghiệp xã hội chủ nghĩa
            self.food += self.food_income
            self.ore += self.ore_income
            self.gold += 100  # Ngân quỹ phụ
            self.add_log(f"[NĂM MỚI] Kế hoạch sản xuất tập thể: +{self.food_income} Thức ăn, +{self.welfare_income} Quỹ Phúc lợi.")
            
        elif self.tech_level == 5:
            # Tự động hóa sản sinh Năng lượng và Tri thức
            self.clean_energy += self.energy_income
            self.knowledge += self.knowledge_income
            self.add_log(f"[NĂM MỚI] Hệ thống tự động: +{self.energy_income} Năng lượng sạch, +{self.knowledge_income} Tri thức.")
            
        # Áp dụng feedback loop
        self.apply_simulation_feedback_loops()
        
        # Đảm bảo các chỉ số nằm trong biên an toàn
        self.upheaval_tension = max(0, min(100, self.upheaval_tension))
        self.equality = max(0, min(100, self.equality))
        self.civilization_level = max(0, min(100, self.civilization_level))
        self.fire = max(0, min(100, self.fire))