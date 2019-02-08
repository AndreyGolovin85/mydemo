#! /usr/bin/env python3

import pygame
from pygame.sprite import Sprite
import random

class Pizza(Sprite):
    """Инициализирует пиццу"""
    def __init__(self, screen_game, ai_setting):
        super(Pizza, self).__init__()
        self.screen_game = screen_game
        self.ai_setting = ai_setting
        self.numbers = [0, 59, 118, 177, 236, 295, 354, 413, 472, 531, 590]
        self.rand_pizza = random.shuffle(self.numbers)     
        white = (255, 255, 255)
        # Загрузка изображения пиццы.
        self.image = pygame.image.load('image/pizza.bmp')
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.screen_rect = screen_game.get_rect()
        self.rand_pizza
        self.x = random.choice(self.numbers)
        # Координаты появления пиццы.
        self.rect.x = (self.x)
        self.rect.y = (70)
        # Флаг ускорения пиццы.
        self.moving_speed = False
        
    def update_pizza(self):
        if self.moving_speed:
            self.rect.y += self.ai_setting.pizza_drop_speed * 3
        else:
            self.rect.y += self.ai_setting.pizza_drop_speed

    def blitme(self):
        self.screen_game.blit(self.image, self.rect)
