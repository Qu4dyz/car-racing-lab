import pygame
import random
from src.settings import *

from SoloProjectCICD.src.settings import PLAYER_START_X, SCREEN_WIDTH


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()

        self.rect.centerx = PLAYER_START_X
        self.rect.bottom = PLAYER_START_Y

        self.speed_x = 0

    def update(self):
        self.speed_x = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -PLAYER_SPEED
        if keystate[pygame.K_RIGHT]:
            self.speed_x = PLAYER_SPEED

        self.rect.x += self.speed_x

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed_y):
        super().__init__()
        self.image = pygame.Surface((50, 80))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = speed_y

    def update(self):
        self.rect.y += self.speed_y

        if self.rect.top > SCREEN_HEIGHT + 10:
            self.kill()