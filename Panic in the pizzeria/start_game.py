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
from help_game import Help
from confirm_exit import ConfirmExit
import game_functions as gf

# Инициализация экрана и создание игры.
def rungame():
    pygame.init()
    ai_setting = Settings()
    screen_game = pygame.display.set_mode(
                    (ai_setting.game_width, ai_setting.game_height))
    pygame.display.set_caption("Panic in the pizzeria")
    # Создание кнопок Play, Help, Quit, Yes, No.
    play_button = Button(ai_setting, screen_game, "Play")
    help_button = Button(ai_setting, screen_game, "Help")
    quit_button = Button(ai_setting, screen_game, "Exit")
    back_button = Button(ai_setting, screen_game, "Back")
    yes_button = Button(ai_setting, screen_game, "Yes")
    no_button = Button(ai_setting, screen_game, "No")
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
    # Вывод справки.
    help_g = Help(ai_setting, screen_game)
    # Подтверждение выхода из игры.
    confirm_exit = ConfirmExit(ai_setting, screen_game)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    """Основной цикл игры."""
    while True:
        # Обновление экрана.
        screen_game.blit(ai_setting.bg_fon, ai_setting.bg_rect)
        gf.update_screen(screen_game,ai_setting, pizzas,
                         pan, pans, pizza, stats, sb, chef,
                         numberspizza, play_button, help_button,
                         quit_button, help_g, back_button, confirm_exit,
                         mouse_x, mouse_y, yes_button, no_button)
        
rungame()
