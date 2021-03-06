import pygame
from menu.knight_castle.tiles import AnimatedTile
from random import randint

class Enemy(AnimatedTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y,'scripts_python/menu/knight_castle/graphics/enemy/run')
        self.rect.y += size - self.image.get_size()[1]
        self.speed = randint(3,5)

#création de la fonction mouvement.
    def move(self):
        self.rect.x += self.speed 
#fonctionne avec le randint qui permet une variation de la vitesse.

#création de la fonction reverse qui permet un flip de l'ennemi.
    def reverse_image(self):
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image,True,False)

    def reverse(self):
        self.speed *= -1

    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverse_image()