import pygame
import sys
import math
from pacman import run_game
from board import boards, test_board, randomize_board
from generate import create_game_tree, populate_tree, print_tree
from image_captioning import predict_step
import start_screen

# pygame.init()

#     while True:
#         pygame.display.flip()
#     pygame.quit()

# if __name__ == '__main__':
#     run_game()