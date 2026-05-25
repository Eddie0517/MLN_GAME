import pygame
import os
import math  # Thêm thư viện math để dùng hàm sin
from config import COLOR_SHADOW, WIDTH, HEIGHT

class Player:
    def __init__(self):
        self.x = 525
        self.y = 480
        self.speed = 6
        self.size = 110

        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "player.png")

        try:
            raw_sprite = pygame.image.load(image_path).convert_alpha()
            self.sprite = pygame.transform.scale(raw_sprite, (self.size, self.size))
        except Exception as e:
            print(f"[CẢNH BÁO] Không tìm thấy file 'player.png' tại: {image_path}. Lỗi: {e}")
            self.sprite = None
            
        self.animation_timer = 0  # Biến đếm thời gian dùng làm mốc nhấp nhô

    def move(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]: self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: self.y += self.speed

        self.x = max(40, min(WIDTH - 40, self.x))
        self.y = max(145, min(HEIGHT - 65, self.y))

        # Tăng biến đếm thời gian liên tục khi game chạy
        self.animation_timer += 0.1 

    def get_rect(self):
        return pygame.Rect(self.x - self.size//2, self.y - self.size//2, self.size, self.size)

    def draw(self, screen):
        # Tính toán độ nhấp nhô hình sin (Biên độ 6 pixel, tốc độ phụ thuộc vào animation_timer)
        y_offset = math.sin(self.animation_timer) * 1
        
        # 1. Vẽ bóng đổ: Giữ cố định dưới mặt đất (không nhấp nhô theo người), nhưng co giãn nhẹ theo nhịp
        # Khi nhân vật bay lên cao (y_offset âm), bóng đổ sẽ nhỏ lại một chút để tạo chiều sâu 3D
        shadow_scale = max(36, 48 + int(y_offset * 0.8))
        shadow_x = self.x - shadow_scale // 2
        pygame.draw.ellipse(screen, COLOR_SHADOW, (shadow_x, self.y + 45, shadow_scale, 12))
        
        # 2. Vẽ nhân vật: Cộng thêm y_offset để tạo hiệu ứng nhấp nhô
        render_y = self.y - self.size//2 + y_offset
        
        if self.sprite:
            screen.blit(self.sprite, (self.x - self.size//2, render_y))
        else:
            # Khối vuông dự phòng nếu mất ảnh (vẫn nhấp nhô sinh động)
            backup_rect = pygame.Rect(self.x - self.size//2, render_y, self.size, self.size)
            pygame.draw.rect(screen, (0, 230, 160), backup_rect, border_radius=8)
            pygame.draw.rect(screen, (20, 20, 20), backup_rect, 2, border_radius=8)