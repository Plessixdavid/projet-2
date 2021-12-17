# Code : UTF-8

# Imports :
import pygame
import sys
from background import *

# New class:
class Game :
    # Function init :
    def __init__(self):
        # Pygame's windows :
        self.screen = pygame.display.set_mode((600, 600))
        # Name of the game :
        pygame.display.set_caption('Tic Tac Toe')
        # Loop when the game is running :
        self.game_running = True
        self.grids = Grid(self.screen)
        # Init variables X and O :
        self.player_X = 'X'
        self.player_O = 'O'
        # The counter :
        self.counter = 0

        self.clicked = False
        self.game_finished = False
        
        # The screen of the beginning :
        self.screen_begin = True

    # Main function :
    def Main_function(self) :
        # Loop when the game is running :
        while self.game_running:
            # Loop when the screen is True :
            while self.screen_begin:
              # To receive all elements in pygame :
                for event in pygame.event.get():
                    # Quit the game :
                    if event.type == pygame.QUIT:
                        sys.exit() 
                    if event.type == pygame.KEYDOWN:
                        # Event for the player with Escape to have the screen of menu :
                        if event.key == pygame.K_ESCAPE:
                            print("Menu")

                    # Display the screen of the game when player clicks on space :
                    if event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_SPACE:
                           self.screen_begin = False

                # Background for the screen of the beginning :
                self.screen.fill((240, 240, 240))

                # Messages : 
                self.create_message('big', 'Tic Tac Toe', (0, 0, 0), [200, 30, 200, 50])
                self.create_message('small', 'Ce jeu se joue à deux, et chacun se verra attribuer un symbole.', (0, 0, 0), [50, 130, 400, 50])
                self.create_message('small', 'X ou O', (0, 0, 0), [220, 150, 100, 100])
                self.create_message('small', 'Le premier joueur qui réussit à aligner 3 de ses symboles gagne.', (0, 0, 0), [50, 170, 200, 50])
                self.create_message('medium', 'Pour recommencer le jeu, appuyer sur Enter.', (0, 0, 0), [70, 350, 200, 50])
                self.create_message('medium', 'Appuyer sur Espace pour commencer le jeu.', (0, 0, 0), [70, 400, 200, 50])
                self.create_message('medium', 'Pour revenir à cet écran, appuyer sur ESC.', (0, 0, 0), [70, 450, 200, 50])

                pygame.display.flip()

            # To receive all elements in pygame :
            for event in pygame.event.get():
                # Quit the game :
                if event.type == pygame.QUIT:
                    sys.exit()

                # Event : right click : 
                    # [0] : list of buttons in the mouse = right click. 
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:   
                    # Get the position of the mouse :
                    position = pygame.mouse.get_pos()
                    # Position x of the mouse :
                    position_x = position[0]//200
                    # Position y of the mouse :
                    position_y = position[1]//200
                    
                    # Condition if the counter is pair or odd :
                    if self.counter %2 == 0:
                        # The player in X who plays :
                        self.grids.stare_the_value(position_x, position_y, self.player_X)
                    else:
                        # The player in O who plays :
                        self.grids.stare_the_value(position_x, position_y, self.player_O)
                    
                    # Condition if the counter is True :
                    if self.grids.counter_on:
                        # Increment the counter +1 :
                        self.counter += 1
                        # Stare the value of counter_on as False :
                        self.grids.counter_on = False

                    self.clicked = True

                # New events :
                if event.type == pygame.KEYDOWN:
                    # Event for the player with Enter to restart the game :
                    if event.key == pygame.K_RETURN:       # Touch Enter on the clapboard.
                        self.restart()
                    # Event for the player with Escape to have the screen of beginning during the party:
                    if event.key == pygame.K_ESCAPE:
                        self.screen_begin = True

            # Lists :
            List_X = []               # All positions in x and y about X.
            List_O = []               # All positions in x and y about O.
            List_lines_X = []
            List_column_X = []
            List_lines_O = []
            List_column_O = []

            # Winner :
            self.winner(List_X, List_O, List_column_X, List_lines_X, List_column_O, List_lines_O)

            # Colors of the windows :
            self.screen.fill((240, 240, 240))

            # Display the lines of the grids :
            self.grids.display_lines()

            # Update the screen :
            pygame.display.flip()

    # New function about texts :
    def create_message(self, font, message, color, message_rectangle):
        # Font of the message :
        if font == 'small':
            # Create a Font + height + bold text = False:
            font = pygame.font.SysFont('Lato', 20, False)
        
        elif font == 'medium':
            font = pygame.font.SysFont('Lato', 30, False)

        elif font == 'big':
            font = pygame.font.SysFont('Lato', 40, True)

        message = font.render(message, True, color)
        self.screen.blit(message, message_rectangle)
    
    # New function whom attribuate the value None at all boxes :
    def restart(self):
        for line in range(0, len(self.grids.grid)):
            for column in range(0, len(self.grids.grid)):
                self.grids.stare_None(line, column, None)

    # New function for the winner :
    def winner(self, List_X, List_O, List_column_X, List_lines_X, List_column_O, List_lines_O):
        # Loop about the position of X or O :
        for line in range(0, len(self.grids.grid)):
            for column in range(0, len(self.grids.grid)):
                # Condition :
                if self.grids.grid[line][column] == 'X':
                    X_position = (line, column)
                    List_X.append(X_position)
                elif self.grids.grid[line][column] == 'O':
                    O_position = (line, column)
                    List_O.append(O_position)

        # New condition if the winner has 3 cross on the game :
        if len(List_X) >= 3:
            for (line, column) in List_X:
                List_lines_X.append(line)
                List_column_X.append(column)

            # New condition if the player win horizontally :
            if List_lines_X.count(0) == 3 or List_lines_X.count(1) == 3 or List_lines_X.count(2) == 3 :
                print("Le joueur qui jouait avec les croix a gagné ! Félicitations.")
                self.restart()
            
            # New condition if the player win vertically :
            elif List_column_X.count(0) == 3 or List_column_X.count(1) == 3 or List_column_X.count(2) == 3 :
                print("Le joueur qui jouait avec les croix a gagné ! Félicitations.")
                self.restart()

            # New condition is the player win diagonally :
            elif List_lines_X == List_column_X or List_lines_X == List_column_X[::-1] :
                print("Le joueur qui jouait avec les croix a gagné ! Félicitations.")
                self.restart()

        # New condition if the winner has 3 circles on the game :
        if len(List_O) >= 3:
            for (line, column) in List_O:
                List_lines_O.append(line)
                List_column_O.append(column)

            # New condition if the player win horizontally :
            if List_lines_O.count(0) == 3 or List_lines_O.count(1) == 3 or List_lines_O.count(2) == 3 :
                print("Le joueur qui jouait avec les ronds a gagné ! Félicitations.")
                self.restart()

            # New condition if the player win vertically :
            elif List_column_O.count(0) == 3 or List_column_O.count(1) == 3 or List_column_O.count(2) == 3 :
                print("Le joueur qui jouait avec les ronds a gagné ! Félicitations.")
                self.restart()

            # New condition is the player win diagonally :
            elif List_lines_O == List_column_O or List_lines_O == List_column_O[::-1] :
                print("Le joueur qui jouait avec les ronds a gagné ! Félicitations.")
                self.restart()
