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

pygame.font.init()
# Ép load font hệ thống hỗ trợ tiếng Việt có dấu
FONT_LARGE = pygame.font.SysFont("Segoe UI", 22, bold=True)
FONT_STATUS = pygame.font.SysFont("Segoe UI", 16, bold=True)
FONT_MED = pygame.font.SysFont("Segoe UI", 14, bold=True)
FONT_SMALL = pygame.font.SysFont("Segoe UI", 12, bold=True)
FONT_MINI = pygame.font.SysFont("Segoe UI", 12, bold=True)