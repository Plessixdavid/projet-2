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
        self.grid = [[None in x in range(0, 3) for y in range(0, 3)]]

    # New function to print the grid :
    def print_grid(self):
        print(self.grid)
        
    # New function to display the lines :
    def display_lines(self):
        # For each lines in self :
        for line in self.lines :
            # Display the lines :
            # Function pygame + color + start + end + thickness.
            pygame.draw.line(self.screen, (0, 0, 0), line[0], line[1], 2)