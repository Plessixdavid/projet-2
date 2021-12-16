# Code : UTF-8

# Imports :
from connexion import *

g = Connexion()

while g.running:
    g.curr_menu.display_menu()
    g.connexion_loop()
    g.inscription_loop()
    g.credits_menu()