import pygame
import sys
import pacman
# TODO: import view photo files

# pygame.init()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/fonts/font.ttf", size)

def main_menu(screen):
    screen = pygame.display.set_mode([900, 950])
    pygame.display.set_caption("Menu")
    
    MENU_TEXT = get_font(85).render("MAIN MENU", True, "White")
    MENU_RECT = MENU_TEXT.get_rect(center=(450, 100))

    START_TEXT = get_font(50).render("START[S]", True, "Blue")
    START_RECT = START_TEXT.get_rect(center=(450, 450))
    PHOTOS_TEXT = get_font(50).render("VIEW PHOTOS[P]", True, "Blue")
    PHOTOS_RECT = PHOTOS_TEXT.get_rect(center=(450, 550))

    screen.blit(MENU_TEXT, MENU_RECT)
    screen.blit(START_TEXT, START_RECT)
    screen.blit(PHOTOS_TEXT, PHOTOS_RECT)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    pacman.run_game()
                elif event.key == pygame.K_p:
                    # xxx.run()
                    # TODO: show photos
                    pass
        pygame.display.update()
        pygame.display.flip()