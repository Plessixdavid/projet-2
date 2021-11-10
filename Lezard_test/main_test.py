import pygame
from game import Game

pygame.init()



pygame.display.set_caption("test pygame")
screen = pygame.display.set_mode((800,780))

background_screen = pygame.image.load("Lezard_test/algatia.png")

game = Game()

run_is_game = True

while run_is_game:

    screen.blit(background_screen,(-970,-450))

    screen.blit(game.player.image,game.player.rect)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()

    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
        game.player.move_up()

    if game.pressed.get(pygame.K_DOWN) and game.player.rect.y + game.player.rect.height < screen.get_height():
        game.player.move_down()


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_is_game = False
            pygame.quit()
            print("Fermeture du jeu.")

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False











            # if event.key == pygame.K_RIGHT:
            #     game.player.move_right()

            # elif event.key == pygame.K_LEFT:
            #     game.player.move_left()
