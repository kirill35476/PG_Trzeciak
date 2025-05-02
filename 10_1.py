import pygame
import random
import os


pygame.init()


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
ROWS = 3
COLS = 3
MARGIN = 2
BACKGROUND = (0, 0, 0)
SELECT_COLOR = (0, 255, 0)
FONT_COLOR = (255, 255, 255)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Пазл-игра")
screen.fill(BACKGROUND)

try:
    font = pygame.font.Font(None, 36)
except:
    font = pygame.font.SysFont('arial', 36)

picture_folder = 'picture'
pictures = [f for f in os.listdir(picture_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

picture = random.choice(pictures)
image = pygame.image.load(os.path.join(picture_folder, picture))
image_width, image_height = image.get_size()
TILE_WIDTH = image_width // COLS
TILE_HEIGHT = image_height // ROWS

tiles = []
for i in range(ROWS):
    for j in range(COLS):
        rect = pygame.Rect(j * TILE_WIDTH, i * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
        tile = image.subsurface(rect)
        tiles.append(tile)

origin_tiles = tiles.copy()
random.shuffle(tiles)


selected = None
swaps = 0
completed = False


def draw_tiles():
    for i in range(len(tiles)):
        tile = tiles[i]
        row = i // ROWS
        col = i % COLS
        x = col * (TILE_WIDTH + MARGIN) + MARGIN
        y = row * (TILE_HEIGHT + MARGIN) + MARGIN
        screen.blit(tile, (x, y))
        if i == selected:
            pygame.draw.rect(screen, SELECT_COLOR, (x - 2, y - 2, TILE_WIDTH + 4, TILE_HEIGHT + 4), 3)


def is_puzzle_completed():
    return all(tile == origin_tiles[i] for i, tile in enumerate(tiles))


def draw_info():
    swaps_text = font.render(f"Ходы: {swaps}", True, FONT_COLOR)
    screen.blit(swaps_text, (20, SCREEN_HEIGHT - 50))
    if completed:
        complete_text = font.render("Пазл собран!", True, (0, 255, 0))
        text_rect = complete_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30))
        screen.blit(complete_text, text_rect)


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not completed:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            for i in range(len(tiles)):
                row = i // ROWS
                col = i % COLS
                x = col * (TILE_WIDTH + MARGIN) + MARGIN
                y = row * (TILE_HEIGHT + MARGIN) + MARGIN

                if x <= mouse_x <= x + TILE_WIDTH and y <= mouse_y <= y + TILE_HEIGHT:
                    if selected is not None and selected != i:
                        tiles[i], tiles[selected] = tiles[selected], tiles[i]
                        selected = None
                        swaps += 1
                        completed = is_puzzle_completed()
                    elif selected == i:
                        selected = None
                    else:
                        selected = i

    screen.fill(BACKGROUND)
    draw_tiles()
    draw_info()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()