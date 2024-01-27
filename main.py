import pygame
import sys
import math
from pacman import run_game
from board import boards, test_board, randomize_board

WIDTH = 900
HEIGHT = 950

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("TwoPac")
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

    # Loading screen loop
    loading = True
    while loading:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill((0, 0, 0))
        
        # Draw the circular loading icon
        start_angle = math.radians(angle)
        end_angle = math.radians(angle + 270)
        pygame.draw.arc(screen, color, (center[0]-radius, center[1]-radius, radius*2, radius*2), start_angle, end_angle, thickness)

        padding = 30
        loading_text = font.render('Loading...', True, color)
        text_rect = loading_text.get_rect(center=(center[0], center[1] + radius + 40)) 
        screen.blit(loading_text, text_rect)

        angle = (angle + 5) % 360

        pygame.display.flip()

        if pygame.time.get_ticks() - start_time > loading_duration:
            loading = False
        clock.tick(60)
        
    run_game()
