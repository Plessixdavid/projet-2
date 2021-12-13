# coding : utf-8

import pygame

class animate_sprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.sprite_sheet = pygame.image.load("Sprites\Dragons\Sprite dragon vert.png")
        self.animation_index = 1
        self.clock = 0
        self.images = {
        "down" : self.get_images(0),
        "left" : self.get_images(32),
        "right" : self.get_images(64),
        "up" : self.get_images(96)
        }
        self.speed = 2
        self.speed_clock = 130

    def change_animation(self, name):
        self.image = self.images[name][self.animation_index]
        self.image.set_colorkey((0, 0, 0))
        self.clock += self.speed * 8

        if self.clock >= self.speed_clock:

            self.animation_index += 1 #pour passer à l'image suivante

            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0

            self.clock = 0

    def get_images(self, y):
        images = []
        for i in range(0, 4):
            x = i * 32
            image = self.get_image(x, y)
            images.append(image)

        return images

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image