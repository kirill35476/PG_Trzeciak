import pygame
from all_colors import *
from random import choice
pygame.init()

size = (1200, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("новая игра")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

COLORS = [BLACK, WHITE, RED, GREEN, YELLOW, CYAN, MAGENTA, GRAY,
          ORANGE, PINK, BROWN, PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, COLD]

rectangles =[]

RECTANGLE_COLOR = (255, 0, 0)
top_left = (0, 0)
size = (0, 0)
dragging = False

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            top_left = event.pos
            size = 0, 0
            dragging = True

        elif event.type == pygame.MOUSEMOTION and dragging:
            right_bottom = event.pos
            size = (right_bottom[0] - top_left[0],
                    right_bottom[1] - top_left[1])

        elif event.type == pygame.MOUSEBUTTONUP:
            right_bottom = event.pos
            size = (right_bottom[0] - top_left[0],
                    right_bottom[1] - top_left[1])
            rect = pygame.Rect(top_left,size)
            color = choice(COLORS)
            rectangles.append((rect,color))
            dragging = False


    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, RECTANGLE_COLOR, (top_left, size), 1)
    for rectangle,color in rectangles:
        pygame.draw.rect(screen, color,rectangle,1)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()