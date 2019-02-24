import pygame.font

class Button():
    def __init__(self, ai_setting, screen_game, msg):
        """Инициализирует атрибуты кнопки."""
        self.screen_game = screen_game
        self.ai_setting = ai_setting
        self.screen_rect = screen_game.get_rect()
        
        # Назначение размеров и свойств кнопок.
        self.width, self.height = 90, 50
        self.button_color = (0, 191, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Построение объекта rect кнопки и выравнивание её по центру экрана.
        self.rect_1 = pygame.Rect(280, 80, self.width, self.height)
        self.rect_2 = pygame.Rect(280, 180, self.width, self.height)
        self.rect_3 = pygame.Rect(280, 280, self.width, self.height)
        self.rect_4 = pygame.Rect(280, 400, self.width, self.height)
        # Сообщение кнопки создается только один раз.
        self.prep_msg_1(msg)
        self.prep_msg_2(msg)
        self.prep_msg_3(msg)
        self.prep_msg_4(msg)
        
    def prep_msg_1(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        self.msg_image_1 = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect_1 = self.msg_image_1.get_rect()
        self.msg_image_rect_1.center = self.rect_1.center
        
    def prep_msg_2(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        self.msg_image_2 = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect_2 = self.msg_image_2.get_rect()
        self.msg_image_rect_2.center = self.rect_2.center
    
    def prep_msg_3(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        self.msg_image_3 = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect_3 = self.msg_image_3.get_rect()
        self.msg_image_rect_3.center = self.rect_3.center
    
    def prep_msg_4(self, msg):
        self.msg_image_4 = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect_4 = self.msg_image_4.get_rect()
        self.msg_image_rect_4.center = self.rect_4.center
        
    def prep_msg_5(self, msg):
        self.msg_image_5 = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect_5 = self.msg_image_5.get_rect()
        self.msg_image_rect_5.center = self.rect_5.center
    
    def prep_msg_6(self, msg):
        self.msg_image_6 = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect_6 = self.msg_image_6.get_rect()
        self.msg_image_rect_6.center = self.rect_6.center
        
    def draw_button_1(self):
        # Отображение пустой кнопки и вывод сообщения.
        self.screen_game.fill(self.button_color, self.rect_1)
        self.screen_game.blit(self.msg_image_1, self.msg_image_rect_1)
        
    def draw_button_2(self):
        self.screen_game.fill(self.button_color, self.rect_2)
        self.screen_game.blit(self.msg_image_2, self.msg_image_rect_2)
        
    def draw_button_3(self):
        self.screen_game.fill(self.button_color, self.rect_3)
        self.screen_game.blit(self.msg_image_3, self.msg_image_rect_3)
        
    def draw_button_4(self):
        self.screen_game.fill(self.button_color, self.rect_4)
        self.screen_game.blit(self.msg_image_4, self.msg_image_rect_4)
        
    def draw_button_5(self):
        self.screen_game.fill(self.button_color, self.rect_5)
        self.screen_game.blit(self.msg_image_5, self.msg_image_rect_5)
    
    def draw_button_6(self):
        self.screen_game.fill(self.button_color, self.rect_6)
        self.screen_game.blit(self.msg_image_6, self.msg_image_rect_6)
