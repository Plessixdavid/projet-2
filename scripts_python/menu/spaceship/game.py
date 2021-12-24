import pygame
from menu.spaceship.player import Player
from menu.spaceship.enemy import Enemy
import math
from BDD.DBUtil import DBUtil
# Création de la classe game.
class Game1:

    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_enemy = pygame.sprite.Group()
        self.spawn_enemy(25) 
        self.spawn_enemy(25)
        self.total_xp = None
        
        
        
        self.pressed = {}
        

    def start(self):
        self.is_playing = True
        
        self.start_music = pygame.mixer.Sound('scripts_python/menu/spaceship/assets/sounds/starts.wav')
        self.start_music.play(loops = -1)


    def game_over(self):
        self.all_enemy = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        Query = "INSERT INTO spaceship (score, nameid ) VALUES (%s, %s)"
        Values = (self.current_xp, 16)
        DBUtil.ExecuteQuery(Query, Values)
        self.current_xp = 0
        self.max_xp = 500
        self.total_xp = 0
        self.current_level = 1



    def update(self, screen):
        # affiche la barre de santé
        self.player.update_health_bar(screen)

        #affiche la barre de level
        self.player.update_level_bar(screen)

        # récupère les projectiles du joueur.
        for projectile in self.player.all_projectiles:
            projectile.move()


        for enemy in self.all_enemy:
            enemy.forward()
            enemy.update_health_bar(screen)

        # Applique le projectile sur le screen derrière le joueur.
        self.player.all_projectiles.draw(screen)

        # Applique l'image du joueur.
        screen.blit(self.player.image, self.player.rect)

        # Applique les ennemis.
        self.all_enemy.draw(screen)

        if (self.pressed.get(pygame.K_d) or self.pressed.get("DPAD_RIGHT")) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif (self.pressed.get(pygame.K_q) or self.pressed.get("DPAD_LEFT")) and self.player.rect.x > 0:
            self.player.move_left()
        elif (self.pressed.get(pygame.K_z) or self.pressed.get("DPAD_UP")) and self.player.rect.y > 0:
            self.player.move_up()
        elif (self.pressed.get(pygame.K_s) or self.pressed.get("DPAD_DOWN")) and self.player.rect.y < 625:
            self.player.move_down()
    
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_enemy(self, xp):
        enemy = Enemy(self, xp)
        self.all_enemy.add(enemy)