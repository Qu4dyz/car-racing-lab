import pygame
import sys
from src.settings import *
from src.entities import Player, Enemy

class Game:
    def __init__(self, difficulty='easy'):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

        self.difficulty = difficulty
        if self.difficulty == 'hard':
            self.enemy_speed = SPEED_HARD
        else:
            self.enemy_speed = SPEED_EASY

    def new_game(self):
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

        self.run()

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

        if len(self.enemies) < 5:
            if pygame.time.get_ticks() % 100 == 0:
                self.spawn_enemy()

        hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
        if hits:
            self.playing = False
            self.running = False

    def spawn_enemy(self):
        e= Enemy(self.enemy_speed)
        self.all_sprites.add(e)
        self.enemies.add(e)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(GRAY)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def show_go_screen(self):
        pass