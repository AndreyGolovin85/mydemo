#! /usr/bin/env python3

import random
import pygame
from pygame.sprite import Sprite

class Chef(Sprite):
    """Инициализирует пиццу"""
    def __init__(self, screen_game, ai_setting, pizza):
        super(Chef, self).__init__()
        self.screen_game = screen_game
        self.ai_setting = ai_setting
        blue = (8, 0, 181)
        # Загрузка изображения повара.
        self.image = pygame.image.load('image/chef.bmp')
        self.image.set_colorkey(blue)
        self.rect = self.image.get_rect()
        self.screen_rect = screen_game.get_rect()
        
        # Координаты появления пиццы.
        self.rect.x = (pizza.x)
        self.rect.y = (0)
        
    def blitme(self):
        self.screen_game.blit(self.image, self.rect)
