import pygame
from pygame import joystick
from pygame.constants import JOYAXISMOTION, JOYBUTTONDOWN, JOYBUTTONUP, JOYHATMOTION
from player import Player
from game import Game
from enemy import Enemy
import math

def start():
    pygame.init()


    # génère la fenêtre du jeu et charge des images en memoire et change le nom de la fenêtre ainsi que l'icon.
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    icons = pygame.image.load("spaceship/assets/icons/bender.png")
    background = pygame.image.load("spaceship/assets/bg4.png")

    banner = pygame.image.load("spaceship/assets/futu.png")
    banner = pygame.transform.scale(banner ,(500,500))
    banner_rect = banner.get_rect()
    banner_rect.x = math.ceil(screen.get_width() / 4 + 150)
    banner_rect.y = math.ceil(screen.get_height() / 4 -150)

    play_button = pygame.image.load("spaceship/assets/button.png")
    play_button = pygame.transform.scale(play_button, (400, 150))
    play_button_rect = play_button.get_rect()
    play_button_rect.x = math.ceil(screen.get_width() / 4 + 200)
    play_button_rect.y = math.ceil(screen.get_height() / 2 + 200)
    pygame.display.set_caption("Planet Express")
    pygame.display.set_icon(icons)

    joystick = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    pygame.joystick.init()

    game = Game()


    running = True
    while running:

        
        # Applique et actualise le fond de l'ecran.
        screen.blit(background, (0,0))

        if game.is_playing:
            game.update(screen)
        else:
            screen.blit(banner,banner_rect)
            screen.blit(play_button, play_button_rect)

        pygame.display.flip()

        # Si le joueur ferme la fenêtre.
        for event in pygame.event.get():
            if event.type == pygame.JOYHATMOTION:
                print(event)
                # Permet d'actionner la croix  directionnel de la manette.
                if event.value[0] == 1:
                    game.pressed["DPAD_RIGHT"] = True
                if event.value[0] == -1:
                    game.pressed["DPAD_LEFT"] = True
                if event.value[1] == 1:
                    game.pressed["DPAD_UP"] = True 
                if event.value[1] == -1:
                    game.pressed["DPAD_DOWN"] = True
                # Permet de reset les comamandes en X
                if event.value[0] == 0:
                    game.pressed["DPAD_RIGHT"] = False
                    game.pressed["DPAD_LEFT"] = False
                # Permet de rest les commandes en Y
                if event.value[1] == 0:
                    game.pressed["DPAD_UP"] = False
                    game.pressed["DPAD_DOWN"] = False
            if event.type == JOYBUTTONDOWN:
                print(event)
                if event.button == 9:
                    game.start()
                if event.button == 8 :
                    running = False
                    pygame.quit()
                elif event.button == 1 or 2 or 3 or 0 :
                    game.player.lunch_projectile()
                    
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                if event.key == pygame.K_SPACE:
                    game.player.lunch_projectile()
                elif event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.player.lunch_projectile()
                if play_button_rect.collidepoint(event.pos):
                    game.start()

if __name__ == "__main__":
    start()