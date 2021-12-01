import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 50, 50)
        self.offset = -100

    # afficher et configurer le curseur.
    def draw_cursor(self):
        self.game.draw_text('*', 40, self.cursor_rect.x, self.cursor_rect.y)
    

    # Création de l'ecran d'affichage.
    def blit_screen(self):
        self.game.window.blit(self.game.display,(0,0))
        pygame.display.update()
        self.game.reset_keys()

# Création du menu et configuration des elements.
class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Commencer"
        self.startx, self.starty = self.mid_w, self.mid_h + 20
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 60
        self.creditx, self.credity = self.mid_w, self.mid_h + 80
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
    
    # Affichage des elements du menu
    def display_menu(self):
        self.run_display = True
        self.image = pygame.image.load("menu/123.jpg")
        while self.run_display:
            self.game.display.blit(self.image, (0, 50))
            self.game.check_events()
            self.check_input()
            self.game.display.blit(self.image,(0,0))
            self.game.draw_text("Menu Principal", 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100)
            self.game.draw_text("Commencer", 50, self.startx, self.starty-20)
            self.game.draw_text("Options", 50, self.optionsx, self.optionsy-20)
            self.game.draw_text("Credits", 50,self.creditx, self.credity)
            self.draw_cursor()
            self.blit_screen()
    
    # fonction du mouvement du curseur
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Commencer":
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = "Options"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.creditx + self.offset, self.credity)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Commencer"
        elif self.game.UP_KEY:
            if self.state == "Commencer":
                self.cursor_rect.midtop = (self.creditx + self.offset, self.credity)
                self.state = "Credits"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Commencer"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = "Options"

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Commencer":
                self.game.playing = True
            elif self.state == "Options":
                pass
            elif self.state == "Credits":
                pass
            self.run_display = False

        
        
        