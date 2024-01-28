import pygame
from generate import print_tree
import sys
import pacman
# TODO: import view photo files

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/fonts/font.ttf", size)

def get_logo(size):
    return pygame.font.Font("assets/fonts/pacman_font.TTF", size)


def main_menu(screen, root):
    screen = pygame.display.set_mode([900, 950])
    pygame.display.set_caption("Menu")
    
    MENU_TEXT = get_font(85).render("MAIN MENU", True, "White")
    MENU_RECT = MENU_TEXT.get_rect(center=(450, 330))

    LOGO_TEXT = get_logo(100).render("TU-PAC", True, "Yellow")
    LOGO_RECT = LOGO_TEXT.get_rect(center=(450, 180))

    START_TEXT = get_font(50).render("START[S]", True, "Blue")
    START_RECT = START_TEXT.get_rect(center=(450, 500))
    PHOTOS_TEXT = get_font(50).render("VIEW PHOTOS[P]", True, "Blue")
    PHOTOS_RECT = PHOTOS_TEXT.get_rect(center=(450, 600))

    LOGO_PIC = pygame.image.load("assets/logo.png").convert()
    LOGO_PIC = pygame.transform.scale(LOGO_PIC, (300, 300))

    screen.blit(MENU_TEXT, MENU_RECT)
    screen.blit(LOGO_TEXT, LOGO_RECT)
    screen.blit(START_TEXT, START_RECT)
    screen.blit(PHOTOS_TEXT, PHOTOS_RECT)
    screen.blit(LOGO_PIC, LOGO_PIC.get_rect(center=(450, 780)))
    
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    pacman.run_game(root, 0, None)
                elif event.key == pygame.K_p:
                    # xxx.run()
                    # TODO: show photos
                    pass
        pygame.display.update()
        pygame.display.flip()

# main_menu()