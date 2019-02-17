import pygame

class Settings():
    # Настроки игры.
    def __init__(self):
        # Разрешение экрана
        self.game_width = 640
        self.game_height = 480
        self.bg_fon = pygame.image.load("image/wall.jpg")
        self.bg_rect = self.bg_fon.get_rect(bottomright = (640, 480))
        # Размер кнопок.
        self.width = 80
        self.height = 30
        # Скорость перемещения сковороды.
        self.speed_pan = 5
        # Скорость снижения пиццы
        self.pizza_drop_speed = 1
        # Подсчет очков.
        self.points = 10
