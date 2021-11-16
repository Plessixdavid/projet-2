# Coding : utf-8

# Imports :
from game import game

# Attribution of the function Game :
g = game()

# Loop when the game is running :
while g.running:
    g.playing = True
    g.game_loop()