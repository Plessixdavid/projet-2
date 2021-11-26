# Code : utf-8

# Imports:
import pygame
import sys
from grid import *

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

    # Main function :
    def Main_function(self) :
        # Loop :
        while self.game_running:
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
                    
                    print(position_x, position_y)

                    # Function to stare the values :
                    self.grids.stare_the_value(position_x, position_y, 'X')

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

            # Lists :
            List_X = []               # All positions in x and y about X.
            List_O = []               # All positions in x and y about O.
            List_lines_X = []
            List_column_X = []
            List_lines_O = []
            List_column_O = []

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

                # New condition if the player win vertically :
                if List_column_X.count(0) == 3 or List_column_X.count(1) == 3 or List_column_X.count(2) == 3 :
                    print("Le joueur qui jouait avec les croix a gagné ! Félicitations.")
            
                # New condition is the player win diagonally :
                if List_lines_X == List_column_X or List_lines_X == List_column_X[::-1] :
                    print("Le joueur qui jouait avec les croix a gagné ! Félicitations.")


            # Colors of the windows :
            self.screen.fill((240, 240, 240))

            # Display the lines of the grids :
            self.grids.display_lines()

            # Update the screen :
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    Game().Main_function()
    pygame.QUIT() 