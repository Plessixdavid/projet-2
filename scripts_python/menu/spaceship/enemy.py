import pygame
from random import randint
from BDD.DBUtil import DBUtil


# Création de la classe des ennemis
class Enemy(pygame.sprite.Sprite):

    def __init__(self, game, xp):
        super().__init__()
        self.game = game
        self.health = 100 
        self.max_health = 100
        self.attack = DBUtil.ExecuteQuery('SELECT enemy_attack FROM spaceship_settings')[0][0]
        self.image = pygame.image.load("scripts_python/menu/spaceship/assets/nibbler.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = 1800
        self.rect.y = randint(50, 600)
        self.max_rect_y = self.rect.y + 50
        self.minus_rect_y = self.rect.y - 50 
        self.velocity = randint(2,5)
        self.velocity_y = DBUtil.ExecuteQuery('SELECT enemy_velocity FROM spaceship_settings')[0][0]
        self.xp = DBUtil.ExecuteQuery('SELECT enemy_attack FROM spaceship_settings')[0][0]

    def damage(self, amount, player):
        self.health -= amount
        self.explose_music = pygame.mixer.Sound('scripts_python/menu/spaceship/assets/sounds/stomp.wav')
        self.explose_music.play()

        if self.health <= 0:
            self.health = self.max_health
            self.rect.x = 1800
            self.rect.y = randint(50, 600)
            self.max_rect_y = self.rect.y + 50
            self.minus_rect_y = self.rect.y - 50 
            self.velocity = randint(2, 5)
            self.velocity_y = 1
            player.gain_xp(self.xp)


    def update_health_bar(self, surface):

        pygame.draw.rect(surface, (1, 0, 0), [self.rect.x, self.rect.y ,self.max_health ,5])
        pygame.draw.rect(surface, (255 , 45, 0), [self.rect.x, self.rect.y ,self.health ,5])

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
            if self.rect.y <= self.minus_rect_y:
                self.velocity_y = -self.velocity_y
            if self.rect.y >= self.max_rect_y:
                self.velocity_y = -self.velocity_y
            self.rect.y += self.velocity_y
        else:
            self.game.player.damage(self.attack)
            
            
        
                    
            

        