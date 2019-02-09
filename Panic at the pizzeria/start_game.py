#! /usr/bin/env python3

import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from button import Button
from setting import Settings
from pan import Pan
from pizza import Pizza
from chef import Chef
from game_stats import GameStats
from scoreboard import ScoreBoard
from numbers_pizza import NumbersPizza
import game_functions as gf

# Инициализация экрана и создание игры.
def rungame():
    pygame.init()
    ai_setting = Settings()
    screen_game = pygame.display.set_mode(
                    (ai_setting.game_width, ai_setting.game_height))
    pygame.display.set_caption("Panic at the pizzeria")
    
    # Создание кнопки Play.
    play_button = Button(ai_setting, screen_game, "Play")
    # Создание сковороды.
    pan = Pan(screen_game, ai_setting)
    # Создание пиццы.
    pizza = Pizza(screen_game, ai_setting)
    # Создание группы спрайтов.
    pizzas = Group()
    pans = Group()
    # Объявление переменной stats.
    stats = GameStats(ai_setting)
    # Вывод очков на экран.
    sb = ScoreBoard(ai_setting, screen_game, stats)
    chef = Chef(screen_game, ai_setting, pizza)
    # Вывод колличества пиццы на экран.
    numberspizza = NumbersPizza(ai_setting, screen_game, stats)
    
    """Основной цикл игры."""
    while True:
        # Обновление экрана.
        screen_game.blit(ai_setting.bg_fon, ai_setting.bg_rect)
        gf.update_screen(screen_game,ai_setting, pizzas,
                         pan, pans, pizza, stats, sb, chef,
                         numberspizza, play_button)
        
rungame()
