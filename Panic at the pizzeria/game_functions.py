#! /usr/bin/env python3

import sys
import pygame
from pygame.sprite import Group
from pan import Pan
from pizza import Pizza
from setting import Settings
import random

def update_pizzas(pizza):
    """Обновляет позицию пиццы."""
    pizza.update_pizza()
    
def pizzas_rand_cickle(screen_game, ai_setting, pan, pizzas,
                       pizza, stats, sb, chef, numberspizza, play_button):
    """Обновляет позицию пиццы, проверяет коллизию, рандомно выдает пиццу."""
    if pizza.rect.y < ai_setting.game_height:
        collisions = pygame.sprite.spritecollide(pan, pizzas, True)
        update_pizzas(pizza)
        pass
    else:
        collisions_pizza_pan(screen_game, ai_setting, pan,
                             pizzas, pizza, stats, sb, numberspizza, play_button)
        pizza_chef_random(pizza, chef)
    
def pizza_chef_random(pizza, chef):
    """Рандомное появление пиццы."""
    numbers = [0, 59, 118, 177, 236, 295, 354, 413, 472, 531, 590]
    rand_pizza = random.shuffle(numbers)     
    rand_pizza
    x = random.choice(numbers)
    # Координаты появления пиццы и повара.
    chef.rect.x = (x)
    chef.rect.y = (0)
    pizza.rect.x = (x)
    pizza.rect.y = (70)

def check_event_keydown(event, pan, pizza):
    """Реагирует на нажатие клавиш."""
    if event.key == pygame.K_RIGHT:
        pan.moving_right = True
    if event.key == pygame.K_LEFT:
        pan.moving_left = True
    if event.key == pygame.K_SPACE:
        pizza.moving_speed = True
    if event.key == pygame.K_q:
        sys.exit()

def check_event_keyup(event, pan, pizza):
    """Реагирует на отпускание клавиш."""
    if event.key == pygame.K_RIGHT:
        pan.moving_right = False
    if event.key == pygame.K_LEFT:
        pan.moving_left = False
    if event.key == pygame.K_SPACE:
        pizza.moving_speed = False

def check_event(pans, pizza, play_button, stats):
    """Обрабатывает нажатие клавиш"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_event_keydown(event, pans, pizza)
            
        elif event.type == pygame.KEYUP:
            check_event_keyup(event, pans, pizza)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)

def check_play_button(stats, play_button, mouse_x, mouse_y):
    """Запускает новую игру при нажатии кнопки Play."""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True

def pizza_delete(ai_setting, pizza, pizzas, chef, stats, sb, numberspizza):
    """Проверяет достигла ли пицца края экрана и удаляет её"""
    if pizza.rect.bottom >= pizza.screen_rect.bottom:
        pizza.remove(pizzas)

def collisions_pizza_pan(screen_game, ai_setting, pan,
                         pizzas, pizza, stats, sb, numberspizza, play_button):
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
    else:
        stats.game_active = False
        
def update_screen(screen_game, ai_setting, pizzas,
                  pan, pans, pizza, stats, sb, chef,
                  numberspizza, play_button):
    """Обновляет изображение на экране"""
    check_event(pan, pizza, play_button, stats)
    chef.blitme()
    pizzas.draw(screen_game)
    pan.blitme()
    pan.update_pan()                                 # Обновление сковороды.
    pizza_delete(ai_setting,pizza, pizzas,
                 chef, stats, sb, numberspizza)      # Удаление пиццы вышедшей за экран.
    pizzas.add(pizza)                                # Добавление пиццы в группу спрайтов.
    sb.show_score()                                  # Вывод очков на экран.
    numberspizza.show_numbers()
    pizzas_rand_cickle(screen_game, ai_setting, pan, pizzas, pizza, stats, sb,
                       chef, numberspizza, play_button)
    # Кнопка Play отображается если игра не активна.
    if not stats.game_active:
        play_button.draw_button()
        
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()
