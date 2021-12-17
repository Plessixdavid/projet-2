import pygame
# from pygame import display
# from pygame import surface
from test_request import input_box



class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 50, 50)
        self.offset = -150
        self.chat_player = input_box()


    # afficher et configurer le curseur.
    def draw_cursor(self):
        self.game.draw_text('*', 40, self.cursor_rect.x, self.cursor_rect.y)
    

    # Création de l'ecran d'affichage.
    def blit_screen(self):
        self.game.window.blit(self.game.display,(0,0))
        pygame.display.update()
        self.game.reset_keys()


# Création du menu et configuration des elements.
class Commencer(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        
        self.state = "Connexion"
        self.connexionx, self.connexiony = self.mid_w, self.mid_h -100
        self.inscriptionx, self.inscriptiony = self.mid_w, self.mid_h 
        self.creditx, self.credity = self.mid_w, self.mid_h + 100
        self.cursor_rect.midtop = (self.connexionx + self.offset, self.connexiony)
        

        

    # Affichage des elements du menu
    def display_menu(self):
        
        self.run_display = True
        
        while self.run_display:
            self.game.check_events(self.chat_player)
            self.check_input()
            self.game.draw_text("Connexion", 50, self.connexionx, self.connexiony)
            self.game.draw_text("Inscription", 50, self.inscriptionx, self.inscriptiony)
            self.game.draw_text("Credits", 50,self.creditx, self.credity)
            self.draw_cursor()
            self.blit_screen()
    
    # fonction du mouvement du curseur
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Connexion":
                self.cursor_rect.midtop = (self.inscriptionx + self.offset, self.inscriptiony)
                self.state = "Inscription"
            elif self.state == "Inscription":
                self.cursor_rect.midtop = (self.creditx + self.offset, self.credity)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.connexionx + self.offset, self.connexiony)
                self.state = "Connexion"
        elif self.game.UP_KEY:
            if self.state == "Connexion":
                self.cursor_rect.midtop = (self.creditx + self.offset, self.credity)
                self.state = "Credits"
            elif self.state == "Inscription":
                self.cursor_rect.midtop = (self.connexionx + self.offset, self.connexiony)
                self.state = "Connexion"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.inscriptionx + self.offset, self.inscriptiony)
                self.state = "Inscription"

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Connexion":
                self.game.curr_menu = self.game.connexion
            elif self.state == "Inscription":
                self.game.curr_menu = self.game.inscription
            elif self.state == "Credits":
                self.game.curr_menu = self.game.credits
            self.run_display = False


class Connexion(Menu):
    def __init__(self, game):
        Menu.__init__(self,game)
        self.state = 'Connexion'
        self.pseudox, self.pseudoy = self.mid_w, self.mid_h + 20
        self.mdpx, self.mdpy = self.mid_w, self.mid_h + 40
        self.mailx, self.maily = self.mid_w, self.mid_h + 40
        self.validex, self.validey = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.pseudox + self.offset, self.pseudoy)
        self.chat_player = input_box()


    def display_menu(self):

        self.run_display = True
        while self.run_display:
            self.game.display.fill((0,0,0))
            self.game.check_events(self.chat_player)

            self.chat_player.update_chat()
            self.chat_player.draw_chat(self.game.display)

            pygame.display.flip()

            self.game.draw_text("Pseudo :", 60, self.pseudox -300, self.pseudoy )
            self.game.draw_text("MDP :", 60, self.mdpx -300, self.mdpy + 100)
            self.game.draw_text("Valide :", 60, self.mailx, self.maily + 300)
            self.blit_screen()
            
            

            


class Inscription(Menu):
    def __init__(self, game):
        Menu.__init__(self,game)
        self.state = 'Inscription'
        self.pseudox, self.pseudoy = self.mid_w, self.mid_h + 20
        self.mdpx, self.mdpy = self.mid_w, self.mid_h + 40
        self.mailx, self.maily = self.mid_w, self.mid_h + 40
        self.validex, self.validey = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.pseudox + self.offset, self.pseudoy)

    def display_menu(self):

        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0,0,0))
            self.game.draw_text('Inscription', 80,self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 250)
            self.game.draw_text("Pseudo :", 60, self.pseudox -300, self.pseudoy )
            self.game.draw_text("MDP :", 60, self.mdpx -300, self.mdpy + 100)
            self.game.draw_text("Mail :", 60, self.mailx -300, self.maily + 200)
            self.game.draw_text("Valide :", 60, self.mailx, self.maily + 300)
            self.blit_screen()

    

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == "Pseudo :":
                self.state = "MDP :"
                self.cursor_rect.midtop = (self.mdpx + self.offset , self.mdpy)
            elif self.state == "MDP :":
                self.state = "Mail :"
                self.cursor_rect.midtop = (self.mailx + self.offset, self.maily)
            elif self.state == "Mail :":
                self.state = "Pseudo :"
                self.cursor_rect.midtop = (self.pseudox + self.offset, self.pseudoy)
        elif self.game.START_KEY:
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True

        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Fait par:', 80, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 80)
            self.game.draw_text("David Plessix", 60, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 +40)
            self.blit_screen()
        

        
        
        