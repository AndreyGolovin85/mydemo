import sys
import pygame

class ConfirmExit():
    def __init__(self, ai_setting, screen_game):
        self.ai_setting = ai_setting
        self.screen_game = screen_game
        # Параметры текста для вопроса подтверждения выхода.
        text = "Вы хотите выйти из игры?"
        self.help_text = pygame.font.SysFont('Serif', 35)
        self.text_screen = self.help_text.render(text,1, (0, 0, 0))
        self.text_rect = self.text_screen.get_rect()
        self.screen_rect = screen_game.get_rect()
        self.text_rect.x = (140)
        self.text_rect.y = (200)
        
    def blitme_confirm(self):
        self.screen_game.blit(self.text_screen, self.text_rect)
