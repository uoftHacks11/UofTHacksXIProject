import pygame
import sys
import math
from pacman import run_game
from board import boards, test_board, randomize_board
from generate import create_game_tree, populate_tree, print_tree
from image_captioning import predict_step

WIDTH = 900
HEIGHT = 950

imgs = ['./images/biking.jpg', './images/monke.jpg', './images/rohan.jpeg']
captions = predict_step(imgs)
root = None

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Two-Pac")
    font = pygame.font.Font(None, 36)

    clock = pygame.time.Clock()
    loading_duration = 3000  # 3000 = 3 sec
    start_time = pygame.time.get_ticks()

    # Parameters for the loading icon
    center = (WIDTH // 2, HEIGHT // 2)
    radius = 50
    angle = 0
    color = (255, 255, 255)
    thickness = 5
        
    screen.fill((0, 0, 0))

    # Draw the circular loading icon
    # start_angle = math.radians(angle)
    # end_angle = math.radians(angle + 270)
    # pygame.draw.arc(screen, color, (center[0]-radius, center[1]-radius, radius*2, radius*2), start_angle, end_angle, thickness)

    padding = 30
    loading_text = font.render('Loading...', True, color)
    text2 = font.render('Analyzing Imgaes...', True, color)
    text3 = font.render('Extracting Memories...', True, color)
    text_rect = loading_text.get_rect(center=(center[0], center[1] + radius - 10)) 
    screen.blit(loading_text, text_rect)
    screen.blit(text2, text2.get_rect(center=(center[0], center[1] + radius + 20)))
    screen.blit(text3, text3.get_rect(center=(center[0], center[1] + radius + 50)))

    pygame.display.flip()

    root = create_game_tree(imgs)
    loadingComplete = populate_tree(root, captions)

        # angle = (angle + 5) % 360

        # if pygame.time.get_ticks() - start_time > loading_duration:
        #     loadingComplete = True
        # clock.tick(60)

    root = create_game_tree(imgs)
    loadingComplete = populate_tree(root, captions)
    
    # print_tree(root)
        
    run_game()
