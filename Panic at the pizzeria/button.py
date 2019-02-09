import pygame.font

class Button():
    def __init__(self, ai_setting, screen_game, msg):
        """Инициализирует атрибуты кнопки."""
        self.screen_game = screen_game
        self.ai_setting = ai_setting
        self.screen_rect = screen_game.get_rect()
        
        # Назначение размеров и свойств кнопок.
        self.width, self.height = 200, 50
        self.button_color = (0, 191, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Построение объекта rect кнопки и выравнивание её по центру экрана.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # Сообщение кнопки создается только один раз.
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        # Отображение пустой кнопки и вывод сообщения.
        self.screen_game.fill(self.button_color, self.rect)
        self.screen_game.blit(self.msg_image, self.msg_image_rect)
