import pygame
from random import randint


# Création de la classe des enemies
class Enemy(pygame.sprite.Sprite):

    def __init__(self, game, xp):
        super().__init__()
        self.game = game
        self.health = 100 
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load("spaceship/assets/nibbler.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = 1800
        self.rect.y = randint(50, 600)
        self.max_rect_y = self.rect.y + 50
        self.minus_rect_y = self.rect.y - 50 
        self.velocity = randint(2,5)
        self.velocity_y = 1
        self.xp = 100

    def damage(self, amount, player):
        self.health -= amount
        self.explose_music = pygame.mixer.Sound('spaceship/assets/sounds/stomp.wav')
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
            
            
        
                    
            

        