from pygame.constants import *
import pygame
pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("новая игра")
BACKGROUND = (255,255,255)
screen.fill(BACKGROUND)
RED = (255,0,0)


speed = 5
move = {K_LEFT:(-speed,0),
        K_RIGHT:(speed,0),
        K_UP:(0,-speed),
        K_DOWN:(0,speed)}

player = pygame.Rect(0,0,100,40)
player.midleft = (0,size[1]//2)

enemy = pygame.Rect(0,0,100,40)
enemy.midleft = (size[0]-100,size[1]//2)

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    old_pos = player.topleft
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    for key in move:
        if keys[key]:
            v = move[key]
            player.move_ip(v)

    if player.colliderect(enemy):
        player.topleft = old_pos

    screen.fill(BACKGROUND)
    pygame.draw.rect(screen,RED,player)
    pygame.draw.rect(screen,RED,enemy)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
