import pygame
from menu.spaceship.game import Game1 
from menu.knight_castle.main import knight_start
from menu.PacMan.app_class import App
from menu.puissance4.puissancePygame import puissance4_start
from menu.Snake_Game.game import Game4
from menu.TicTacToe.game import Game5
from menu.menu import *


class Game_Menu():
    def __init__(self):
        pygame.init()
        self.running = True
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

        # InfoObject permet de récupérer les info du display x et y
        infoObject = pygame.display.Info()

        #display.set_mode permet d'utiliser les infos de infoObject et de les utiliser avec le current_w et current_x
        self.DISPLAY_W, self.DISPLAY_H =  infoObject.current_w, infoObject.current_h
        self.window = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        
       
        
        self.BLACK,self.WHITE = (0,0,0), (255,255,255)
        self.main_menu = MainMenu(self, Game1, knight_start, App, puissance4_start, Game4, Game5)
        self.score_menu = Score_Table(self)
        self.curr_menu = self.main_menu


    # def check_events(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             self.running= False
    #             self.curr_menu.run_display = False   
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_SPACE:
    #                 self.START_KEY = True
    #             if event.key == pygame.K_ESCAPE:
    #                 self.BACK_KEY = False
    #                 self.running= False
    #                 print(self.curr_menu.run_display_menu)
    #                 return
    #             if event.key == pygame.K_DOWN:
    #                 self.DOWN_KEY = True
    #             if event.key == pygame.K_UP:
    #                 self.UP_KEY = True
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.START_KEY = True
                elif event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True
                    self.running =  False
                elif event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                elif event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_Key, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        pygame.init()
        toto = pygame.font.Font("scripts_python/menu/FreckleFace-Regular.ttf", size)
        text_surface = toto.render(text,True,self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    