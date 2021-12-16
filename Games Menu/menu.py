# Code : UTF-8

# Imports : 
import pygame

# New class : Menu :
class Menu():
    def __init__(self, connexion, inscription, credits):
        self.connexion = connexion
        self.inscription = inscription
        self.credits = credits

        # Dimensions of the screen :
        self.mid_width = self.connexion.DISPLAY_WIDTH / 2
        self.mid_height = self.connexion.DISPLAY_HEIGHT / 2
        
        # To make the menu keep running :
        self.run_display = True

        # Use arrow on clapboard :
        self.cursor_rect = pygame.Rect(0, 0, 40, 40)
        
        # Gap between the text and the cursor :
        self.offset = - 90

    # New function to draw the cursor on the screen :
    def draw_cursor(self):
        self.connexion.draw_text('*', 30, self.cursor_rect.x, self.cursor_rect.y)

    # New function to reset the canevas :
    def blit_screen(self):
        self.connexion.window.blit(self.connexion.display, (0, 0))
        pygame.display.update()
        self.connexion.reset_keys()

# New class about the menu in itself :
class MainMenu(Menu):
    def __init__(self, connexion, inscription, credits):
        # Use the class Menu, just created before :
        Menu.__init__(self, connexion, inscription, credits)

        # Cursor on the element "Start" :
        self.state = "Connexion"

        # Positions of the text and the cursor :
        self.connexion_x, self.connexion_y = self.mid_width, self.mid_height + 10
        self.inscription_x, self.inscription_y = self.mid_width, self.mid_height + 90
        self.credits_x, self.credits_y = self.mid_width, self.mid_height + 200
        self.cursor_rect.midtop = (self.connexion_x + self.offset, self.connexion_y)

    # New function to display the menu :
    def display_menu(self):
        # Make sure the menu is always true :
        self.run_display = True

        # Loop about when the screen is display :
        while self.run_display:
            # Movements of the cursor through arrows on clapboard :
            self.connexion.check_events()
            self.inscription.check_events()
            self.check_input()

            # Reset the screen :
            self.connexion.display.fill(self.connexion.black)

            # Texts :
            self.connexion.draw_text('Bienvenue dans Home !', 40, self.connexion.DISPLAY_WIDTH / 2, self.connexion.DISPLAY_HEIGHT / 4 - 20)
            self.connexion.draw_text("Connexion", 30, self.connexion_x, self.connexion_y)
            self.connexion.draw_text("Inscription", 30, self.inscription_x, self.inscription_y)
            self.connexion.draw_text("Credits", 20, self.credits_x, self.credits_y)
            
            # Draw the cursor :
            self.draw_cursor()
            # Display all the texts on the screen :
            self.blit_screen()

    # New function to move the cursor through arrows on clapoboard :
    def move_cursor(self):
        if self.connexion.DOWN_KEY:   
            # Loop about the move of the cursor to "Connexion" at "Credits" :     
            if self.state == 'Connexion':
                self.cursor_rect.midtop = (self.inscription_x + self.offset, self.inscription_y)
                self.state = 'Inscription'
            elif self.state == 'Inscription':
                self.cursor_rect.midtop = (self.credits_x + self.offset, self.credits_y)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.connexion_x + self.offset, self.connexion_y)
                self.state = 'Connexion'
        
        elif self.connexion.UP_KEY:
            # Loop about the move of the cursor to "Credits" at "Connexion" :     
            if self.state == 'Connexion':
                self.cursor_rect.midtop = (self.credits_x + self.offset, self.credits_y)
                self.state = 'Credits'
            elif self.state == 'Inscription':
                self.cursor_rect.midtop = (self.connexion_x + self.offset, self.connexion_y)
                self.state = 'Connexion'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.inscription_x + self.offset, self.inscription_y)
                self.state = 'Inscription'

    # New function to check the element choice :
    def check_input(self):

        # To make sure that the player move the cursor :
        self.move_cursor()
        
        # Navigation of the cursor between the different menus :
        if self.connexion.START_KEY:
            if self.state == 'Connexion':
                self.connexion.playing = True
            elif self.state == 'Inscription':
                self.inscription.playing = True
            elif self.state == 'Credits':
                self.credits.playing = True

            # Make the principal menu stop to display :
            self.run_display = False