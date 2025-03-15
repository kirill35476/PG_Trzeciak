import pygame
pygame.init()

size = (1200, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("новая игра")
BACKGROUND = (255,255,0)
screen.fill(BACKGROUND)

my_font = pygame.font.SysFont('Arial',32)
my_text = my_font.render('Потрачено!',True,(0,0,0),(BACKGROUND))
screen.blit(my_text,(100,100))



FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #screen.fill(BACKGROUND)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()