import sys
import pygame

class Help():
    def __init__(self, ai_setting, screen_game):
        self.ai_setting = ai_setting
        self.screen_game = screen_game
        # Параметры текста справки.
        self.help_text = pygame.font.SysFont('Serif', 25)
        self.text_screen = self.help_text.render("Справка по игре", 1, (0, 0, 0))
        self.text_rect = self.text_screen.get_rect()
        self.screen_rect = screen_game.get_rect()
        self.text_rect.x = (220)
        self.text_rect.y = (10)
        
    def blitme_help(self):
        self.screen_game.blit(self.text_screen, self.text_rect)
