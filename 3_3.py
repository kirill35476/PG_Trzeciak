import pygame
pygame.init()
from all_colors import *
import pygame.mixer
pygame.mixer.init()

pygame.mixer.music.load('resources/Hydrogen.mp3')

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

shot_sound = pygame.mixer.Sound('resources/shot.mp3')
explosion_sound = pygame.mixer.Sound('resources/explosion.mp3')
fail_sound = pygame.mixer.Sound('resources/fail.mp3')
win_sound = pygame.mixer.Sound('resources/win.mp3')

shot_sound.set_volume(0.6)
win_sound.set_volume(0.2)

size = (1200, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("новая игра")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
COLORS = [BLACK, WHITE, RED, GREEN, YELLOW, CYAN, MAGENTA, GRAY,
          ORANGE, PINK, BROWN, PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, COLD]

screen_rect = screen.get_rect()

ship = pygame.Rect(300, 200, 50, 100)
ship.right = screen_rect.right
ship.centery = screen_rect.centery

# Список для хранения всех снарядов
missiles = []

missile_speed_x = 3  # Скорость снаряда по горизонтали
ship_speed_y = 1  # Скорость движения корабля вверх и вниз
hp_ship = 10  # Начальное количество жизней корабля
ammo = 10  # Начальное количество снарядов

ship_alive = True

FPS = 60
clock = pygame.time.Clock()
running = True

# Шрифт для отображения текста
font = pygame.font.Font(None, 36)

def draw_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ammo > 0:
                # Проверяем, нет ли уже активных снарядов
                if not missiles:  # Если список снарядов пуст
                    # Создаем новый снаряд
                    new_missile = pygame.Rect(50, 50, 10, 10)
                    new_missile.left = screen_rect.left
                    new_missile.centery = screen_rect.centery
                    missiles.append(new_missile)  # Добавляем снаряд в список
                    ammo -= 1  # Уменьшаем количество снарядов
                    pygame.mixer.music.stop()
                    shot_sound.play()

    if ship_alive:
        ship.move_ip(0, ship_speed_y)
        if ship.top < screen_rect.top or ship.bottom > screen_rect.bottom:
            ship_speed_y = -ship_speed_y  # Меняем направление движения

    # Обновляем положение всех снарядов
    for missile in missiles[:]:  # Используем срез [:] для безопасного удаления элементов
        missile.move_ip(missile_speed_x, 0)

        # Если снаряд выходит за пределы экрана
        if not missile.colliderect(screen_rect):
            missiles.remove(missile)  # Удаляем снаряд из списка
            pygame.mixer.music.stop()
            fail_sound.play()

        # Если снаряд попадает в корабль
        if ship_alive and missile.colliderect(ship):
            missiles.remove(missile)  # Удаляем снаряд из списка
            hp_ship -= 1  # Уменьшаем количество жизней корабля
            if hp_ship <= 0:
                ship_alive = False
                background_color = GREEN
                explosion_sound.play()

    # Проверка условий завершения игры
    if hp_ship <= 0 or ammo <= 0:
        running = False

    # Отрисовка
    screen.fill(BACKGROUND)
    if ship_alive:
        pygame.draw.rect(screen, BLUE, ship)

    # Отрисовка всех снарядов
    for missile in missiles:
        pygame.draw.rect(screen, RED, missile)

    # Отображение жизней и снарядов
    draw_text(f"Жизни: {hp_ship}", 10, 10, BLACK)
    draw_text(f"Снаряды: {ammo}", screen_rect.width - 150, 10, BLACK)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()