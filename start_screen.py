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

    vic_track = []
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    wl, num_shards = pacman.run_game(root, 0, None)
                    if wl:
                        print("won level")
                        vic_track.append(('Won', 4))
                        change_screen_win_screen()
                    else:
                        print("lost level")
                        vic_track.append(('Loss', num_shards))
                elif event.key == pygame.K_p:
                    # xxx.run()
                    # TODO: show photos
                    pass
        pygame.display.update()
        pygame.display.flip()

    pygame.quit()

def change_screen_win_screen():
    screen = pygame.display.set_mode([900, 950])
    half_height = screen.get_height//2
    half_width = screen.get_width//2
    
    RESULT = get_font(85).render(f"You ", True, "White")
    RESULT_RECT = RESULT.get_rect(center=(half_width, 100))
    
    half_width = screen.get_width() // 2
    image_height = screen.get_height()
    render_text(screen,"Press R to return",(half_width,half_height),pygame.font.SysFont('Arial', 28),"white",half_width)


    vic_track = []
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    run = False
                    
        pygame.display.update()
        pygame.display.flip()
# main_menu()

def render_text(surface, text, pos, font, color, max_width):
    """
    Render text on the given surface with word wrapping.

    :param surface: Pygame surface where text will be drawn.
    :param text: The text to be rendered.
    :param pos: A tuple (x, y) where the text begins.
    :param font: Pygame font object used for rendering text.
    :param color: Color of the text.
    :param max_width: Maximum width in pixels for text lines.
    """
    words = text.split()
    space = 10 # Width of a space.
    max_height = font.get_height()
    x, y = pos
    line = []

    for word in words:
        # Check width of the line with the new word added
        line_width, _  = font.size(' '.join(line + [word]))
        if line_width <= max_width:
            line.append(word)
        else:
            # Draw the line and start a new one
            surface.blit(font.render(' '.join(line), True, color), (x, y))
            y += max_height  # Move to the next line
            line = [word]

    if line:
        surface.blit(font.render(' '.join(line), True, color), (x, y))   