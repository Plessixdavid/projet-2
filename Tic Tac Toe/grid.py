# Code : utf-8

# Imports :
import pygame

# New class :
class Grid:
    # Function init :
    def __init__(self, screen):
        # Define the screen :
        self.screen = screen
        # Lines of the grids :
        self.lines = [                  # List.
            ((200, 0), (200, 600)),     # First line.
            ((400, 0),(400, 600)),      # Second line.
            ((0, 200), (600, 200)),     # Third line.
            ((0, 400), (600, 400))      # Fourth line.
            ]
        # Init the grid :
        self.grid = [[None for x in range(0, 3)] for y in range(0, 3)]

        # Init a variable to verify ig the counter is 'ON' :
        self.counter_on = False

    # New function to display the lines :
    def display_lines(self):
        # For each lines in self :
        for line in self.lines :
            # Display the lines :
                # Function pygame + color + start + end + thickness.
            pygame.draw.line(self.screen, (0, 0, 0), line[0], line[1], 2)

        # Display X and O :
            # Loop through the lines :
        for y in range(0, len(self.grid)):
            # Loop through the columns :
            for x in range(0, len(self.grid)):
                # Condition to draw the lines :
                if self.grid[y][x] == 'X':
                    # Pygame + draw line + black color + start position + end position + thickness.
                    pygame.draw.line(self.screen, (0, 0, 0), (x * 200, y * 200), (200 * (x * 200), 200 * (y * 200)), 3)
                    pygame.draw.line(self.screen, (0, 0, 0), ((x * 200), 200 * (y * 200)), (200 * (x * 200), (y * 200)), 3)
                elif self.grid[y][x] == 'O':
                    # Pygame + draw circle + black color + start position + end position + radius + thickness.
                    pygame.draw.circle(self.screen, (0, 0, 0), (100 * (x * 200), 100 * (y * 200)), 100, 3)


    # New function to print the grid :
    def print_grid(self):
        print(self.grid)

    # New function to stare the values :
    def stare_the_value(self, x, y, value):
        # Condition if the box had the value None :
        if self.grid[y][x] == None:
            self.grid[y][x] = value
            # The counter is 'ON' :
            self.counter_on = True

    # New function to stare the value at None :
    def stare_None(self, line, column, value):
        self.grid[line][column] = value