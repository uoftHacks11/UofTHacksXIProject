# Build Pac-Man from Scratch in Python with PyGame!!
import copy
from board import boards, test_board
from generate import print_tree
import pygame
import math
from trees import Story, Tree
from splitImage import split_image
from start_screen import change_screen_win_screen

pygame.init()

SPLIT_COUNT = 3

class Shard():

    # num_found = 0
    # use 3 - SPLIT_COUNT instaed

    def __init__(self, sprite, image, split, caption, story, black):
        self.sprite = sprite
        self.image = image
        self.split = split # split in ["left", "right", "up", "down"]
        self.caption = caption
        self.story = story
        self.black = black
    
    
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
 
def draw_images(shard_list,screen, width, height):
    global SPLIT_COUNT
    half_width = screen.get_width() // 2
    image_height = screen.get_height()
    image1 = shard_list[0].image
    image2 = shard_list[1].image
    image3 = shard_list[2].image
    image4 = shard_list[3].image
    black = pygame.image.load('./black.png').convert_alpha()
    # black_image = pygame.transform.scale(black_image, (half_width//1.15, image_height//2.25))
    image1 = pygame.transform.scale(image1, (200, 200)) if SPLIT_COUNT <= 2 else black
    image2 = pygame.transform.scale(image2, (200, 200)) if SPLIT_COUNT <= 1 else black
    image3 = pygame.transform.scale(image3, (200, 200)) if SPLIT_COUNT <= 0 else black
    image4 = pygame.transform.scale(image4, (200, 200)) if SPLIT_COUNT < 0 else black
    screen.blit(image1, (0, 200))
    screen.blit(image2, (0 + image1.get_width(), 200))
    screen.blit(image3, (0, 200 + image1.get_height()))
    screen.blit(image4, (0 + image1.get_width(), 200 + image1.get_height()))
    
        

