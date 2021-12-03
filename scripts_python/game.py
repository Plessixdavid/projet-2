# coding : utf-8

import pygame
from map import MapManager
from player import Player

class Game:

    def __init__(self):
        # créer la fenetre du jeu
        self.screen = pygame.display.set_mode((900,780))
        pygame.display.set_caption("PYGAMON")

        # generer un joueur
        self.player = Player(0, 0)
        self.map_manager = MapManager(self.screen, self.player)

    # recuperation des touche pour le deplacement
    def handle_input(self):
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation("up")

        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation("down")

        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation("right")

        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation("left")

    def update(self):
        self.map_manager.update()

    def run(self):

        # gerer les FPS
        clock = pygame.time.Clock()
        
        # boucle du jeu
        running = True

        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()
