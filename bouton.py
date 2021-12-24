# Code : "UTF - 8"

# Imports :
import pygame
from pygame.locals import *

taille = largeur, hauteur = 800, 600
pygame.init()

fenetre = pygame.display.set_mode(taille)
largeur_bouton, hauteur_bouton = 150, 50

bouton = pygame.Surface((largeur_bouton, hauteur_bouton))

bouton.fill((180, 180, 180))
pygame.draw.rect(bouton, (255, 0, 0), bouton.get_rect(), 1)
police = pygame.font.SysFont('Arial', 20, bold = True)
texte = police.render("Cliquez ici", True, (0, 128, 0))
bouton.blit(texte, ((largeur)))