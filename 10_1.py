import pygame
import random
import os


def draw_tiles():
    for i in range(len(tiles)):
        tile = tiles[i]
        row = i // ROWS
        col = i % COLS
        x = col * (TILE_WIDTH  + MARGIN)+MARGIN
        y = row * (TITLE_HEIGHT +  MARGIN)+MARGIN

        screen.blit(tile,(x,y))


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
ROWS = 3
COLS = 3
MARGIN = 2


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("новая игра")
BACKGROUND = (255,255,255)
screen.fill(BACKGROUND)

picture = os.listdir('picture')
picture = random.choice(picture)
image = pygame.image.load('picture/'+ picture)


image_width, image_height = image.get_size()
TILE_WIDTH = image_width // COLS
TITLE_HEIGHT = image_height // ROWS


tiles = []
for i in range(ROWS):
    for j in range(COLS):
        rect = pygame.Rect(j * TILE_WIDTH,
                           i * TITLE_HEIGHT,
                           TILE_WIDTH,
                           TITLE_HEIGHT)
        tile = image.subsurface(rect)
        tiles.append(tile)


origin_tiles = tiles.copy()

random.shuffle(tiles)

selected = None

swaps = 0

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            for i in range(len(tiles)):
                row = i // ROWS
                col = i % COLS
                x = col * (TILE_WIDTH + MARGIN) + MARGIN
                y = row * (TITLE_HEIGHT + MARGIN) + MARGIN


                if x  <= mouse_x <= x + TILE_WIDTH and y < mouse_y <=y + TITLE_HEIGHT:
                    if selected is not None and selected != i:
                        tiles[i] ,tiles[selected] = tiles[selected], tiles[i]
                        selected = None
                        swaps +=1
                    elif selected == i:
                        selected = None
                    else:
                        selected = i


    screen.fill((0,0,0))
    draw_tiles()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
#