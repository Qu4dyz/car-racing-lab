import pytest
import pygame
import os
from unittest.mock import patch
from src.game import Game
from src.settings import *

# Заглушка для відеодрайвера, щоб Pygame міг працювати на сервері GitHub без монітора
os.environ["SDL_VIDEODRIVER"] = "dummy"

# 1. Фікстури (Fixtures) та Мокування (Mocking)
@pytest.fixture
def basic_game():
    """Фікстура, яка створює об'єкт гри з підміненими (мокнутими) зображеннями."""
    with patch('pygame.image.load', return_value=pygame.Surface((50, 80))), \
         patch('pygame.display.set_mode', return_value=pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))):
        game = Game(difficulty='easy', bg_color='gray')
        game.new_game()
        game.playing = False # Зупиняємо цикл, щоб тест не завис
        yield game

# 2. Тестові маркери (Markers) та Параметризація (Parametrization)
@pytest.mark.logic
@pytest.mark.parametrize("diff, bg_color, expected_speed, expected_color", [
    ('easy', 'white', SPEED_EASY, WHITE),
    ('hard', 'black', SPEED_HARD, BLACK),
])
def test_game_initialization(diff, bg_color, expected_speed, expected_color):
    """Перевіряє, чи правильно гра зчитує аргументи складності та кольору."""
    with patch('pygame.image.load', return_value=pygame.Surface((50, 80))), \
         patch('pygame.display.set_mode', return_value=pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))):
        game = Game(difficulty=diff, bg_color=bg_color)
        assert game.difficulty == diff
        assert game.enemy_speed == expected_speed
        assert game.bg_color == expected_color

@pytest.mark.logic
def test_spawn_enemy(basic_game):
    """Перевіряє роботу методу спавну ворогів."""
    initial_enemy_count = len(basic_game.enemies)
    basic_game.spawn_enemy()
    assert len(basic_game.enemies) == initial_enemy_count + 1

@pytest.mark.logic
def test_score_increment(basic_game):
    """Перевіряє, чи нараховуються бали під час оновлення ігрового кадру."""
    basic_game.score = 0
    basic_game.update()
    assert basic_game.score == 1