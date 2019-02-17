#! /usr/bin/env python3
import pygame.font

class ScoreBoard():
    """Класс для вывода игровой информации."""
    def __init__(self, ai_setting, screen_game, stats):
        """Инициализирует атрибуты подсчета игры."""
        self.ai_setting = ai_setting
        self.screen_rect = screen_game.get_rect()
        self.screen_game = screen_game
        self.stats = stats
        
        # Настройка шрифта для вывода на экран.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Подготовка исходного изображения.
        self.prep_score()
        
    def prep_score(self):
        """Преобразование текущего счета в графическое изображение."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
            self.text_color, self.ai_setting.bg_fon)
            
        # Вывод счета в правой вехней части экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        """Выводит счет на экран."""
        self.screen_game.blit(self.score_image, self.score_rect)
