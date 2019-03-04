import pygame
import pygame.font

class ScoreBoard():
    """Класс для вывода игровой информации."""
    def __init__(self, ai_setting, screen_game, stats):
        self.ai_setting = ai_setting
        self.screen_rect = screen_game.get_rect()
        self.screen_game = screen_game
        self.stats = stats
        # Настройка шрифта для вывода на экран.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Подготовка исходного изображения.
        self.prep_score()
        self.prep_numbers()
        
    
    def prep_score(self):
        # Преобразование текста в изображение.
        self.text_str_1 = str(self.stats.score)
        self.score_image = self.font.render(self.text_str_1, True, 
                                self.text_color, self.ai_setting.bg_fon)
        # Преобразование текста в прямоугольник.
        self.score_rect = self.score_image.get_rect()
        # Вывод счета в правой вехней части экрана.
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_numbers(self):
        # Преобразование текста в изображение.
        self.text_str_2 = str(self.stats.numbers)
        self.numbers_image = self.font.render(self.text_str_2, True, 
                                self.text_color, self.ai_setting.bg_fon)
        # Преобразование текста в прямоугольник.
        self.numbers_rect = self.numbers_image.get_rect()
        # Вывод счета в левой вехней части экрана.
        self.numbers_rect.left = self.screen_rect.left + 20
        self.numbers_rect.top = 20
        
    def show_numbers(self):
        """Выводит количество пиццы на экран."""
        self.screen_game.blit(self.numbers_image, self.numbers_rect)
        
    def show_score(self):
        """Выводит счет на экран."""
        self.screen_game.blit(self.score_image, self.score_rect)

class ConfirmExit():
    def __init__(self, ai_setting, screen_game):
        self.ai_setting = ai_setting
        self.screen_game = screen_game
        # Параметры текста для вопроса подтверждения выхода.
        text = "Вы хотите выйти из игры?"
        self.help_text = pygame.font.SysFont('Serif', 35)
        self.text_screen = self.help_text.render(text, 1, (255, 255, 255))
        self.text_rect = self.text_screen.get_rect()
        self.text_rect.x = 140
        self.text_rect.y = 200
        
    def blitme_confirm(self):
        self.screen_game.blit(self.text_screen, self.text_rect)

class Help():
    def __init__(self, ai_setting, screen_game):
        self.ai_setting = ai_setting
        self.screen_game = screen_game
        # Параметры текста справки.
        self.help_text = pygame.font.SysFont('Serif', 25)
        self.text_screen = self.help_text.render("Справка по игре", 1, (0, 0, 0))
        self.text_rect = self.text_screen.get_rect()
        self.text_rect.x = 220
        self.text_rect.y = 10
        
    def blitme_help(self):
        self.screen_game.blit(self.text_screen, self.text_rect)

class GameStats():
    def __init__(self, ai_setting):
        self.ai_setting = ai_setting
        self.reset_stats()
        self.pizzas_numbers()
        
        # Игра запускается в неактивном состоянии.
        self.game_active = False
        # Флаг перехода в раздел помощь.
        self.help_active = False
        # Флаг подтверждения выхода из игры.
        self.game_exit = False
        # Флаг ускорения пиццы.
        self.moving_speed = False
        # Флаги перемещения сковороды.
        self.moving_right = False
        self.moving_left = False
        
    def reset_stats(self):
        self.score = 0
        
    def pizzas_numbers(self):
        self.numbers = 5

