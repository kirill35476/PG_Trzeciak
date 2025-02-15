from all_colors import *
import pygame
pygame.init()

size = (1200, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("новая игра")
BACKGROUND = (255,255,255)
screen.fill(BACKGROUND)

width,height= 100,100
x,y = 60,60
color = RED
speed = 5

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= speed
                if y <0:
                    y=0
                print(f'нажали клавишу вверх')
            elif event.key == pygame.K_DOWN:
                y += speed
                if y > 620:
                    y = 620
                print(f'нажали клавишу вниз')
            elif event.key == pygame.K_LEFT:
                x -= speed
                if x < 0:
                    x = 0
                print(f'нажали клавишу влево')
            elif event.key == pygame.K_RIGHT:
                x += speed
                if x > 1100:
                    x = 1100
                print(f'нажали клавишу вправо')
            else:
                print(f'нажали клавишу {event.key}')




    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, color, (x, y, width, height))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()