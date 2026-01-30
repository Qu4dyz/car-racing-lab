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

        # Установка складності (argparse)
        self.difficulty = difficulty
        if self.difficulty == 'hard':
            self.enemy_speed = SPEED_HARD
        else:
            self.enemy_speed = SPEED_EASY

    def new_game(self):
        # Запуск нової гри
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

        self.run()

    def run(self):
        # Ігровий цикл (Game loop)
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Оновлення спрайтів
        self.all_sprites.update()

        # Спавн ворогів (чим складшніше, тим частіше можна зробити, але поки - рандом)
        if len(self.enemies) < 5: # Максимум 5 ворогів на екрані
            if pygame.time.get_ticks() % 100 == 0: # Проста логіка спавна
                self.spawn_enemy()

        # Перевірка зіткнень (кінець гри)
        hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
        if hits:
            self.playing = False
            self.running = False # Вихід з гри при зіткненні

    def spawn_enemy(self):
        # Створюємо ворога з встановленною швидкістю
        e= Enemy(self.enemy_speed)
        self.all_sprites.add(e)
        self.enemies.add(e)

    def events(self):
        # Обробка ввода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Відрісовка
        self.screen.fill(GRAY) # Фон дороги
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def show_go_screen(self):
        # гейм овер
        pass