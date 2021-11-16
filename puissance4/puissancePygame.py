import pygame

pygame.draw.rect(surface, color, rect)
pygame.draw.circle(surface, color, center, radius)

#Les constantes
LARGEUR_CASE = 100
BLEU = (0,0,255)
ROUGE = (255,0,0)
JAUNE = (255,255,0)
NOIR = (0,0,0)
BLANC = (255,255,255)
RAYON= int(LARGEUR_CASE/2)-4