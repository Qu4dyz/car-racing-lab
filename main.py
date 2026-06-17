import argparse
import sys
from src.game import Game

def parse_args():
    parser = argparse.ArgumentParser(description="Car Racing Game")
    parser.add_argument('--difficulty', type=str, choices=['easy', 'hard'], default='easy',
                        help='Set game difficulty (speed)')
    # Додаємо вибір кольору фону
    parser.add_argument('--bg-color', type=str, choices=['gray', 'black', 'white'], default='gray',
                        help='Set background color of the road')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()

    # Передаємо обидва аргументи в гру
    game = Game(difficulty=args.difficulty, bg_color=args.bg_color)

    while game.running:
        game.new_game()