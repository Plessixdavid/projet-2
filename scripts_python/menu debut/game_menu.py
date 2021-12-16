import pygame

from menu import *

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

        # InfoObject permet de recuperer les info du display x et y
        infoObject = pygame.display.Info()

        #display.set_mode permet d'utiliser les infos de infoObject et de les utiliser avec le current_w et current_x
        self.DISPLAY_W, self.DISPLAY_H =  infoObject.current_w, infoObject.current_h
        self.window = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        # self.font_name = pygame.font.get_default_font()
        
        self.BLACK,self.WHITE = (0,0,0), (255,255,255)
        self.main_menu = Commencer(self)
        self.connexion = Connexion(self)
        self.inscription = Inscription(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
                
            
            # self.display.fill(self.BLACK)
            # self.draw_text("Merci d avoir joué", 50, self.DISPLAY_W/2, self.DISPLAY_H/2)
            # self.window.blit(self.display,(0,0))
            # pygame.display.update()
            # self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.START_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = False
                    self.running, self.playing = False, False
                    self.curr_menu.run_display = False
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

            

    def reset_keys(self):
        self.UP_Key, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font("scripts_python/menu/knight_castle/FreckleFace-Regular.ttf", size)
        text_surface = font.render(text,True,self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    