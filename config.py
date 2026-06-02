import pygame
import os

WIDTH, HEIGHT = 1050, 680
FPS = 60

# Bảng màu Hệ thống Retro Premium Extended
COLOR_BG = (24, 24, 28)
COLOR_ROAD = (38, 38, 44)
COLOR_TEXT_LIGHT = (245, 245, 245)
COLOR_TEXT_DARK = (20, 20, 20)
COLOR_GOLD = (255, 191, 0)
COLOR_MINT = (0, 230, 160)
COLOR_PINK = (255, 64, 129)
COLOR_CARD_INFRA = (240, 244, 248)
COLOR_CARD_POLICY = (255, 243, 230)
COLOR_SHADOW = (10, 10, 12)
COLOR_RED = (235, 60, 60)
COLOR_BLUE = (0, 150, 255)
COLOR_GOLD_SOFT = (245, 210, 120)  # Vàng hoàng gia pastel nhạt
COLOR_MINT_SOFT = (140, 230, 185)  # Xanh bạc hà pastel dịu mắt

# Màu sắc chủ đề 5 Chương (Học thuyết Hình thái KT-XH)
COLOR_CH1 = (139, 90, 43)      # Nâu đất - Công xã nguyên thủy
COLOR_CH2 = (112, 128, 144)    # Xám xích sắt - Chiếm hữu nô lệ
COLOR_CH3 = (184, 134, 11)     # Vàng đất cát - Phong kiến
COLOR_CH4 = (204, 30, 30)      # Đỏ hồng - Xã hội chủ nghĩa
COLOR_CH5 = (0, 180, 220)      # Xanh neon tươi sáng - Thế giới ngày mai (Solarpunk)


pygame.font.init()
# Font hỗ trợ tiếng Việt có dấu - dùng Tahoma hoặc font mặc định
try:
    FONT_LARGE = pygame.font.SysFont("Tahoma", 22, bold=True)
    FONT_STATUS = pygame.font.SysFont("Tahoma", 16, bold=True)
    FONT_MED = pygame.font.SysFont("Tahoma", 14, bold=True)
    FONT_SMALL = pygame.font.SysFont("Tahoma", 12, bold=True)
    FONT_MINI = pygame.font.SysFont("Tahoma", 11, bold=False)
except:
    FONT_LARGE = pygame.font.Font(None, 22)
    FONT_STATUS = pygame.font.Font(None, 16)
    FONT_MED = pygame.font.Font(None, 14)
    FONT_SMALL = pygame.font.Font(None, 12)
    FONT_MINI = pygame.font.Font(None, 11)