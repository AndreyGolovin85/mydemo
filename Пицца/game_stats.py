#! /usr/bin/env python3

class GameStats():
    def __init__(self, ai_setting):
        self.ai_setting = ai_setting
        self.reset_stats()
        self.pizzas_numbers()
        
    def reset_stats(self):
        self.score = 0
        
    def pizzas_numbers(self):
        self.numbers = 20
