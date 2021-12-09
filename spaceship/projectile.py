import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load("spaceship/assets/laser.png")
        self.image = pygame.transform.scale(self.image,(40,8))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 70
        self.rect.y = player.rect.y + 50

    def remove(self):
        self.player.all_projectiles.remove(self)


    def move(self):

        self.rect.x += self.velocity

        for enemy in self.player.game.check_collision(self, self.player.game.all_enemy):
            self.remove()
            enemy.damage(self.player.attack, self.player)
            
            
        if self.rect.x > 2048 and self.rect.x < 0:
            self.remove()
        
