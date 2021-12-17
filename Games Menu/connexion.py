# Code : UTF-8

# Imports :
import pygame
from menu import *

# Creation of the class Connexion.
class Connexion():
    def __init__(self, connexion, inscription, credits):
        # To have all the fonctionnalities of pygame.
        pygame.init()

        # Variables of menu :
        self.running = True           # When the connexion is started but not played.
        self.playing = False          # When the player really start the connexion.

        # All keys are false until the player choose one and become true.
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        
        # Variables to display the background :
            # A modifier pour avoir un Fullscreen.
        self.DISPLAY_WIDTH = 600
        self.DISPLAY_HEIGHT = 600   
        self.display = pygame.Surface((self.DISPLAY_WIDTH,self.DISPLAY_HEIGHT))
        self.window = pygame.display.set_mode(((self.DISPLAY_WIDTH,self.DISPLAY_HEIGHT)))
        
        # Font for the menu :
        # self.font_name = 'Lato'
        self.font_name = pygame.font.get_default_font()
        # Colors (RGB) of the font :
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        self.main_menu = connexion
        self.inscription = inscription
        self.credits = credits
        self.curr_menu = self.main_menu

        self.mid_width = self.DISPLAY_WIDTH / 2
        self.mid_height = self.DISPLAY_HEIGHT / 2
        self.connexion_x, self.connexion_y = self.mid_width - 200, self.mid_height - 100
        self.inscription_x, self.inscription_y = self.mid_width - 200, self.mid_height 
        self.credits_x, self.credits_y = self.mid_width - 200, self.mid_height + 100

    # New function : loop for the connexion :
    def connexion_loop(self):
        while self.playing:
            # Verify what the player do :
            self.check_events()

            # If the player clicks on the start key :
            if self.START_KEY:
                self.playing = False     # Stop the loop without stop the connexion.
            
            # Reset the canevas :
            self.display.fill(self.black)

            self.draw_text('Connexion :', 20, (self.DISPLAY_WIDTH / 2), (self.DISPLAY_HEIGHT / 2))
            self.draw_text('Pseudo', 20, self.connexion_x, self.connexion_y)              # Créer une boîte pour rentrer le pseudo.
            self.draw_text('Mot de passe', 20, self.inscription_x, self.inscription_y)    # Créer une boîte pour rentrer le mot de passe.

            self.window.blit(self.display, (0,0))
            
            # Our screen :
            pygame.display.update()

            # Reset keys :
            self.reset_keys()

    # New function : loop for the inscription :
    def inscription_loop(self):
        while self.playing:
            # Verify what the player do :
            self.check_events()

            # If the player clicks on the start key :
            if self.START_KEY:
                self.playing = False     # Stop the loop without stop the connexion.
            
            # Reset the canevas :
            self.display.fill(self.black)

            self.draw_text('Inscription :', 20, (self.DISPLAY_WIDTH / 2), (self.DISPLAY_HEIGHT / 2))
            self.draw_text('Pseudo', 20, self.connexion_x, self.connexion_y)              # Créer une boîte pour rentrer le pseudo.
            self.draw_text('Mot de passe', 20, self.inscription_x, self.inscription_y)    # Créer une boîte pour rentrer le mot de passe.
            self.draw_text('Adresse mail', 20, self.inscription_x, self.inscription_y)    # Créer une boîte pour rentrer l'adresse mail.   
            
            self.window.blit(self.display, (0,0))
            
            # Our screen :
            pygame.display.update()

            # Reset keys :
            self.reset_keys()

    def credits_menu(self):
        self.run_display = True

        while self.run_display:
            self.check_events()

            if self.START_KEY or self.BACK_KEY :
                self.curr_menu = self.main_menu
                self.run_display = False

            self.display.fill(self.BLACK)

            self.draw_text('Credits', 20, self.DISPLAY_WIDTH / 2, self.DISPLAY_HEIGHT / 2 - 20)
            self.draw_text('Made by the team "La Licorne biffleuse". ', 15, self.DISPLAY_WIDTH / 2, self.DISPLAY_HEIGHT / 2 + 10)
            
            self.window.blit(self.display (0, 0))

    # New function : actions of the player :
    def check_events(self):
        # Loop about all the things that the player could do on the computer.
        for event in pygame.event.get():
            if event.type == pygame.QUIT :   # If the player clicks on the 'x' in the up of the window.
                # Stop the loop :
                self.running = False
                self.playing = False
                # Make all menu running stop :
                self.curr_menu.run_display = False

            if event.type == pygame.KEYDOWN:   # 'Keydown' is the touch 'Enter'.
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                    # Stop the loop :
                    self.running = False
                    self.playing = False
               
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    # New function : reset actions of the player :
    def reset_keys(self):
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False

    # New function : write on the screen :
    def draw_text(self, text, size, x, y ):
        # Font:
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.white)
        
        # Dimensions :
        text_rect = text_surface.get_rect()
        
        # Positions of the text :
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