def change_screen_shard_collected(screen, width, height, shard_list):
    global SPLIT_COUNT
    screen = pygame.display.set_mode([width, height])
    image = shard_list[SPLIT_COUNT].image
    # black = shard_list[SPLIT_COUNT].black
    total_story = shard_list[SPLIT_COUNT].story
    total_story = total_story.split('. ')
    curr_caption = shard_list[SPLIT_COUNT].caption
    
    story_level = ". ".join(total_story[:3 - SPLIT_COUNT + 1])
    SPLIT_COUNT -= 1
                
    cont = True
    while cont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                cont = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  
                    cont = False

        half_width = screen.get_width() // 2
        image_height = screen.get_height()
        draw_images(shard_list, screen, width, height)
        # black_image = pygame.transform.scale(black_image, (half_width//1.15, image_height//2.25))
        # image = pygame.transform.scale(image, (half_width//1.15, image_height//2.25))
        # screen.blit(image, (0, 200))
        # screen.blit(black_image,(0,200))
        #screen.blit(curr_caption,(half_width,0))
        
        text = pygame.font.SysFont('Arial', 20).render(curr_caption, True, (255,255,255))
        text_rect = text.get_rect(center=(650,250))
        screen.blit(text, text_rect)

        render_text(screen,story_level,(half_width,image_height//2),pygame.font.SysFont('Arial', 28),"white",half_width)
        # render_text(screen,curr_caption,(half_width,image_height),pygame.font.SysFont('Arial', 28),"white",half_width)
        pygame.display.update()

    return None


def change_screen_level_change(screen, width, height, shard_list):
    global SPLIT_COUNT
    screen = pygame.display.set_mode([width, height])
    image = shard_list[SPLIT_COUNT].image
    total_story = shard_list[SPLIT_COUNT].story
    total_story = total_story.split('. ')
    curr_caption = shard_list[SPLIT_COUNT].caption
    
    story_level = ". ".join(total_story[:3 - SPLIT_COUNT + 1])
    SPLIT_COUNT -= 1
                
    cont = True
    while cont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                cont = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  
                    cont = False

        half_width = screen.get_width() // 2
        image_height = screen.get_height()
        image = pygame.transform.scale(image, (half_width//1.15, image_height//2.25))
        screen.blit(image, (0, 200))
        # #screen.blit(curr_caption,(half_width,0))
        
        # text = pygame.font.SysFont('Arial', 20).render(curr_caption, True, (255,255,255))
        # text_rect = text.get_rect(center=(650,250))
        # screen.blit(text, text_rect)

        # render_text(screen,story_level,(half_width,image_height//2),pygame.font.SysFont('Arial', 28),"white",half_width)
        pygame.display.update()

    return None

# def change_screen_shard_collected(screen, width, height, shard_list):
#     global SPLIT_COUNT
#     screen = pygame.display.set_mode([width, height])
#     image = shard_list[SPLIT_COUNT].image
#     total_story = shard_list[SPLIT_COUNT].story
#     total_story = total_story.split('. ')
#     curr_caption = shard_list[SPLIT_COUNT].caption
#     story_level = total_story[:3 - SPLIT_COUNT + 1]
#     SPLIT_COUNT -= 1

#     font = pygame.font.Font('freesansbold.ttf', 20)
#     text_color = (255, 255, 255)  # White color

#     # Function to split the caption into multiple lines
#     def split_caption(caption, line_width):
#         words = caption.split(' ')
#         lines = []
#         current_line = ''
#         for word in words:
#             if font.size(current_line + word)[0] <= line_width:
#                 current_line += word + ' '
#             else:
#                 lines.append(current_line)
#                 current_line = word + ' '
#         lines.append(current_line)
#         return lines

#     caption_lines = split_caption(curr_caption, 880)  # Assuming 880 pixels wide text box

#     cont = True
#     while cont:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT: 
#                 cont = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_r:  
#                     cont = False

#         screen.blit(image, (0, 0))
#         pygame.draw.rect(screen, (255, 255, 255), (0, 0, 100, 50), 3)
#         text = font.render('Return', True, text_color)
#         screen.blit(text, (10, 10))

#         # Create text box for story
#         pygame.draw.rect(screen, (0, 0, 0), (0, 600, 900, 350))
#         pygame.draw.rect(screen, (255, 255, 255), (0, 600, 900, 350), 3)

#         # Display each line of the caption
#         line_height = font.get_height()
#         for i, line in enumerate(caption_lines.join("")):
#             text = font.render(line, True, text_color)
#             screen.blit(text, (10, 610 + i * line_height))

#         pygame.display.update()

#     return None


def run_game(root, tree_level, victory_tracker, board = None):
    WIDTH = 900
    HEIGHT = 950
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    timer = pygame.time.Clock()
    fps = 60
    font = pygame.font.Font('freesansbold.ttf', 20)
    level = test_board if board is None else board
    color = 'blue'
    PI = math.pi
    player_images = []
    for i in range(1, 5):
        player_images.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (45, 45)))
    blinky_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/red.png'), (45, 45))
    pinky_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/pink.png'), (45, 45))
    inky_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/blue.png'), (45, 45))
    clyde_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/orange.png'), (45, 45))
    spooked_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/powerup.png'), (45, 45))
    dead_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/dead.png'), (45, 45))
    player_x = 450
    player_y = 663
    direction = 0
    blinky_x = 56
    blinky_y = 58
    blinky_direction = 0
    inky_x = 440
    inky_y = 388
    inky_direction = 2
    pinky_x = 440
    pinky_y = 438
    pinky_direction = 2
    clyde_x = 440
    clyde_y = 438
    clyde_direction = 2
    counter = 0
    lost_level = False
    flicker = False
    # R, L, U, D
    turns_allowed = [False, False, False, False]
    direction_command = 0
    player_speed = 2
    score = [0]
    powerup = False
    power_counter = 0
    eaten_ghost = [False, False, False, False]
    targets = [(player_x, player_y), (player_x, player_y), (player_x, player_y), (player_x, player_y)]
    blinky_dead = False
    inky_dead = False
    clyde_dead = False
    pinky_dead = False
    blinky_box = False
    inky_box = False
    clyde_box = False
    pinky_box = False
    moving = False
    ghost_speeds = [2, 2, 2, 2]
    startup_counter = 0
    lives = 3
    game_over = False
    game_won = False
    caption = ''
    story = ''
    if tree_level == 0:
        caption = root.caption
        story = root.val
    elif tree_level == 1:
        pass
    elif tree_level == 2:
        pass
    img_pp = pygame.image.load("photo_piece.png").convert_alpha()
    img_pp = pygame.transform.scale(img_pp, (30,30))
    # img_ppb = pygame.image.load("A_black_image.png").convert_alpha()
    # img_ppb = pygame.transform.scale(img_ppb, (30,30))
    split_image(root.image, './images', 'testingShard') #root.image
    # split_image(root.black, './images', 'blackShard')
    #split_image(image_path, destination_path, name
    img_pp1 = pygame.image.load('./images/testingShard/top_left.jpg').convert_alpha()
    img_pp2 = pygame.image.load('./images/testingShard/top_right.jpg').convert_alpha()
    img_pp3 = pygame.image.load('./images/testingShard/bottom_left.jpg').convert_alpha()
    img_pp4 = pygame.image.load('./images/testingShard/bottom_right.jpg').convert_alpha()
    
    # img_ppb1 = pygame.image.load('./images/blackShard/top_left.jpg').convert_alpha()
    # img_ppb2 = pygame.image.load('./images/blackShard/top_right.jpg').convert_alpha()
    # img_ppb3 = pygame.image.load('./images/blackShard/bottom_left.jpg').convert_alpha()
    # img_ppb4 = pygame.image.load('./images/blackShard/top_left.jpg').convert_alpha()
    # shard_list = [img_pp1, img_pp2, img_pp3, img_pp4]

    # if level is not 0, traverse using victory_tracker to find correct image/story


    shard1 = Shard(sprite=None, image=img_pp1, split='left', caption=caption, story=story, black='')
    shard2 = Shard(sprite=None, image=img_pp2, split='right', caption=caption, story=story, black='')
    shard3 = Shard(sprite=None, image=img_pp3, split='up', caption=caption, story=story,black='')
    shard4 = Shard(sprite=None, image=img_pp4, split='down', caption=caption, story=story,black='')
    shard_list = [shard1, shard2, shard3, shard4]
    
    mute = False
    shards = [0]

    # Each Ghost's class, each ghost has its own movement, this can be changed to just one movement way

    class Ghost:
        def __init__(self, x_coord, y_coord, target, speed, img, direct, dead, box, id):
            self.x_pos = x_coord
            self.y_pos = y_coord
            self.center_x = self.x_pos + 22
            self.center_y = self.y_pos + 22
            self.target = target
            self.speed = speed
            self.img = img
            self.direction = direct
            self.dead = dead
            self.in_box = box
            self.id = id
            self.turns, self.in_box = self.check_collisions()
            self.rect = self.draw()

        def draw(self):
            if (not powerup and not self.dead) or (eaten_ghost[self.id] and powerup and not self.dead):
                screen.blit(self.img, (self.x_pos, self.y_pos))
            elif powerup and not self.dead and not eaten_ghost[self.id]:
                screen.blit(spooked_img, (self.x_pos, self.y_pos))
            else:
                screen.blit(dead_img, (self.x_pos, self.y_pos))
            ghost_rect = pygame.rect.Rect((self.center_x - 18, self.center_y - 18), (36, 36))
            return ghost_rect

        def check_collisions(self):
            # R, L, U, D
            num1 = ((HEIGHT - 50) // 32)
            num2 = (WIDTH // 30)
            num3 = 15
            self.turns = [False, False, False, False]
            if 0 < self.center_x // 30 < 29:
                if level[(self.center_y - num3) // num1][self.center_x // num2] == 9:
                    self.turns[2] = True
                if (level[self.center_y // num1][(self.center_x - num3) // num2] < 3 or level[self.center_y // num1][(self.center_x - num3) // num2] == 10 \
                        or ((level[self.center_y // num1][(self.center_x - num3) // num2] == 9) and (
                        self.in_box or self.dead))):
                    self.turns[1] = True
                if (level[self.center_y // num1][(self.center_x + num3) // num2] < 3 or level[self.center_y // num1][(self.center_x + num3) // num2] == 10 \
                        or ((level[self.center_y // num1][(self.center_x + num3) // num2] == 9 ) and (
                        self.in_box or self.dead))):
                    self.turns[0] = True
                if (level[(self.center_y + num3) // num1][self.center_x // num2] < 3 or level[(self.center_y + num3) // num1][self.center_x // num2] == 10\
                        or ((level[(self.center_y + num3) // num1][self.center_x // num2] == 9 ) and (
                        self.in_box or self.dead))):
                    self.turns[3] = True
                if (level[(self.center_y - num3) // num1][self.center_x // num2] < 3 or level[(self.center_y - num3) // num1][self.center_x // num2] == 10\
                        or ((level[(self.center_y - num3) // num1][self.center_x // num2] == 9 ) and (
                        self.in_box or self.dead))):
                    self.turns[2] = True

                if self.direction == 2 or self.direction == 3:
                    if 12 <= self.center_x % num2 <= 18:
                        if level[(self.center_y + num3) // num1][self.center_x // num2] < 3 or level[self.center_y // num1][(self.center_x - num3) // num2] == 10\
                                or ((level[self.center_y // num1][(self.center_x - num3) // num2] == 9 ) and (
                                self.in_box or self.dead)):
                            self.turns[3] = True
                        if level[(self.center_y - num3) // num1][self.center_x // num2] < 3 or level[self.center_y // num1][(self.center_x + num3) // num2] == 10\
                                or ((level[self.center_y // num1][(self.center_x + num3) // num2] == 9 ) and (
                                self.in_box or self.dead)):
                            self.turns[2] = True
                    if 12 <= self.center_y % num1 <= 18:
                        if level[self.center_y // num1][(self.center_x - num2) // num2] < 3 or level[(self.center_y + num3) // num1][self.center_x // num2] == 10\
                                or ((level[(self.center_y + num3) // num1][self.center_x // num2] == 9 ) and (
                                self.in_box or self.dead)):
                            self.turns[1] = True
                        if level[self.center_y // num1][(self.center_x + num2) // num2] < 3 or level[(self.center_y - num3) // num1][self.center_x // num2] == 10\
                                or ((level[(self.center_y - num3) // num1][self.center_x // num2] == 9 ) and (
                                self.in_box or self.dead)):
                            self.turns[0] = True

                if self.direction == 0 or self.direction == 1:
                    if 12 <= self.center_x % num2 <= 18:
                        if level[(self.center_y + num3) // num1][self.center_x // num2] < 3 or level[self.center_y // num1][(self.center_x - num3) // num2] == 10\
                                or ((level[self.center_y // num1][(self.center_x - num3) // num2] == 9 ) and (
                                self.in_box or self.dead)):
                            self.turns[3] = True
                        if level[(self.center_y - num3) // num1][self.center_x // num2] < 3 or level[self.center_y // num1][(self.center_x + num3) // num2] == 10\
                                or ((level[self.center_y // num1][(self.center_x + num3) // num2] == 9 ) and (
                                self.in_box or self.dead)):
                            self.turns[2] = True
                    if 12 <= self.center_y % num1 <= 18:
                        if level[self.center_y // num1][(self.center_x - num3) // num2] < 3 or level[(self.center_y + num3) // num1][self.center_x // num2] == 10\
                                or ((level[(self.center_y + num3) // num1][self.center_x // num2] == 9 ) and (
                                self.in_box or self.dead)):
                            self.turns[1] = True
                        if level[self.center_y // num1][(self.center_x + num3) // num2] < 3 or level[(self.center_y - num3) // num1][self.center_x // num2] == 10\
                                or ((level[(self.center_y - num3) // num1][self.center_x // num2] == 9 ) and (
                                self.in_box or self.dead)):
                            self.turns[0] = True
            else:
                self.turns[0] = True
                self.turns[1] = True
            if 350 < self.x_pos < 550 and 370 < self.y_pos < 480:
                self.in_box = True
            else:
                self.in_box = False
            return self.turns, self.in_box

        def move_clyde(self):
            # r, l, u, d
            # clyde is going to turn whenever advantageous for pursuit
            if self.direction == 0:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.x_pos += self.speed
                elif not self.turns[0]:
                    if self.target[1] > self.y_pos and self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.target[1] < self.y_pos and self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.target[0] < self.x_pos and self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    elif self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                elif self.turns[0]:
                    if self.target[1] > self.y_pos and self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    if self.target[1] < self.y_pos and self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    else:
                        self.x_pos += self.speed
            elif self.direction == 1:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.x_pos -= self.speed
                elif not self.turns[1]:
                    if self.target[1] > self.y_pos and self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.target[1] < self.y_pos and self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.target[0] > self.x_pos and self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                    elif self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                elif self.turns[1]:
                    if self.target[1] > self.y_pos and self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    if self.target[1] < self.y_pos and self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    else:
                        self.x_pos -= self.speed
            elif self.direction == 2:
                if self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif not self.turns[2]:
                    if self.target[0] > self.x_pos and self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                    elif self.target[0] < self.x_pos and self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    elif self.target[1] > self.y_pos and self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    elif self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                elif self.turns[2]:
                    if self.target[0] > self.x_pos and self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                    elif self.target[0] < self.x_pos and self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    else:
                        self.y_pos -= self.speed
            elif self.direction == 3:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.y_pos += self.speed
                elif not self.turns[3]:
                    if self.target[0] > self.x_pos and self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                    elif self.target[0] < self.x_pos and self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    elif self.target[1] < self.y_pos and self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    elif self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                elif self.turns[3]:
                    if self.target[0] > self.x_pos and self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                    elif self.target[0] < self.x_pos and self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    else:
                        self.y_pos += self.speed
            if self.x_pos < -30:
                self.x_pos = 900
            elif self.x_pos > 900:
                self.x_pos - 30
            return self.x_pos, self.y_pos, self.direction

        def move_blinky(self):
            # r, l, u, d
            # blinky is going to turn whenever colliding with walls, otherwise continue straight
            if self.direction == 0:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.x_pos += self.speed
                elif not self.turns[0]:
                    if self.target[1] > self.y_pos and self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.target[1] < self.y_pos and self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.target[0] < self.x_pos and self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    elif self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                elif self.turns[0]:
                    self.x_pos += self.speed
            elif self.direction == 1:
                if self.target[0] < self.x_pos and self.turns[1]:
                    self.x_pos -= self.speed
                elif not self.turns[1]:
                    if self.target[1] > self.y_pos and self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.target[1] < self.y_pos and self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.target[0] > self.x_pos and self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                    elif self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                elif self.turns[1]:
                    self.x_pos -= self.speed
            elif self.direction == 2:
                if self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif not self.turns[2]:
                    if self.target[0] > self.x_pos and self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                    elif self.target[0] < self.x_pos and self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    elif self.target[1] > self.y_pos and self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                    elif self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                elif self.turns[2]:
                    self.y_pos -= self.speed
            elif self.direction == 3:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.y_pos += self.speed
                elif not self.turns[3]:
                    if self.target[0] > self.x_pos and self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                    elif self.target[0] < self.x_pos and self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    elif self.target[1] < self.y_pos and self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                    elif self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                elif self.turns[3]:
                    self.y_pos += self.speed
            if self.x_pos < -30:
                self.x_pos = 900
            elif self.x_pos > 900:
                self.x_pos - 30
            return self.x_pos, self.y_pos, self.direction

        def move_inky(self):
            # r, l, u, d
            # inky turns up or down at any point to pursue, but left and right only on collision
            if self.direction == 0:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.x_pos += self.speed
                elif not self.turns[0]:
                    if self.target[1] > self.y_pos and self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.target[1] < self.y_pos and self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.target[0] < self.x_pos and self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    elif self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                elif self.turns[0]:
                    if self.target[1] > self.y_pos and self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    if self.target[1] < self.y_pos and self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    else:
                        self.x_pos += self.speed
            elif self.direction == 1:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.x_pos -= self.speed
                elif not self.turns[1]:
                    if self.target[1] > self.y_pos and self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.target[1] < self.y_pos and self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.target[0] > self.x_pos and self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                    elif self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                elif self.turns[1]:
                    if self.target[1] > self.y_pos and self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    if self.target[1] < self.y_pos and self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    else:
                        self.x_pos -= self.speed
            elif self.direction == 2:
                if self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif not self.turns[2]:
                    if self.target[0] > self.x_pos and self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                    elif self.target[0] < self.x_pos and self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    elif self.target[1] > self.y_pos and self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    elif self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                elif self.turns[2]:
                    self.y_pos -= self.speed
            elif self.direction == 3:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.y_pos += self.speed
                elif not self.turns[3]:
                    if self.target[0] > self.x_pos and self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                    elif self.target[0] < self.x_pos and self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    elif self.target[1] < self.y_pos and self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    elif self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                elif self.turns[3]:
                    self.y_pos += self.speed
            if self.x_pos < -30:
                self.x_pos = 900
            elif self.x_pos > 900:
                self.x_pos - 30
            return self.x_pos, self.y_pos, self.direction

        def move_pinky(self):
            # r, l, u, d
            # inky is going to turn left or right whenever advantageous, but only up or down on collision
            if self.direction == 0:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.x_pos += self.speed
                elif not self.turns[0]:
                    if self.target[1] > self.y_pos and self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.target[1] < self.y_pos and self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.target[0] < self.x_pos and self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    elif self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                elif self.turns[0]:
                    self.x_pos += self.speed
            elif self.direction == 1:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direction = 3
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.x_pos -= self.speed
                elif not self.turns[1]:
                    if self.target[1] > self.y_pos and self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.target[1] < self.y_pos and self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.target[0] > self.x_pos and self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                    elif self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                elif self.turns[1]:
                    self.x_pos -= self.speed
            elif self.direction == 2:
                if self.target[0] < self.x_pos and self.turns[1]:
                    self.direction = 1
                    self.x_pos -= self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direction = 2
                    self.y_pos -= self.speed
                elif not self.turns[2]:
                    if self.target[0] > self.x_pos and self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                    elif self.target[0] < self.x_pos and self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    elif self.target[1] > self.y_pos and self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    elif self.turns[3]:
                        self.direction = 3
                        self.y_pos += self.speed
                    elif self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                elif self.turns[2]:
                    if self.target[0] > self.x_pos and self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                    elif self.target[0] < self.x_pos and self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    else:
                        self.y_pos -= self.speed
            elif self.direction == 3:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.y_pos += self.speed
                elif not self.turns[3]:
                    if self.target[0] > self.x_pos and self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                    elif self.target[0] < self.x_pos and self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    elif self.target[1] < self.y_pos and self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.turns[2]:
                        self.direction = 2
                        self.y_pos -= self.speed
                    elif self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    elif self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                elif self.turns[3]:
                    if self.target[0] > self.x_pos and self.turns[0]:
                        self.direction = 0
                        self.x_pos += self.speed
                    elif self.target[0] < self.x_pos and self.turns[1]:
                        self.direction = 1
                        self.x_pos -= self.speed
                    else:
                        self.y_pos += self.speed
            if self.x_pos < -30:
                self.x_pos = 900
            elif self.x_pos > 900:
                self.x_pos - 30
            return self.x_pos, self.y_pos, self.direction

    # Drawing scores

    def draw_misc():
        nonlocal score
        nonlocal shards

        font = pygame.font.Font('freesansbold.ttf', 25)
        score_text = font.render(f'Score: {score[0]}', True, 'white')
        shards_text = font.render(f'Shards: {shards[0]} / 4', True, 'white')
        screen.blit(score_text, (WIDTH // 2.26, HEIGHT // 2.35))
        screen.blit(shards_text, (WIDTH // 2.4, HEIGHT // 2.15))

        if powerup:
            pygame.draw.circle(screen, 'blue', (140, 930), 15)
        for i in range(lives):
            screen.blit(pygame.transform.scale(player_images[0], (30, 30)), (650 + i * 40, 915))
        if game_over:
            pygame.draw.rect(screen, 'white', [50, 200, 800, 300],0, 10)
            pygame.draw.rect(screen, 'dark gray', [70, 220, 760, 260], 0, 10)
            gameover_text = font.render('Game over! Space bar to restart!', True, 'red')
            screen.blit(gameover_text, (100, 300))
        if game_won:
            pygame.draw.rect(screen, 'white', [50, 200, 800, 300],0, 10)
            pygame.draw.rect(screen, 'dark gray', [70, 220, 760, 260], 0, 10)
            gameover_text = font.render('Victory! Space bar to restart!', True, 'green')
            screen.blit(gameover_text, (100, 300))

    # Checking for collisions

    def check_collisions(scor, power, power_count, eaten_ghosts):
        nonlocal shards
        num1 = (HEIGHT - 50) // 32
        num2 = WIDTH // 30
        if 0 < player_x < 870:
            if level[center_y // num1][center_x // num2] == 1:
                level[center_y // num1][center_x // num2] = 0
                scor[0] += 10
            if level[center_y // num1][center_x // num2] == 2:
                level[center_y // num1][center_x // num2] = 0
                scor[0] += 50
                power = True
                power_count = 0
                eaten_ghosts = [False, False, False, False]
            if level[center_y // num1][center_x // num2] == 10:
                level[center_y // num1][center_x // num2] = 0
                shards[0] += 1
                change_screen_shard_collected(screen, WIDTH, HEIGHT, shard_list) 
        return scor, power, power_count, eaten_ghosts

    # Draw the board from board.py

    def draw_board():
        num1 = ((HEIGHT - 50) // 32)
        num2 = (WIDTH // 30)
        for i in range(len(level)):
            for j in range(len(level[i])):
                if level[i][j] == 1:
                    pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
                if level[i][j] == 2 and not flicker:
                    pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
                if level[i][j] == 3:
                    pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1),
                                    (j * num2 + (0.5 * num2), i * num1 + num1), 3)
                if level[i][j] == 4:
                    pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)),
                                    (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
                if level[i][j] == 5:
                    pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                    0, PI / 2, 3)
                if level[i][j] == 6:
                    pygame.draw.arc(screen, color,
                                    [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
                if level[i][j] == 7:
                    pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI,
                                    3 * PI / 2, 3)
                if level[i][j] == 8:
                    pygame.draw.arc(screen, color,
                                    [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * PI / 2,
                                    2 * PI, 3)
                if level[i][j] == 9:
                    pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                    (j * num2 + num2, i * num1 + (0.5 * num1)), 3)  
                if level[i][j] == 10:
                    # pygame.draw.circle(screen, 'aqua', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
                    screen.blit(img_pp, (j * num2, i * num1))


    def draw_player():
        # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
        if direction == 0:
            screen.blit(player_images[counter // 5], (player_x, player_y))
        elif direction == 1:
            screen.blit(pygame.transform.flip(player_images[counter // 5], True, False), (player_x, player_y))
        elif direction == 2:
            screen.blit(pygame.transform.rotate(player_images[counter // 5], 90), (player_x, player_y))
        elif direction == 3:
            screen.blit(pygame.transform.rotate(player_images[counter // 5], 270), (player_x, player_y))


    def check_position(centerx, centery):
        turns = [False, False, False, False]
        num1 = (HEIGHT - 50) // 32
        num2 = (WIDTH // 30)
        num3 = 15
        # check collisions based on center x and center y of player +/- fudge number
        if centerx // 30 < 29:
            if direction == 0:
                if level[centery // num1][(centerx - num3) // num2] < 3 or level[centery // num1][(centerx - num3) // num2] > 9:
                    turns[1] = True
            if direction == 1:
                if level[centery // num1][(centerx + num3) // num2] < 3 or level[centery // num1][(centerx + num3) // num2] > 9:
                    turns[0] = True
            if direction == 2:
                if level[(centery + num3) // num1][centerx // num2] < 3 or level[(centery + num3) // num1][centerx // num2] > 9:
                    turns[3] = True
            if direction == 3:
                if level[(centery - num3) // num1][centerx // num2] < 3 or level[(centery - num3) // num1][centerx // num2] > 9:
                    turns[2] = True

            if direction == 2 or direction == 3:
                if 12 <= centerx % num2 <= 18:
                    if level[(centery + num3) // num1][centerx // num2] < 3 or level[(centery + num3) // num1][centerx // num2] > 9:
                        turns[3] = True
                    if level[(centery - num3) // num1][centerx // num2] < 3 or level[(centery - num3) // num1][centerx // num2] > 9:
                        turns[2] = True
                if 12 <= centery % num1 <= 18:
                    if level[centery // num1][(centerx - num2) // num2] < 3 or level[centery // num1][(centerx - num2) // num2] > 9:
                        turns[1] = True
                    if level[centery // num1][(centerx + num2) // num2] < 3 or level[centery // num1][(centerx + num2) // num2] > 9:
                        turns[0] = True
            if direction == 0 or direction == 1:
                if 12 <= centerx % num2 <= 18:
                    if level[(centery + num1) // num1][centerx // num2] < 3 or level[(centery + num1) // num1][centerx // num2] > 9:
                        turns[3] = True
                    if level[(centery - num1) // num1][centerx // num2] < 3 or level[(centery - num1) // num1][centerx // num2] > 9:
                        turns[2] = True
                if 12 <= centery % num1 <= 18:
                    if level[centery // num1][(centerx - num3) // num2] < 3 or level[centery // num1][(centerx - num3) // num2] > 9:
                        turns[1] = True
                    if level[centery // num1][(centerx + num3) // num2] < 3 or level[centery // num1][(centerx + num3) // num2] > 9:
                        turns[0] = True
        else:
            turns[0] = True
            turns[1] = True

        return turns


    def move_player(play_x, play_y):
        # r, l, u, d
        if direction == 0 and turns_allowed[0]:
            play_x += player_speed
        elif direction == 1 and turns_allowed[1]:
            play_x -= player_speed
        if direction == 2 and turns_allowed[2]:
            play_y -= player_speed
        elif direction == 3 and turns_allowed[3]:
            play_y += player_speed
        return play_x, play_y


    def get_targets(blink_x, blink_y, ink_x, ink_y, pink_x, pink_y, clyd_x, clyd_y):
        if player_x < 450:
            runaway_x = 900
        else:
            runaway_x = 0
        if player_y < 450:
            runaway_y = 900
        else:
            runaway_y = 0
        return_target = (380, 400)
        if powerup:
            if not blinky.dead and not eaten_ghost[0]:
                blink_target = (runaway_x, runaway_y)
            elif not blinky.dead and eaten_ghost[0]:
                if 340 < blink_x < 560 and 340 < blink_y < 500:
                    blink_target = (400, 100)
                else:
                    blink_target = (player_x, player_y)
            else:
                blink_target = return_target
            if not inky.dead and not eaten_ghost[1]:
                ink_target = (runaway_x, player_y)
            elif not inky.dead and eaten_ghost[1]:
                if 340 < ink_x < 560 and 340 < ink_y < 500:
                    ink_target = (400, 100)
                else:
                    ink_target = (player_x, player_y)
            else:
                ink_target = return_target
            if not pinky.dead:
                pink_target = (player_x, runaway_y)
            elif not pinky.dead and eaten_ghost[2]:
                if 340 < pink_x < 560 and 340 < pink_y < 500:
                    pink_target = (400, 100)
                else:
                    pink_target = (player_x, player_y)
            else:
                pink_target = return_target
            if not clyde.dead and not eaten_ghost[3]:
                clyd_target = (450, 450)
            elif not clyde.dead and eaten_ghost[3]:
                if 340 < clyd_x < 560 and 340 < clyd_y < 500:
                    clyd_target = (400, 100)
                else:
                    clyd_target = (player_x, player_y)
            else:
                clyd_target = return_target
        else:
            if not blinky.dead:
                if 340 < blink_x < 560 and 340 < blink_y < 500:
                    blink_target = (400, 100)
                else:
                    blink_target = (player_x, player_y)
            else:
                blink_target = return_target
            if not inky.dead:
                if 340 < ink_x < 560 and 340 < ink_y < 500:
                    ink_target = (400, 100)
                else:
                    ink_target = (player_x, player_y)
            else:
                ink_target = return_target
            if not pinky.dead:
                if 340 < pink_x < 560 and 340 < pink_y < 500:
                    pink_target = (400, 100)
                else:
                    pink_target = (player_x, player_y)
            else:
                pink_target = return_target
            if not clyde.dead:
                if 340 < clyd_x < 560 and 340 < clyd_y < 500:
                    clyd_target = (400, 100)
                else:
                    clyd_target = (player_x, player_y)
            else:
                clyd_target = return_target
        return [blink_target, ink_target, pink_target, clyd_target]


    run = True
    delay_duration = 640
    last_play_time = 0 
    while run:
        
        pygame.mixer.init()
        sound = pygame.mixer.Sound('pacman_chomp.wav')
        
        current_time = pygame.time.get_ticks()
        if current_time - last_play_time >= delay_duration:
            if not mute:
                sound.play()
            last_play_time = current_time
        
        timer.tick(fps)
        if counter < 19:
            counter += 1
            if counter > 3:
                flicker = False
        else:
            counter = 0
            flicker = True
        if powerup and power_counter < 600:
            power_counter += 1
        elif powerup and power_counter >= 600:
            power_counter = 0
            powerup = False
            eaten_ghost = [False, False, False, False]
        if startup_counter < 180 and not game_over and not game_won:
            moving = False
            startup_counter += 1
        else:
            moving = True

        screen.fill('black')
        draw_board()
        center_x = player_x + 23
        center_y = player_y + 24
        if powerup:
            ghost_speeds = [1, 1, 1, 1]
        else:
            ghost_speeds = [2, 2, 2, 2]
        if eaten_ghost[0]:
            ghost_speeds[0] = 2
        if eaten_ghost[1]:
            ghost_speeds[1] = 2
        if eaten_ghost[2]:
            ghost_speeds[2] = 2
        if eaten_ghost[3]:
            ghost_speeds[3] = 2
        if blinky_dead:
            ghost_speeds[0] = 4
        if inky_dead:
            ghost_speeds[1] = 4
        if pinky_dead:
            ghost_speeds[2] = 4
        if clyde_dead:
            ghost_speeds[3] = 4

        game_won = True
        for i in range(len(level)):
            if 1 in level[i] or 2 in level[i]:
                game_won = False

        player_circle = pygame.draw.circle(screen, 'black', (center_x, center_y), 20, 2)
        draw_player()
        blinky = Ghost(blinky_x, blinky_y, targets[0], ghost_speeds[0], blinky_img, blinky_direction, blinky_dead,
                    blinky_box, 0)
        inky = Ghost(inky_x, inky_y, targets[1], ghost_speeds[1], inky_img, inky_direction, inky_dead,
                    inky_box, 1)
        pinky = Ghost(pinky_x, pinky_y, targets[2], ghost_speeds[2], pinky_img, pinky_direction, pinky_dead,
                    pinky_box, 2)
        clyde = Ghost(clyde_x, clyde_y, targets[3], ghost_speeds[3], clyde_img, clyde_direction, clyde_dead,
                    clyde_box, 3)
        draw_misc()
        targets = get_targets(blinky_x, blinky_y, inky_x, inky_y, pinky_x, pinky_y, clyde_x, clyde_y)

        turns_allowed = check_position(center_x, center_y)
        if moving:
            player_x, player_y = move_player(player_x, player_y)
            if not blinky_dead and not blinky.in_box:
                blinky_x, blinky_y, blinky_direction = blinky.move_blinky()
            else:
                blinky_x, blinky_y, blinky_direction = blinky.move_clyde()
            if not pinky_dead and not pinky.in_box:
                pinky_x, pinky_y, pinky_direction = pinky.move_pinky()
            else:
                pinky_x, pinky_y, pinky_direction = pinky.move_clyde()
            if not inky_dead and not inky.in_box:
                inky_x, inky_y, inky_direction = inky.move_inky()
            else:
                inky_x, inky_y, inky_direction = inky.move_clyde()
            clyde_x, clyde_y, clyde_direction = clyde.move_clyde()
        score, powerup, power_counter, eaten_ghost = check_collisions(score, powerup, power_counter, eaten_ghost)
        # add to if not powerup to check if eaten ghosts
        if not powerup:
            if (player_circle.colliderect(blinky.rect) and not blinky.dead) or \
                    (player_circle.colliderect(inky.rect) and not inky.dead) or \
                    (player_circle.colliderect(pinky.rect) and not pinky.dead) or \
                    (player_circle.colliderect(clyde.rect) and not clyde.dead):
                if lives > 0:
                    lives -= 1
                    startup_counter = 0
                    powerup = False
                    power_counter = 0
                    player_x = 450
                    player_y = 663
                    direction = 0
                    direction_command = 0
                    blinky_x = 56
                    blinky_y = 58
                    blinky_direction = 0
                    inky_x = 440
                    inky_y = 388
                    inky_direction = 2
                    pinky_x = 440
                    pinky_y = 438
                    pinky_direction = 2
                    clyde_x = 440
                    clyde_y = 438
                    clyde_direction = 2
                    eaten_ghost = [False, False, False, False]
                    blinky_dead = False
                    inky_dead = False
                    clyde_dead = False
                    pinky_dead = False
                else:
                    game_over = True
                    moving = False
                    startup_counter = 0
                    lost_level = True
                    break
        if powerup and player_circle.colliderect(blinky.rect) and eaten_ghost[0] and not blinky.dead:
            if lives > 0:
                powerup = False
                power_counter = 0
                lives -= 1
                startup_counter = 0
                player_x = 450
                player_y = 663
                direction = 0
                direction_command = 0
                blinky_x = 56
                blinky_y = 58
                blinky_direction = 0
                inky_x = 440
                inky_y = 388
                inky_direction = 2
                pinky_x = 440
                pinky_y = 438
                pinky_direction = 2
                clyde_x = 440
                clyde_y = 438
                clyde_direction = 2
                eaten_ghost = [False, False, False, False]
                blinky_dead = False
                inky_dead = False
                clyde_dead = False
                pinky_dead = False
            else:
                game_over = True
                moving = False
                startup_counter = 0
                change_screen_win_screen()
        if powerup and player_circle.colliderect(inky.rect) and eaten_ghost[1] and not inky.dead:
            if lives > 0:
                powerup = False
                power_counter = 0
                lives -= 1
                startup_counter = 0
                player_x = 450
                player_y = 663
                direction = 0
                direction_command = 0
                blinky_x = 56
                blinky_y = 58
                blinky_direction = 0
                inky_x = 440
                inky_y = 388
                inky_direction = 2
                pinky_x = 440
                pinky_y = 438
                pinky_direction = 2
                clyde_x = 440
                clyde_y = 438
                clyde_direction = 2
                eaten_ghost = [False, False, False, False]
                blinky_dead = False
                inky_dead = False
                clyde_dead = False
                pinky_dead = False
            else:
                game_over = True
                moving = False
                startup_counter = 0
        if powerup and player_circle.colliderect(pinky.rect) and eaten_ghost[2] and not pinky.dead:
            if lives > 0:
                powerup = False
                power_counter = 0
                lives -= 1
                startup_counter = 0
                player_x = 450
                player_y = 663
                direction = 0
                direction_command = 0
                blinky_x = 56
                blinky_y = 58
                blinky_direction = 0
                inky_x = 440
                inky_y = 388
                inky_direction = 2
                pinky_x = 440
                pinky_y = 438
                pinky_direction = 2
                clyde_x = 440
                clyde_y = 438
                clyde_direction = 2
                eaten_ghost = [False, False, False, False]
                blinky_dead = False
                inky_dead = False
                clyde_dead = False
                pinky_dead = False
            else:
                game_over = True
                moving = False
                startup_counter = 0
        if powerup and player_circle.colliderect(clyde.rect) and eaten_ghost[3] and not clyde.dead:
            if lives > 0:
                powerup = False
                power_counter = 0
                lives -= 1
                startup_counter = 0
                player_x = 450
                player_y = 663
                direction = 0
                direction_command = 0
                blinky_x = 56
                blinky_y = 58
                blinky_direction = 0
                inky_x = 440
                inky_y = 388
                inky_direction = 2
                pinky_x = 440
                pinky_y = 438
                pinky_direction = 2
                clyde_x = 440
                clyde_y = 438
                clyde_direction = 2
                eaten_ghost = [False, False, False, False]
                blinky_dead = False
                inky_dead = False
                clyde_dead = False
                pinky_dead = False
            else:
                game_over = True
                moving = False
                startup_counter = 0
        if powerup and player_circle.colliderect(blinky.rect) and not blinky.dead and not eaten_ghost[0]:
            blinky_dead = True
            eaten_ghost[0] = True
            score[0] += (2 ** eaten_ghost.count(True)) * 100
        if powerup and player_circle.colliderect(inky.rect) and not inky.dead and not eaten_ghost[1]:
            inky_dead = True
            eaten_ghost[1] = True
            score[0] += (2 ** eaten_ghost.count(True)) * 100
        if powerup and player_circle.colliderect(pinky.rect) and not pinky.dead and not eaten_ghost[2]:
            pinky_dead = True
            eaten_ghost[2] = True
            score[0] += (2 ** eaten_ghost.count(True)) * 100
        if powerup and player_circle.colliderect(clyde.rect) and not clyde.dead and not eaten_ghost[3]:
            clyde_dead = True
            eaten_ghost[3] = True
            score[0] += (2 ** eaten_ghost.count(True)) * 100

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction_command = 0
                if event.key == pygame.K_LEFT:
                    direction_command = 1
                if event.key == pygame.K_UP:
                    direction_command = 2
                if event.key == pygame.K_DOWN:
                    direction_command = 3
                if event.key == pygame.K_SPACE and (game_over or game_won):
                    powerup = False
                    power_counter = 0
                    lives -= 1
                    startup_counter = 0
                    player_x = 450
                    player_y = 663
                    direction = 0
                    direction_command = 0
                    blinky_x = 56
                    blinky_y = 58
                    blinky_direction = 0
                    inky_x = 440
                    inky_y = 388
                    inky_direction = 2
                    pinky_x = 440
                    pinky_y = 438
                    pinky_direction = 2
                    clyde_x = 440
                    clyde_y = 438
                    clyde_direction = 2
                    eaten_ghost = [False, False, False, False]
                    blinky_dead = False
                    inky_dead = False
                    clyde_dead = False
                    pinky_dead = False
                    score[0] = 0
                    lives = 3
                    level = copy.deepcopy(boards)
                    game_over = False
                    game_won = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT and direction_command == 0:
                    direction_command = direction
                if event.key == pygame.K_LEFT and direction_command == 1:
                    direction_command = direction
                if event.key == pygame.K_UP and direction_command == 2:
                    direction_command = direction
                if event.key == pygame.K_DOWN and direction_command == 3:
                    direction_command = direction
                if event.key == pygame.K_m:
                    mute = not mute
                
                if event.key == pygame.K_1:
                    shards[0] = 1
                if event.key == pygame.K_2:
                    shards[0] = 2
                if event.key == pygame.K_3:
                    shards[0] = 3
                if event.key == pygame.K_4:
                    shards[0] = 4
                if event.key == pygame.K_w:
                    # automatic win condition for demo and stuff
                    shards[0] = 4

        if direction_command == 0 and turns_allowed[0]:
            direction = 0
        if direction_command == 1 and turns_allowed[1]:
            direction = 1
        if direction_command == 2 and turns_allowed[2]:
            direction = 2
        if direction_command == 3 and turns_allowed[3]:
            direction = 3

        if player_x > 900:
            player_x = -47
        elif player_x < -50:
            player_x = 897

        if blinky.in_box and blinky_dead:
            blinky_dead = False
        if inky.in_box and inky_dead:
            inky_dead = False
        if pinky.in_box and pinky_dead:
            pinky_dead = False
        if clyde.in_box and clyde_dead:
            clyde_dead = False
            
        # Game end
        if shards[0] == 4:
            run = False

        pygame.display.flip()
    # pygame.quit()
        
    return not lost_level, shards[0]


if __name__ == '__main__':
    run_game()