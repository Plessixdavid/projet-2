import pygame
from pygame import surface
from menu.spaceship.projectile import Projectile
from menu.spaceship.enemy import Enemy


# Création du joueur.
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 50
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("scripts_python/menu/spaceship/assets/ship.png")
        self.rect = self.image.get_rect()
        self.rect.x = 25
        self.rect.y = 360
        self.current_xp = 0
        self.max_xp = 500
        self.total_xp = 0
        self.current_level = 1
        
        

    def update_level_bar(self,surface):
        # Dessiner la barre de level       
        
        pygame.draw.rect(surface, (0, 0, 0), [
            0, #position en x
            surface.get_height() -75, #position en y
            surface.get_width(), # 
            25
            ])
        pygame.draw.rect(surface, (187, 11, 11), [
            0,
            surface.get_height() - 75,
            (surface.get_width()/ self.max_xp) * self.current_xp,
            25])
        score_text = pygame.font.Font('scripts_python/menu/spaceship/assets/FreckleFace-Regular.ttf', 40).render(f'Score: {self.total_xp}', True, (247, 255, 0 ))
        surface.blit(score_text, (50, surface.get_height() - 150))
        level_text = pygame.font.Font('scripts_python/menu/spaceship/assets/FreckleFace-Regular.ttf', 40).render(f'Level: {self.current_level}', True, (247, 255, 0 ))
        surface.blit(level_text, (50, surface.get_height() - 200))

    def gain_xp(self, xp, ):
        self.current_xp += xp
        self.total_xp += self.current_xp
        if self.current_xp == self.max_xp:
            # self.current_xp = self.current_xp - self.max_xp
            self.current_level += 1
            self.max_xp += 500
            self.game.spawn_enemy(25)
            
            
    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def update_health_bar(self, surface):

        pygame.draw.rect(surface, (1, 0, 0), [
            self.rect.x + 20, 
            self.rect.y - 20,
            self.max_health,
            5
            ])
        pygame.draw.rect(surface, (247, 255, 0 ), [
            self.rect.x + 20,
             self.rect.y - 20,
             self.health,
             5
             ])

    def lunch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_enemy):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity