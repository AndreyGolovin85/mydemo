#! /usr/bin/env python3

import pygame.font

class NumbersPizza():
    """Класс для вывода игровой информации количества пиццы."""
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
        self.prep_numbers()
        
    def prep_numbers(self):
        """Преобразование текущего количества пиццы в графическое изображение."""
        numbers_str = str(self.stats.numbers)
        self.numbers_image = self.font.render(numbers_str, True,
            self.text_color, self.ai_setting.bg_fon)
            
        # Вывод счета в правой вехней части экрана.
        self.numbers_rect = self.numbers_image.get_rect()
        self.numbers_rect.left = self.screen_rect.left + 20
        self.numbers_rect.top = 20
        
    def show_numbers(self):
        """Выводит количество пиццы на экран."""
        self.screen_game.blit(self.numbers_image, self.numbers_rect)
