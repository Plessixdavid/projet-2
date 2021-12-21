import pygame
from menu.spaceship.spaceship_main import spaceship_start
from menu.PacMan.Main import Pacman_start
from menu.knight_castle.main import knight_start
from menu.puissance4.puissancePygame import puissance4_start
from menu.Snake_Game.main import Snake_start
from menu.TicTacToe.main import Morbac_start



class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 50, 50)
        self.offset = -150

    # afficher et configurer le curseur.
    def draw_cursor(self):
        self.game.draw_text('*', 40, self.cursor_rect.x, self.cursor_rect.y)
    

    # Création de l'ecran d'affichage.
    def blit_screen(self):
        self.game.window.blit(self.game.display,(0,0))
        self.game.display.fill((0, 0, 0))
        pygame.display.update()
        self.game.reset_keys()

# Création du menu et configuration des elements.
class MainMenu(Menu):
    def __init__(self, game, spaceship_start, knight_start, Pacman_start, puissance4_start, Snake_start, Morbac_start):
        Menu.__init__(self, game)
        self.state = "Planet Express"
        self.planet_expressx, self.planet_expressy = self.mid_w, self.mid_h - 200
        self.Knight_Castlex, self.Knight_Castley = self.mid_w, self.mid_h - 100
        self.Pacmanx, self.Pacmany = self.mid_w, self.mid_h +0
        self.Puissance_4x, self.Puissance_4y = self.mid_w, self.mid_h + 100
        self.Snakex, self.Snakey = self.mid_w, self.mid_h +200
        self.Morbacx, self.Morbacy = self.mid_w, self.mid_h + 300
        self.cursor_rect.midtop = (self.planet_expressx + self.offset, self.planet_expressy)

        

    # Affichage des elements du menu
    def display_menu(self):
        
        self.run_display = True
        self.image = pygame.image.load("scripts_python/menu/a415uP.jpeg")
        
        while self.run_display:
            self.game.display.blit(self.image, (0, 0))
            self.game.check_events()
            self.check_input()
            self.game.display.blit(self.image,(0,0))
            self.game.draw_text("Menu Principal", 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 300)
            self.game.draw_text("Planet Express", 50, self.planet_expressx, self.planet_expressy)
            self.game.draw_text("Knight Castle", 50, self.Knight_Castlex, self.Knight_Castley)
            self.game.draw_text("Pacman", 50, self.Pacmanx, self.Pacmany)
            self.game.draw_text("puissance 4 ", 50, self.Puissance_4x, self.Puissance_4y)
            self.game.draw_text("Snake", 50, self.Snakex, self.Snakey)
            self.game.draw_text("Morbac", 50, self.Morbacx, self.Morbacy)
            self.draw_cursor()
            self.blit_screen()
    
    # fonction du mouvement du curseur
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Planet Express":
                self.cursor_rect.midtop = (self.Knight_Castlex + self.offset, self.Knight_Castley)
                self.state = "Knight Castle"
            elif self.state == "Knight Castle":
                self.cursor_rect.midtop = (self.Pacmanx + self.offset, self.Pacmany)
                self.state = "Pacmans"
            elif self.state == "Pacmans":
                self.cursor_rect.midtop = (self.Puissance_4x + self.offset, self.Puissance_4y)
                self.state = "Puissance 4"
            elif self.state == "Puissance 4":
                self.cursor_rect.midtop = (self.Snakex + self.offset, self.Snakey)
                self.state = "Snake"
            elif self.state == "Snake":
                self.cursor_rect.midtop = (self.Morbacx + self.offset, self.Morbacy)
                self.state = "Morbac"
            elif self.state == "Morbac":
                self.cursor_rect.midtop = (self.planet_expressx + self.offset, self.planet_expressy)
                self.state = "Planet Express"
        # elif self.game.UP_KEY:
        #     if self.state == "Knight Castle":
        #         self.cursor_rect.midtop = (self.planet_expressx + self.offset, self.planet_expressy)
        #         self.state = "Planet Express"
        #     elif self.state == "Pacmans":
        #         self.cursor_rect.midtop = (self.Knight_Castlex + self.offset, self.Knight_Castley)
        #         self.state = "Knight Castle"
        #     elif self.state == "Puissance 4":
        #         self.cursor_rect.midtop = (self.Pacmanx + self.offset, self.Pacmany)
        #         self.state = "Pacmans"
        #     elif self.state == "Snake":
        #         self.cursor_rect.midtop = (self.planet_expressx + self.offset, self.planet_expressy)
        #         self.state = "Morbac"
        #      elif self.state == "Morbac":
        #          self.cursor_rect.midtop = (self.Pacmanx + self.offset, self.Pacmany)
        #          self.state = "Morbac"
        #      elif self.state == "Morbac":
        #          self.cursor_rect.midtop = (self.Pacmanx + self.offset, self.Pacmany)
        #          self.state = "Planet Express"

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Planet Express":
                spaceship_start()
            elif self.state == "Knight Castle":
                knight_start()
            elif self.state == "Pacmans":
                Pacman_start()
            elif self.state == "Puissance 4":
                puissance4_start()
            elif self.state == "Snake":
                Snake_start()
            elif self.state == "Morbac":
                Morbac_start()
            # self.run_display = False




        

        
        
        