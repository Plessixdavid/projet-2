# Coding : utf-8

# Imports :
import pygame 

# Creation of the class Game.
class game():
    def __init__(self):

        # To have all the fonctionnalities of pygame.
        pygame.init()

        # Variables of menu :
        self.running = True           # When the game is started but not played.
        self.playing = False          # When the player really start the game.
        # All keys are false until the player choose one and become true.
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

        # Variables to display the background :
        self.display_width = 800
        self.display_height = 800
        self.display = pygame.Surface((self.display_width, self.display_height))
        self.window = pygame.display.set_mode((self.display_width, self.display_height))

        # Font for the menu :
        self.font_name = 'Menu System/8-BIT WONDER.TTF'
        # self.font_name = pygame.font.get_default_font()
        # Colors (RGB) of the font :
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

    # New function : loop for the game :
    def game_loop(self):
        while self.playing:
            # Verify what the player do :
            self.check_events()

            # If the player clicks on the start key :
            if self.START_KEY:
                self.playing = False     # Stop the loop without stop the game.

            # Reset the canevas :
            self.display.fill(self.black)
            self.draw_text('Thanx for playing', 20, self.display_width/2, self.display_height/2)     # self.display/2 : operation to put the text in the center.
            self.window.blit(self.display, (0, 0, ))       # x and y of the window.

            # Our screen :
            pygame.display.update()

            # Reset keys :
            self.reset_keys()

        # Close the window of Pygame:
        pygame.quit()

    # New function : actions of the player :
    def check_events(self):
        # Loop about all the things that the player could do on the computer.
        for event in pygame.event.get():
            if event.type == pygame.QUIT :   # If the player clicks on the 'x' in the up of the window.
                # Stop the loop :
                self.running = False
                self.playing = False
            
            if event.type == pygame.KEYDOWN:   # 'Keydown' is the touch 'Enter'.
                if event.type == pygame.K_RETURN:   
                    self.start_key = True
                
                if event.type == pygame.K_BACKSPACE:
                    self.back_key = True
                
                if event.type == pygame.K_DOWN:    
                    self.down_key = True
                
                if event.type == pygame.K_UP:
                    self.up_key = True

    # New function : reset actions of the player :
    def reset_keys(self):
        self.up_key = False
        self.down_key = False
        self.start_key = False
        self.back_key = False

    # New function : write on the screen :
    def draw_text(self, text, size, x, y ):
        # Font:
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.white)
        
        # Dimensions :
        text_rect = text_surface.get_rect()

        # Positions of the text :
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)