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
        self.font_name = pygame.font.match_font('arial')

        self.difficulty = difficulty
        if self.difficulty == 'hard':
            self.enemy_speed = SPEED_HARD
        else:
            self.enemy_speed = SPEED_EASY

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def new_game(self):
        self.score = 0
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            
        if self.running:
            self.show_go_screen()

    def update(self):
        self.all_sprites.update()
        self.score += 1

        if len(self.enemies) < 5: 
            if pygame.time.get_ticks() % 100 == 0: 
                self.spawn_enemy()

        hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
        if hits:
            self.playing = False

    def spawn_enemy(self):
        e = Enemy(self.enemy_speed)
        self.all_sprites.add(e)
        self.enemies.add(e)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(GRAY)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, WHITE, SCREEN_WIDTH / 2, 15) 
        pygame.display.flip()

    def show_go_screen(self):
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER", 64, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text(f"Твій рахунок: {self.score}", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.draw_text("Натисни будь-яку клавішу для рестарту", 18, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
        pygame.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        pygame.time.wait(500) 
        pygame.event.clear() 
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    waiting = False