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
    
def pizzas_rand_cickle(ai_setting, pan, pizzas, pizza, stats, sb, chef, numberspizza):
    if pizza.rect.y < ai_setting.game_height:
        update_pizzas(pizza)
        pass
    else:
        collisions_pizza_pan(ai_setting, pan, pizzas, pizza, stats, sb, numberspizza)
        pizza_chef_random(pizza, chef)
    
def pizza_chef_random(pizza, chef):
    """Рандомное появление пиццы."""
    numbers = [0, 59, 118, 177, 236, 295, 354, 413, 472, 531, 590]
    rand_pizza = random.shuffle(numbers)     
    rand_pizza
    x = random.choice(numbers)
    # Координаты появления пиццы.
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

def check_event_keyup(event, pan, pizza):
    """Реагирует на отпускание клавиш."""
    if event.key == pygame.K_RIGHT:
        pan.moving_right = False
    if event.key == pygame.K_LEFT:
        pan.moving_left = False
    if event.key == pygame.K_SPACE:
        pizza.moving_speed = False

def check_event(pans, pizza):
    """Обрабатывает нажатие клавиш"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_event_keydown(event, pans, pizza)
            
        elif event.type == pygame.KEYUP:
            check_event_keyup(event, pans, pizza)

def pizza_delete(ai_setting, pizza, pizzas, chef, stats, sb, numberspizza):
    """Проверяет достигла ли пицца края экрана и удаляет её"""
    if pizza.rect.bottom >= pizza.screen_rect.bottom:
        pizza.remove(pizzas)

def collisions_pizza_pan(ai_setting, pan, pizzas, pizza, stats, sb, numberspizza):
    collisions = pygame.sprite.spritecollide(pan, pizzas, True)
    if collisions:
        stats.score += ai_setting.points
        sb.prep_score()
        stats.numbers -= 1
        numberspizza.prep_numbers()
    else:
        stats.numbers -= 1
        numberspizza.prep_numbers()
        
def update_screen(screen_game,ai_setting, pizzas,
                  pan, pans, pizza, stats, sb, chef, numberspizza):
    """Обновляет изображение на экране"""
    check_event(pan, pizza)
    chef.blitme()
    pizzas.draw(screen_game)
    pan.blitme()
    pan.update_pan()                                 # Обновление сковороды.
    pizza_delete(ai_setting,pizza, pizzas, chef, stats, sb, numberspizza)     # Удаление пиццы вышедшей за экран.
    pizzas.add(pizza)                                # Добавление пиццы в группу спрайтов.
    sb.show_score()                                  # Вывод очков на экран.
    numberspizza.show_numbers()
    pizzas_rand_cickle(ai_setting, pan, pizzas, pizza, stats, sb, chef, numberspizza)
    
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()
