import sys
import random
import pygame
from pygame.sprite import Group
from tkinter import messagebox as mb
from tkinter import Tk
from pan import Pan
from pizza import Pizza
from setting import Settings
from button import Button
from help_game import Help
from setting import Settings

def check_quit(stats, confirm_exit, mouse_x, mouse_y, yes_button,
               no_button):
    if yes_button.rect_5.collidepoint(mouse_x, mouse_y):
        sys.exit()
    if no_button.rect_6.collidepoint(mouse_x, mouse_y):
        stats.game_exit = False

def update_pizzas(pizza):
    """Обновляет позицию пиццы."""
    pizza.update_pizza()
    
def pizzas_rand_cickle(screen_game, ai_setting, pan, pizzas,
                       pizza, stats, sb, chef, numberspizza, play_button):
    """Обновляет позицию пиццы, проверяет коллизию, рандомно выдает пиццу."""
    if pizza.rect.y < ai_setting.game_height:
        collisions = pygame.sprite.spritecollide(pan, pizzas, True)
        update_pizzas(pizza)
    else:
        collisions_pizza_pan(screen_game, ai_setting, pan,
                             pizzas, pizza, stats, sb, play_button, numberspizza)
        pizza_chef_random(pizza, chef)
    
def pizza_chef_random(pizza, chef):
    """Рандомное появление пиццы и повара."""
    numbers = [0, 59, 118, 177, 236, 295, 354, 413, 472, 531, 590]
    rand_pizza = random.shuffle(numbers)     
    rand_pizza
    x = random.choice(numbers)
    # Координаты появления пиццы и повара.
    chef.rect.x = (x)
    chef.rect.y = (0)
    pizza.rect.x = (x)
    pizza.rect.y = (70)

def check_event_keydown(event, pan, pizza, stats, confirm_exit, mouse_x,
                        mouse_y, yes_button, no_button):
    """Реагирует на нажатие клавиш."""
    if event.key == pygame.K_RIGHT:
        pan.moving_right = True
    if event.key == pygame.K_LEFT:
        pan.moving_left = True
    if event.key == pygame.K_SPACE:
        pizza.moving_speed = True
    if event.key == pygame.K_q:
        stats.game_exit = True

def check_event_keyup(event, pan, pizza):
    """Реагирует на отпускание клавиш."""
    if event.key == pygame.K_RIGHT:
        pan.moving_right = False
    if event.key == pygame.K_LEFT:
        pan.moving_left = False
    if event.key == pygame.K_SPACE:
        pizza.moving_speed = False

def check_event(pan, pans, pizza, play_button, help_button, back_button,
                quit_button, stats, screen_game, ai_setting, help_g,
                confirm_exit, mouse_x, mouse_y, yes_button, no_button):
    """Обрабатывает нажатие клавиш"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stats.game_exit = True
            
        elif event.type == pygame.KEYDOWN:
            check_event_keydown(event, pan, pizza, stats, confirm_exit,
                                mouse_x, mouse_y, yes_button, no_button)
            
        elif event.type == pygame.KEYUP:
            check_event_keyup(event, pan, pizza)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_help_back_quit_button(stats, play_button, help_button,
                                     back_button, quit_button, mouse_x,
                                     mouse_y, screen_game, ai_setting,
                                     confirm_exit, yes_button, no_button)
            check_quit(stats, confirm_exit, mouse_x, mouse_y, yes_button,
                       no_button)

def check_play_help_back_quit_button(stats, play_button, help_button,
                                     back_button, quit_button, mouse_x,
                                     mouse_y, screen_game, ai_setting,
                                     confirm_exit, yes_button,
                                     no_button):
    """Запускает новую игру при нажатии кнопки Play."""
    if play_button.rect_1.collidepoint(mouse_x, mouse_y):
        stats.game_active = True
    """Запускает справку при нажатии кнопки Help."""
    if help_button.rect_2.collidepoint(mouse_x, mouse_y):
        stats.help_active = True
    """Кнопка Back возвщает в главное меню."""
    if back_button.rect_4.collidepoint(mouse_x, mouse_y):
        stats.help_active = False
    """Вопрос потверждения по нажатии кнопки Quit."""
    if quit_button.rect_3.collidepoint(mouse_x, mouse_y):
        stats.game_exit = True

def pizza_delete(ai_setting, pizza, pizzas, chef, stats, sb, numberspizza):
    """Проверяет достигла ли пицца края экрана и удаляет её"""
    if pizza.rect.bottom >= pizza.screen_rect.bottom:
        pizza.remove(pizzas)

def collisions_pizza_pan(screen_game, ai_setting, pan,
                         pizzas, pizza, stats, sb, play_button, numberspizza):
    collisions = pygame.sprite.spritecollide(pan, pizzas, True)
    if collisions:
        stats.score += ai_setting.points
        sb.prep_score()
    stoppage_play(screen_game, ai_setting, stats, play_button, numberspizza)

def stoppage_play(screen_game, ai_setting, stats, play_button, numberspizza):
    """Проверяет оставшееся количество пиццы."""
    if stats.numbers > 0:
        stats.numbers -= 1
        numberspizza.prep_numbers()
    if stats.numbers == 0:
        stats.game_active = False
        
def update_screen(screen_game, ai_setting, pizzas,
                  pan, pans, pizza, stats, sb, chef,
                  numberspizza, play_button, help_button,
                  quit_button, help_g, back_button, confirm_exit, mouse_x,
                  mouse_y, yes_button, no_button):
    """Обновляет изображение на экране"""
    # Проверяет события клавиатуры и мыши.
    check_event(pan, pans, pizza, play_button, help_button, back_button, quit_button, stats,
                screen_game, ai_setting, help_g, confirm_exit, mouse_x, mouse_y,
                yes_button, no_button)
    if stats.game_active:
        """Активирует игру и запускает обновление экрана."""
        chef.blitme()
        pizzas.draw(screen_game)
        pan.blitme()
        pan.update_pan()                                 # Обновление сковороды.
        pizza_delete(ai_setting,pizza, pizzas,
                     chef, stats, sb, numberspizza)      # Удаление пиццы вышедшей за экран.
        pizzas.add(pizza)                                # Добавление пиццы в группу спрайтов.
        sb.show_score()                                  # Вывод очков на экран.
        numberspizza.show_numbers()                      # Вывод количества пиццы на экран.
        pizzas_rand_cickle(screen_game, ai_setting, pan,
                           pizzas, pizza, stats, sb,chef, numberspizza,
                           play_button)
    # Кнопки Play, Help, Quit отображаются если игра не активна.
    if not stats.game_active:
        if not stats.help_active:
            if not stats.game_exit:
                play_button.draw_button_1()
                help_button.draw_button_2()
                quit_button.draw_button_3()
            if stats.game_exit:
                confirm_exit.blitme_confirm()
                yes_button.draw_button_5()
                no_button.draw_button_6()
        if stats.help_active:
            help_g.blitme_help()
            # Отображение кнопки Back при открытии Help.
            back_button.draw_button_4()
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()
