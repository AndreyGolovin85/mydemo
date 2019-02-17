import pygame
from pygame.sprite import Sprite

class Pan(Sprite):
    """Инициализирует сковороду и задаёт её начальную позицию"""
    def __init__(self, screen_game, ai_setting):
        super(Pan, self).__init__()
        self.ai_setting = ai_setting        
        self.screen_game = screen_game
        white = (255, 255, 255)
        # Загрузка изображения сковороды.
        self.image = pygame.image.load('image/pan1.bmp')
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.screen_rect = screen_game.get_rect()
        # Координаты сковороды.
        self.rect.x = (300)
        self.rect.y = (433)
        # Флаги перемещения сковороды.
        self.moving_right = False
        self.moving_left = False
        
    def update_pan(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.ai_setting.speed_pan
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_setting.speed_pan

    def blitme(self):
        self.screen_game.blit(self.image, self.rect)
