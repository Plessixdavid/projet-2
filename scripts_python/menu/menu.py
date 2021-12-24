import pygame
from menu.spaceship.spaceship_main import spaceship_start
from menu.PacMan.Main import Pacman_start
from menu.knight_castle.main import knight_start
from menu.puissance4.puissancePygame import puissance4_start
from menu.Snake_Game.main import Snake_start
from menu.TicTacToe.main import Morbac_start
from BDD.DBUtil import DBUtil

import var



class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 50, 50)
        self.offset = -250

    # afficher et configurer le curseur.
    def draw_cursor(self):
        self.game.draw_text('*', 40, self.cursor_rect.x, self.cursor_rect.y)
    

    # Création de l'écran d'affichage.
    def blit_screen(self):
        self.game.window.blit(self.game.display,(0,0))
        self.game.display.fill((0, 0, 0))
        pygame.display.update()
        self.game.reset_keys()

# Création du menu et configuration des éléments.
class MainMenu(Menu):
    def __init__(self, game, spaceship_start, knight_start, Pacman_start, puissance4_start, Snake_start, Morbac_start):
        Menu.__init__(self, game)
        self.state = "Planet Express"
        self.planet_expressx, self.planet_expressy = self.mid_w, self.mid_h - 225
        self.Knight_Castlex, self.Knight_Castley = self.mid_w, self.mid_h - 150
        self.Pacmanx, self.Pacmany = self.mid_w, self.mid_h -75
        self.Puissance_4x, self.Puissance_4y = self.mid_w, self.mid_h 
        self.Snakex, self.Snakey = self.mid_w, self.mid_h +75
        self.Morbacx, self.Morbacy = self.mid_w, self.mid_h + 150
        self.Scorex, self.Scorey = self.mid_w, self.mid_h + 225
        self.cursor_rect.midtop = (self.planet_expressx + self.offset, self.planet_expressy)

        

    # Affichage des éléments du menu
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
            self.game.draw_text("Tableau des scores", 50, self.Scorex, self.Scorey)
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
                self.cursor_rect.midtop = (self.Scorex + self.offset, self.Scorey)
                self.state = "Tableau des scores"
            elif self.state == "Tableau des scores":
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
            elif self.state == "tableau des scores":
                Score_Table.display_menu_score()
            self.run_display = False


class Score_Table(Menu):

    def __init__(self, game):
        Menu.__init__(self,game)
        self.state = "Tableau des scores"
        self.planet_expressx, self.planet_expressy = self.mid_w - 200, self.mid_h - 100
        self.Knight_Castlex, self.Knight_Castley = self.mid_w - 200, self.mid_h 
        self.Pacmanx, self.Pacmany = self.mid_w - 200, self.mid_h + 100
        self.Morbacx, self.Morbacy = self.mid_w -200, self.mid_h + 200

    def display_menu_score(self):

        self.run_display = True
        self.image = pygame.image.load("scripts_python/menu/a415uP.jpeg")
        while self.run_display:
            
            self.game.check_events()

            self.game.display.blit(self.image, (0, 0))
            var.spaceship_score = DBUtil.ExecuteQuery(f"SELECT score FROM spaceship INNER JOIN data_joueur ON data_joueur.id = spaceship.id WHERE data_joueur.name = '{var.Pseudo}'")
            var.knight_castle_score = DBUtil.ExecuteQuery(f"SELECT score FROM knight_castle INNER JOIN data_joueur ON data_joueur.id = knight_castle.id WHERE data_joueur.name = '{var.Pseudo}'")
            var.snake_score = DBUtil.ExecuteQuery(f"SELECT score FROM snake_game INNER JOIN data_joueur ON data_joueur.id = snake_game.id WHERE data_joueur.name = '{var.Pseudo}'")
            var.pac_man_score = DBUtil.ExecuteQuery(f"SELECT score FROM pac_man INNER JOIN data_joueur ON data_joueur.id = pac_man.id WHERE data_joueur.name = '{var.Pseudo}'")
            self.game.draw_text('Tableau des Scores : ', 80,self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 300)
            self.game.draw_text(f"Planet Express : {var.spaceship_score[0][0]}", 60, self.planet_expressx, self.planet_expressy )
            self.game.draw_text(f"Knight Castel : {var.knight_castle_score[0][0]}", 60, self.Knight_Castlex, self.Knight_Castley)
            self.game.draw_text(f"Pac-Man : {var.pac_man_score[0][0]}", 60, self.Pacmanx, self.Pacmany)
            self.game.draw_text(f"Snake : {var.snake_score[0][0]}", 60, self.Morbacx, self.Morbacy)
            
            self.blit_screen()


    




        

        
        
        