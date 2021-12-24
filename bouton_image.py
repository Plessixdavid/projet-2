# Code : "UTF-8"

# Imports :
import pygame
from pygame.locals import *

taille = largeur, hauteur = 800, 600
pygame.init()
fenetre = pygame.display.set_mode(taille)
bouton = pygame.image.load("Skin/Licorne_1.png")
bouton_rectangle_position = bouton.get_rect()
bouton_rectangle_position.center = (largeur / 2, hauteur / 2)

continuer = True
bouton_enfonce = False

while continuer :
    for event in pygame.event.get() :
        if event.type == QUIT :
            continuer = False
        if event.type == MOUSEBUTTONDOWN and event.button == 1 and bouton_rectangle_position.collidepoint(event.pos) :
           bouton_enfonce = True
           bouton_rectangle_position = bouton_rectangle_position.move(2, 2)
        if event.type == MOUSEBUTTONUP and bouton_enfonce :
            bouton_rectangle_position = bouton_rectangle_position.move(-2, -2)
            bouton_enfonce = False
    
    fenetre.fill((255, 255, 255))
    fenetre.blit(bouton, bouton_rectangle_position)
    pygame.display.flip()

pygame.quit()