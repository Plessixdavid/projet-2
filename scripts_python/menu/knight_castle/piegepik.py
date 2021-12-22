import pygame
from menu.knight_castle.tiles import AnimatedTile
from random import randint

class PiegePik(AnimatedTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y,'scripts_python/menu/knight_castle/graphics/separate/items/Spike')
        self.rect.y += size - self.image.get_size()[1]
        self.speed = randint(3,5)

#création de la fonction mouvement.
    def move(self):
        self.rect.y += self.speed 
#fonctionne avec le randint qui permet une variation de la vitesse.

    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
