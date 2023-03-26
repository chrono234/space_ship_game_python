import pygame
from shots import Shots

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load(
            "C:\\Users\\jairo O\\Desktop\\Alura\\space_ship_game\\images\\space_ship.png")
        self.rect = self.image.get_rect()
        # to see the radius of colition
        self.radius = 18
        # pygame.draw.circle(self.image, "green", self.rect.center, self.radius)

        # velocidad
        self.speed_x = 0
        self.speed_y = 0

    def keep_player_in_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def shot(self, bullets):
        bullet = Shots(self.rect.centerx, self.rect.top + 15)
        bullets.add(bullet)
        pygame.init()
        pygame.mixer.init()
        laser = pygame.mixer.Sound("images\music and sounds\laserShoot.wav")
        pygame.mixer.Sound.set_volume(laser, 0.1)
        laser.play()


    def shot2(self, bullets):
        bullet = Shots(self.rect.centerx + 20, self.rect.top + 27)
        bullets.add(bullet)

    def shot3(self, bullets):
        bullet = Shots(self.rect.centerx - 20, self.rect.top + 27)
        bullets.add(bullet)

    def check_key_pressed(self, bullets):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect = self.rect.move(-5,0)
        if keys[pygame.K_RIGHT]:
            self.rect = self.rect.move(5,0)
        if keys[pygame.K_UP]:
            self.rect = self.rect.move(0,-5)
        if keys[pygame.K_DOWN]:
            self.rect = self.rect.move(0,5)
        if keys[pygame.K_SPACE]:
            self.shot(bullets)
            self.shot2(bullets)
            self.shot3(bullets)

