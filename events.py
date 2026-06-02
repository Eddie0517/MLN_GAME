import random

class EventEngine:
    def __init__(self):
        self.current_event = None
        
        # Kho sự kiện theo từng chương (Chương 1 đến 5)
        self.events_db = {
            1: [
                {
                    "name": "Bầy thú tấn công",
                    "desc": "Một bầy sói đói hoang dã bao vây hang đá của bầy người.",
                    "choice_a": "A: Dùng Lửa xua đuổi bầy thú (Tốn 30 Lửa)",
                    "choice_b": "B: Cả bầy trốn chạy sâu vào hang (Tốn 15 Lương thực, Lửa giảm 40%)",
                    "apply_a": lambda eco: self._apply_primitive_defense(eco, True),
                    "apply_b": lambda eco: self._apply_primitive_defense(eco, False)
                },
                {
                    "name": "Bão tuyết tràn về",
                    "desc": "Một đợt rét lạnh kỷ lục bao trùm toàn bộ cánh rừng.",
                    "choice_a": "A: Chất củi duy trì lửa ấm (Tốn 20 Lương thực, lửa tăng +30%)",
                    "choice_b": "B: Để ngọn lửa tự tàn cứu thức ăn (Lửa về 10%, năng suất giảm năm tới)",
                    "apply_a": lambda eco: self._apply_blizzard(eco, True),
                    "apply_b": lambda eco: self._apply_blizzard(eco, False)
                }
            ],
            2: [
                {
                    "name": "Nô lệ trốn chạy",
                    "desc": "Một nhóm nô lệ bỏ trốn khỏi công trường xây dựng kênh dẫn nước.",
                    "choice_a": "A: Truy đuổi nghiêm khắc (Tốn 20 Vàng, phản kháng nô lệ +15%)",
                    "choice_b": "B: Bỏ qua chấp nhận tổn thất (Nô lệ -5 người, phản kháng giảm -10%)",
                    "apply_a": lambda eco: self._apply_slave_escape(eco, True),
                    "apply_b": lambda eco: self._apply_slave_escape(eco, False)
                },
                {
                    "name": "Thú rừng quấy phá đồng ruộng",
                    "desc": "Thú hoang dã phá phách diện tích cây trồng lúa nước.",
                    "choice_a": "A: Tăng cường tuần tra ép nô lệ canh gác (Lòng dân chủ nô +5, nô lệ phản kháng +10%)",
                    "choice_b": "B: Sử dụng lương thực dụ thú đi chỗ khác (Tốn 25 Lương thực)",
                    "apply_a": lambda eco: self._apply_beast_farm(eco, True),
                    "apply_b": lambda eco: self._apply_beast_farm(eco, False)
                }
            ],
            3: [
                {
                    "name": "Nông dân xin khẩn hoang",
                    "desc": "Một nhóm nông dân xin khẩn hoang vùng đất hoang dã phía Tây.",
                    "choice_a": "A: Đồng ý và giảm thuế năm đầu (Bất ổn -15%, sản lượng thức ăn +15/năm)",
                    "choice_b": "B: Từ chối vì sợ mất kiểm soát địa giới (Bất ổn +20% do bất mãn)",
                    "apply_a": lambda eco: self._apply_reclaim_land(eco, True),
                    "apply_b": lambda eco: self._apply_reclaim_land(eco, False)
                },
                {
                    "name": "Lũ lụt sông lớn",
                    "desc": "Mưa bão lớn gây vỡ đê sông Hồng tàn phá đất nông nghiệp của lãnh chúa.",
                    "choice_a": "A: Chi ngân quỹ cứu trợ nhân dân (Tốn 100 Vàng, độ bất ổn giảm -20%)",
                    "choice_b": "B: Tự khắc phục, ưu tiên trữ lương thực (Mất 100 Lương thực, bất ổn tăng +30%)",
                    "apply_a": lambda eco: self._apply_flood_crisis(eco, True),
                    "apply_b": lambda eco: self._apply_flood_crisis(eco, False)
                }
            ],
            4: [
                {
                    "name": "Nhà máy xuất sắc",
                    "desc": "Một nhà máy cơ khí đạt danh hiệu xuất sắc, năng suất tăng vọt!",
                    "choice_a": "A: Khen thưởng nâng cao điều kiện lao động (Tốn 15,000 Quỹ Phúc lợi, Bình đẳng +10%)",
                    "choice_b": "B: Điều phối hỗ trợ công nghệ cho nông nghiệp (Bình đẳng +5%, thức ăn +15/năm)",
                    "apply_a": lambda eco: self._apply_factory_award(eco, True),
                    "apply_b": lambda eco: self._apply_factory_award(eco, False)
                },
                {
                    "name": "Khủng hoảng kinh tế tư bản ngoài",
                    "desc": "Thế giới tư bản phương Tây khủng hoảng thừa, ảnh hưởng giao thương xuất nhập khẩu.",
                    "choice_a": "A: Tăng cường tự lực cánh sinh sản xuất trong nước (Bình đẳng +5%, tốn 5,000 Phúc lợi)",
                    "choice_b": "B: Bán tháo hàng tồn giảm giá sốc (Tốn 15,000 Quỹ Phúc lợi, Bình đẳng -5%)",
                    "apply_a": lambda eco: self._apply_capitalist_crisis(eco, True),
                    "apply_b": lambda eco: self._apply_capitalist_crisis(eco, False)
                }
            ],
            5: [
                {
                    "name": "Phản vật chất xanh",
                    "desc": "Đột phá khoa học tạo ra nguồn năng lượng phản vật chất vô hạn.",
                    "choice_a": "A: Phục vụ dân sự thành thị (Năng lượng +50, Văn minh +10%)",
                    "choice_b": "B: Nghiên cứu thám hiểm vũ trụ sâu (Tri thức +50, Năng lượng +20)",
                    "apply_a": lambda eco: self._apply_antimatter(eco, True),
                    "apply_b": lambda eco: self._apply_antimatter(eco, False)
                },
                {
                    "name": "Bão mặt trời cực mạnh",
                    "desc": "Bão Mặt Trời đe dọa làm tê liệt hệ thống thông tin AI vệ tinh.",
                    "choice_a": "A: Bật màn chắn bảo vệ không gian tự động (Tốn 40 Năng lượng sạch)",
                    "choice_b": "B: Chấp nhận mất dữ liệu khôi phục sau (Mất 40 Tri thức tích lũy)",
                    "apply_a": lambda eco: self._apply_solar_flare(eco, True),
                    "apply_b": lambda eco: self._apply_solar_flare(eco, False)
                }
            ]
        }

    # --- CÁC HÀM XỬ LÝ KẾT QUẢ SỰ KIỆN ---
    def _apply_primitive_defense(self, eco, opt_a):
        if opt_a:
            if eco.fire >= 30:
                eco.fire -= 30
                eco.add_log("[EVENT] Dùng lửa xua đuổi bầy sói thành công dũng cảm!")
            else:
                eco.food = max(0, eco.food - 15)
                eco.fire = max(0, eco.fire - 40)
                eco.add_log("[EVENT] Lửa không đủ mạnh! Sói quấy phá mất lương thực.")
        else:
            eco.food = max(0, eco.food - 15)
            eco.fire = max(0, eco.fire - 40)
            eco.add_log("[EVENT] Bầy người trốn trong hang đá. Lửa lụi tàn và mất thức ăn.")

    def _apply_blizzard(self, eco, opt_a):
        if opt_a:
            if eco.food >= 20:
                eco.food -= 20
                eco.fire = min(100, eco.fire + 30)
                eco.add_log("[EVENT] Vượt qua bão tuyết bằng củi đốt dồi dào.")
            else:
                eco.fire = 10
                eco.add_log("[EVENT] Không đủ lương thực trữ để nhóm củi. Lửa sắp tắt!")
        else:
            eco.fire = 10
            eco.add_log("[EVENT] Để ngọn lửa lụi tàn, bầy người lạnh lẽo co ro.")

    def _apply_slave_escape(self, eco, opt_a):
        if opt_a:
            eco.gold = max(0, eco.gold - 20)
            eco.upheaval_tension = min(100, eco.upheaval_tension + 15)
            eco.add_log("[EVENT] Truy quét ráo riết bắt lại nô lệ. Phản kháng tăng.")
        else:
            eco.slaves = max(5, eco.slaves - 5)
            eco.upheaval_tension = max(0, eco.upheaval_tension - 10)
            eco.add_log("[EVENT] Chấp nhận mất nô lệ. Lòng nô lệ bớt phẫn uất.")

    def _apply_beast_farm(self, eco, opt_a):
        if opt_a:
            eco.upheaval_tension = min(100, eco.upheaval_tension + 10)
            eco.add_log("[EVENT] Ép nô lệ gác đêm xua thú dữ. Nô lệ phẫn nộ căng thẳng.")
        else:
            eco.food = max(0, eco.food - 25)
            eco.add_log("[EVENT] Dùng 25 Lương thực nhử thú hoang dã tránh xa ruộng vườn.")

    def _apply_reclaim_land(self, eco, opt_a):
        if opt_a:
            eco.upheaval_tension = max(0, eco.upheaval_tension - 15)
            eco.food_income += 15
            eco.add_log("[EVENT] Cho phép khai hoang & miễn thuế: Sản xuất lương thực +15/năm.")
        else:
            eco.upheaval_tension = min(100, eco.upheaval_tension + 20)
            eco.add_log("[EVENT] Từ chối khẩn hoang. Nông dân phẫn nộ vì bị kìm hãm.")

    def _apply_flood_crisis(self, eco, opt_a):
        if opt_a:
            eco.gold = max(0, eco.gold - 100)
            eco.upheaval_tension = max(0, eco.upheaval_tension - 20)
            eco.add_log("[EVENT] Chi ngân khố cứu trợ lương thực. Dân chúng ca tụng hiền minh.")
        else:
            eco.food = max(0, eco.food - 100)
            eco.upheaval_tension = min(100, eco.upheaval_tension + 30)
            eco.add_log("[EVENT] Không cứu trợ. Nông dân mất mùa đói kém bất ổn tăng vọt.")

    def _apply_factory_award(self, eco, opt_a):
        if opt_a:
            if eco.welfare_fund >= 15000:
                eco.welfare_fund -= 15000
                eco.equality = min(100, eco.equality + 10)
                eco.welfare_income += 5000
                eco.add_log("[EVENT] Trích 15,000 Phúc lợi cải thiện nhà xưởng: Bình đẳng +10%.")
            else:
                eco.equality = max(0, eco.equality - 5)
                eco.add_log("[EVENT] Hứa thưởng nhưng không đủ tiền! Nhân viên thất vọng.")
        else:
            eco.equality = min(100, eco.equality + 5)
            eco.food_income += 15
            eco.add_log("[EVENT] Chuyển giao công nghệ hỗ trợ nông nghiệp vùng sâu xa.")

    def _apply_capitalist_crisis(self, eco, opt_a):
        if opt_a:
            eco.welfare_fund = max(0, eco.welfare_fund - 5000)
            eco.equality = min(100, eco.equality + 5)
            eco.add_log("[EVENT] Đóng cửa biên giới tự cung tự cấp. Giữ được sự ổn định.")
        else:
            eco.welfare_fund = max(0, eco.welfare_fund - 15000)
            eco.equality = max(0, eco.equality - 5)
            eco.add_log("[EVENT] Bán tháo hạ giá gây thiệt hại lớn cho quỹ phúc lợi quốc gia.")

    def _apply_antimatter(self, eco, opt_a):
        eco.clean_energy += 50
        eco.civilization_level = min(100, eco.civilization_level + 10)
        if opt_a:
            eco.add_log("[EVENT] Phát triển lò năng lượng dân sinh: Năng lượng +50, Văn minh +10%.")
        else:
            eco.knowledge += 50
            eco.add_log("[EVENT] Phục vụ thám hiểm thiên hà: Tri thức +50, Năng lượng +20.")

    def _apply_solar_flare(self, eco, opt_a):
        if opt_a:
            if eco.clean_energy >= 40:
                eco.clean_energy -= 40
                eco.add_log("[EVENT] Khởi động lá chắn bảo vệ thành công rực rỡ.")
            else:
                eco.knowledge = max(0, eco.knowledge - 40)
                eco.add_log("[EVENT] Không đủ năng lượng chạy lá chắn! Bão mặt trời xóa dữ liệu.")
        else:
            eco.knowledge = max(0, eco.knowledge - 40)
            eco.add_log("[EVENT] Bão Mặt trời làm gián đoạn lưới thông tin. Tri thức -40.")

    # --- GIAO DIỆN CHUNG KÍCH HOẠT ---
    def trigger_annual_event(self, eco_state):
        # 40% Xác suất xảy ra biến cố ngẫu nhiên hàng năm
        if random.random() < 0.40:
            chapter_events = self.events_db.get(eco_state.tech_level, [])
            if chapter_events:
                self.current_event = random.choice(chapter_events)
                eco_state.add_log(f"[BIẾN CỐ] Đang xảy ra: {self.current_event['name']}")
                return True
        self.current_event = None
        return False

    def resolve_event(self, choice_letter, eco_state):
        if not self.current_event:
            return False
            
        if choice_letter == 'A':
            self.current_event["apply_a"](eco_state)
            eco_state.history_timeline.append(f"Năm {eco_state.turn}: Chọn quyết định A khi đối mặt {self.current_event['name']}.")
        elif choice_letter == 'B':
            self.current_event["apply_b"](eco_state)
            eco_state.history_timeline.append(f"Năm {eco_state.turn}: Chọn quyết định B khi đối mặt {self.current_event['name']}.")
        
        self.current_event = None
        return True