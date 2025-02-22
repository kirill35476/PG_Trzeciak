import pygame
from all_colors import *
from random import *
pygame.init()

width_screen = 640
height_screen = 480
screen = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption("новая игра")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

width = 100
height = 75

COLORS = [BLACK, WHITE, RED, GREEN, YELLOW, CYAN, MAGENTA, GRAY,
          ORANGE, PINK, BROWN, PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, COLD]

rects = []

rects.append(pygame.Rect(0, 0, width, height))

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].topright = (width_screen, 0)

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].bottomleft = (0, height_screen)

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].bottomright = (width_screen, height_screen)

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].center = (width_screen//2, height_screen//2)


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for rect in rects:
        pygame.draw.rect(screen, choice(COLORS), rect)

    pygame.display.flip()
    clock.tick(5)

pygame.quit()
