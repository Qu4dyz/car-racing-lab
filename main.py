import argparse
import sys
from src.game import Game

def parse_args():
    parser = argparse.ArgumentParser(description="Car Racing Game")
    parser.add_argument('--difficulty', type=str, choices=['easy', 'hard'], default='easy',
                        help='Set game difficulty (speed)')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()

    game = Game(difficulty=args.difficulty)

    while game.running:
        game.new_game()