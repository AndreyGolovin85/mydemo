import pygame.font

class Button():
    def __init__(self, ai_setting, screen_game, msg):
        self.screen_game = screen_game
        self.screen_rect = screen_game.get_rect()
        
        # Назначение размеров и свойств кнопок.
        self.width, self.height = 80, 40
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Построение объекта rect кнопки и выравнивание её по центру экрана.
        self.rect = pygame.Rect(280, 80, self.width, self.height)
        
        #self.rect_3 = pygame.Rect(280, 280, self.width, self.height)
        #self.rect_4 = pygame.Rect(280, 400, self.width, self.height)
        #self.rect_5 = pygame.Rect(100, 300, self.width, self.height)
        #self.rect_6 = pygame.Rect(460, 300, self.width, self.heigh
        # Преобразование текта в прямоугольник.
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_1 = self.msg_image.get_rect()
        self.msg_image_1.center = self.rect.center
        
        self.msg_image_2 = self.msg_image.get_rect()
        self.msg_image_2.center = self.rect.center
        self.msg_image_2.x = 280
        self.msg_image_2.y = 180
    
    def draw_button(self):
        # Вывод сообщения на экран.
        self.screen_game.blit(self.msg_image, self.msg_image_1)
        
    def draw_button_2(self):
        # Вывод сообщения на экран.
        self.screen_game.blit(self.msg_image, self.msg_image_2)
