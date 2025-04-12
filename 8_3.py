def remove_point(mouse_pos):
    for point in points:
        if ((point[0] - mouse_pos[0])**2 + (point[1] - mouse_pos[1])**2
        <= RADIUS**2):
            points.remove(point)
            break



import pygame
pygame.init()




size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("новая игра")
BACKGROUND = (0,0,0)
screen.fill(BACKGROUND)
COLORS = (192,192,192)
LINE_COLOR = (255,255,255)

points = []
RADIUS = 5


FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                points.append(event.pos)

            elif event.button == 3:
                remove_point(event.pos)


    screen.fill(BACKGROUND)

    for i in range(len(points)-1):
        start_points = points[i]
        end_points = points[i+1]
        pygame.draw.line(screen,LINE_COLOR,start_points,end_points,3)

    if len(points)>1:
        last_points = points[-1]
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.aaline(screen, COLORS,last_points,mouse_pos, 3)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
