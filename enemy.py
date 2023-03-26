import pygame
import random

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.flip(pygame.image.load
                ("images\space_ship-2.png"), False, True)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.x = random.randrange((300) - self.rect.width)
        self.rect.y = random.randrange((400) - self.rect.height)
        self.speed_x = random.randrange(1,10)
        self.speed_y = random.randrange(1,10)

    def update(self):
        # actualiza esto cada vuelta de bucle
        self.rect.y += 1
        if self.rect.top > 580:
                self.rect.bottom = 0
        # go horizontal
        # self.rect.x += 1
        # if self.rect.left > SCREEN_WIDTH:
        #     self.rect.right = 0


