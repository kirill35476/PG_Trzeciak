from all_colors import *
from pygame.constants import *
from random import *
import pygame
pygame.init()

size = (1200, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("новая игра")
BACKGROUND = (255,255,255)
screen.fill(BACKGROUND)

x =0
y =0
rect_size =  200
COLORS = [BLACK, WHITE, RED, GREEN, YELLOW, CYAN, MAGENTA, GRAY,
          ORANGE, PINK, BROWN, PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, COLD]

# rect1 = pygame.Rect(x,y,rect_size,rect_size)
# rect1.center = (screen.get_width()//2, screen.get_height()//2)
# pygame.draw.rect(screen,BLACK,rect1)
# rect2 = pygame.Rect(x,y,rect_size//2,rect_size//2)
# rect2.center = (screen.get_width()//2, screen.get_height()//2)
# pygame.draw.rect(screen,RED,rect2)

for i in range(3):
    rect = pygame.Rect(x,y,rect_size,rect_size)
    rect.center = (screen.get_width()//2, screen.get_height()//2)
    pygame.draw.rect(screen, choice(colors),rect)

    x += rect_size
    if x > screen.get_width():
        x = 0
        y += rect_size
        if y > screen.get_height():
            y = 0

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False








    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()