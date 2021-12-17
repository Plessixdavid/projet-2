# coding : utf-8

import pygame

from animation import animate_sprite

class Player (animate_sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = self.get_image(32, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()

    def save_location(self):
        self.old_position = self.position.copy()

    def move_up(self): 
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            self.position[1] -= self.speed*2
            self.speed_clock = 130
        else:
            self.position[1] -= self.speed
            self.speed_clock = 180

    def move_down(self): 
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            self.position[1] += self.speed*2
            self.speed_clock = 130
        else:
            self.position[1] += self.speed
            self.speed_clock = 180

    def move_right(self): 
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            self.position[0] += self.speed*2
            self.speed_clock = 130
        else:
            self.position[0] += self.speed
            self.speed_clock = 180

    def move_left(self): 
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            self.position[0] -= self.speed*2
            self.speed_clock = 130
        else:
            self.position[0] -= self.speed
            self.speed_clock = 180
        
    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

