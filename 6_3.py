import pygame

pygame.init()

size = (1200, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("новая игра")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

RECTANGLE_COLOR = (255, 0, 0)
top_left = (0, 0)
size = (0, 0)
dragging = False
filled = False  # Флаг для отслеживания состояния заливки

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
            dragging = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Переключаем состояние заливки при нажатии пробела
                filled = not filled

    screen.fill(BACKGROUND)

    # Рисуем прямоугольник с заливкой или без в зависимости от состояния filled
    if filled:
        pygame.draw.rect(screen, RECTANGLE_COLOR, (top_left, size))  # Залитый прямоугольник
    else:
        pygame.draw.rect(screen, RECTANGLE_COLOR, (top_left, size), 1)  # Только контур

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()