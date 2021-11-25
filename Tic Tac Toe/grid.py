# Code : utf-8

# Imports :
import pygame

# New class :
class Grid:
    # Function init :
    def __init__(self):
        # Lines of the grids :
        self.lines = [                  # List.
            ((200, 0), (200, 600)),     # First line.
            ((400, 0),(400, 600)),      # Second line.
            ((0, 200), (600, 200)),     # Third line.
            ((0, 400), (600, 400))      # Fourth line.
            ]

