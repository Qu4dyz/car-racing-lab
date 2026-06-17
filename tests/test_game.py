import pytest
import pygame
import os
from unittest.mock import patch
from src.game import Game
from src.settings import *

os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()
pygame.display.set_mode((1, 1))

@pytest.fixture
def basic_game():
    """Фікстура для підготовки базового стану гри перед кожним тестом."""
    game = Game(difficulty='easy', bg_color='gray')
    
    # Забороняємо грі заходити в нескінченний цикл (while) під час створення
    with patch.object(Game, 'run'):
        game.new_game()
        
    game.playing = False 
    yield game

@pytest.mark.logic
@pytest.mark.parametrize("diff, bg_color, expected_speed, expected_color", [
    ('easy', 'white', SPEED_EASY, WHITE),
    ('hard', 'black', SPEED_HARD, BLACK),
])
def test_game_initialization(diff, bg_color, expected_speed, expected_color):
    """Параметризований тест: перевіряє чи правильно гра зчитує аргументи."""
    game = Game(difficulty=diff, bg_color=bg_color)
    assert game.difficulty == diff
    assert game.enemy_speed == expected_speed
    assert game.bg_color == expected_color

@pytest.mark.logic
def test_spawn_enemy(basic_game):
    """Тест спавну ворогів із застосуванням мокування (Mocking)."""
    initial_enemy_count = len(basic_game.enemies)
    
    with patch('random.random', return_value=0.0):
        basic_game.update()
        
    assert len(basic_game.enemies) == initial_enemy_count + 1

@pytest.mark.logic
def test_score_increment(basic_game):
    """Тест перевіряє, чи нараховуються бали за виживання."""
    basic_game.score = 0
    basic_game.update()
    assert basic_game.score >= 1