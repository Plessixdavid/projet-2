# coding: utf-8
import pygame
from Player import Player
from Game import Game

def main() :
    pygame.init()

    #Génère une fenetre 1080p.
    pygame.display.set_caption("projet2")
    screen = pygame.display.set_mode((1080, 720))

    Background = pygame.image.load('assets/bg.jpg')

    #Charger le jeu.
    game = Game()


    running = True

    #boucle tant que la variable est vrai.
    while running:
        #applique l'arriere plan du jeu.
        screen.blit(Background,(0 ,-200))

        #Applique l'image du player sur l'arriere plan du jeu.
        screen.blit(game.player.image, game.player.rect)

        #mettre à jour l'ecan.
        pygame.display.flip()

        #si joueur ferme la fenetre.
        for event in pygame.event.get():
            #vérif que l'event est la fermeture.
            if event.type == pygame.QUIT:
                running = False
                pygame.QUIT()
                print("fermeture du jeu")
            #Si joueur presse touche du clavier.
            elif event.type == pygame.KEYDOWN:
                #Vérif quelle touche est utilisé.
                if event.key == pygame.K_RIGHT:
                    game.player.Move_Right()
                elif event.key == pygame.K_LEFT:
                    game.player.Move_Left()
                elif event.key == pygame.K_UP:
                    game.player.Move_up()
                elif event.key == pygame.K_DOWN:
                    game.player.Move_Down()

if __name__ == "__main__":
    main()
