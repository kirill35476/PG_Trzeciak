import pygame
from random import choice
from pygame.time import Clock
from all_colors import *

pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("новая игра")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)


COLORS = [BLACK, WHITE, RED, GREEN, YELLOW, CYAN, MAGENTA, GRAY,
          ORANGE, PINK, BROWN, PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, COLD]


initial_size = 200

running = True
clock = Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    size = initial_size
    for i in range(18):
        rect = pygame.Rect(0, 0, size, size)
        rect.center = (screen_width // 2, screen_height // 2)
        pygame.draw.rect(screen, choice(COLORS), rect)
        size -= 15

    pygame.display.flip()

    clock.tick(5)

pygame.quit()
