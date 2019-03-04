import pygame
from pygame.sprite import Sprite

class Pizza(Sprite):
    def __init__(self, screen_game, ai_setting):
        super(Pizza, self).__init__()
        self.screen_game = screen_game
        self.ai_setting = ai_setting
        white = (255, 255, 255)
        # Загрузка изображения пиццы.
        self.image = pygame.image.load('image/pizza.bmp')
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        # Координаты появления пиццы.
        self.rect.y = 70

    def blitme(self):
        self.screen_game.blit(self.image, self.rect)
        
class Pan(Sprite):
    def __init__(self, screen_game, ai_setting):
        super(Pan, self).__init__()
        self.ai_setting = ai_setting        
        self.screen_game = screen_game
        white = (255, 255, 255)
        # Загрузка изображения сковороды.
        self.image = pygame.image.load('image/pan1.bmp')
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        # Координаты сковороды.
        self.rect.x = (300)
        self.rect.y = (433)

    def blitme(self):
        self.screen_game.blit(self.image, self.rect)

class Chef(Sprite):
    def __init__(self, screen_game, ai_setting, pizza):
        super(Chef, self).__init__()
        self.screen_game = screen_game
        self.ai_setting = ai_setting
        blue = (8, 0, 181)
        # Загрузка изображения повара.
        self.image = pygame.image.load('image/chef.bmp')
        self.image.set_colorkey(blue)
        self.rect = self.image.get_rect()
        # Координаты появления повара.
        self.rect.y = (0)
        
    def blitme(self):
        self.screen_game.blit(self.image, self.rect)

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
