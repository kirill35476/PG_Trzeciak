import pygame
import sys
import random

pygame.init()
from all_colors import *

# Инициализация звуков
bounce_sound = pygame.mixer.Sound('resources/otskok-myacha.mp3')  # Звук отскока
score_sound = pygame.mixer.Sound('resources/fail.mp3')  # Звук забития гола


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong - Макс. скорость: 30")
BACKGROUND = (255, 255, 255)
screen.fill(BLACK)

# Настройки игры
PADDLE_WIDTH = 25
PADDLE_HEIGHT = 100
PADDLE_SPEED = 10

BALL_SIZE = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
MAX_BALL_SPEED = 30
current_speed = 5  # Отображаемая скорость (целое число)

# Создание объектов
paddle1_rect = pygame.Rect(0, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2_rect = pygame.Rect(SCREEN_WIDTH - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH,
                           PADDLE_HEIGHT)
ball_rect = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Счет
score1 = 0
score2 = 0

# Шрифты
font = pygame.font.SysFont('Arial', 32)
speed_font = pygame.font.SysFont('Arial', 28)

FPS = 60
clock = pygame.time.Clock()
running = True
ai_mode = True
if len(sys.argv) > 1 and sys.argv[1] == '--human':
    ai_mode = False


def reset_ball():
    """Сбрасывает мяч в центр"""
    global BALL_SPEED_X, BALL_SPEED_Y, current_speed
    ball_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    BALL_SPEED_X = 5 if random.random() > 0.5 else -5
    BALL_SPEED_Y = 5 if random.random() > 0.5 else -5
    current_speed = 5


def increase_ball_speed():
    """Увеличивает скорость мяча на 1"""
    global BALL_SPEED_X, BALL_SPEED_Y, current_speed
    if current_speed < MAX_BALL_SPEED:
        current_speed += 1
        # Сохраняем направление движения
        ratio = abs(BALL_SPEED_Y / BALL_SPEED_X) if BALL_SPEED_X != 0 else 1
        BALL_SPEED_X = (current_speed / (1 + ratio ** 2) ** 0.5) * (1 if BALL_SPEED_X > 0 else -1)
        BALL_SPEED_Y = (current_speed * ratio / (1 + ratio ** 2) ** 0.5) * (1 if BALL_SPEED_Y > 0 else -1)
    if bounce_sound:
        bounce_sound.play()


def update_ai():
    """ИИ для управления второй ракеткой"""
    if ball_rect.x > SCREEN_HEIGHT // 2:
        if ball_rect.centery < paddle2_rect.centery:
            paddle2_rect.y -= PADDLE_SPEED
        elif ball_rect.centery > paddle2_rect.centery:
            paddle2_rect.y += PADDLE_SPEED

        if paddle2_rect.top < 0:
            paddle2_rect.top = 0
        if paddle2_rect.bottom > SCREEN_HEIGHT:
            paddle2_rect.bottom = SCREEN_HEIGHT
    else:
        paddle2_rect.centery += (SCREEN_HEIGHT // 2 - paddle2_rect.centery) / PADDLE_SPEED


# Основной игровой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление ракетками
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_rect.y -= PADDLE_SPEED
        if paddle1_rect.top <= 0:
            paddle1_rect.top = 0
    if keys[pygame.K_s]:
        paddle1_rect.y += PADDLE_SPEED
        if paddle1_rect.bottom >= SCREEN_HEIGHT:
            paddle1_rect.bottom = SCREEN_HEIGHT

    if not ai_mode:
        if keys[pygame.K_UP]:
            paddle2_rect.y -= PADDLE_SPEED
            if paddle2_rect.top <= 0:
                paddle2_rect.top = 0
        if keys[pygame.K_DOWN]:
            paddle2_rect.y += PADDLE_SPEED
            if paddle2_rect.bottom >= SCREEN_HEIGHT:
                paddle2_rect.bottom = SCREEN_HEIGHT
    else:
        update_ai()

    # Движение мяча
    ball_rect.x += BALL_SPEED_X
    ball_rect.y += BALL_SPEED_Y

    # Отскок от стен
    if ball_rect.top <= 0 or ball_rect.bottom >= SCREEN_HEIGHT:
        BALL_SPEED_Y *= -1



    # Отскок от ракеток
    if ball_rect.colliderect(paddle1_rect) or ball_rect.colliderect(paddle2_rect):
        BALL_SPEED_X *= -1
        increase_ball_speed()

    # Гол
    if ball_rect.left <= 0:
        score2 += 1
        if score_sound:
            score_sound.play()
        reset_ball()
    if ball_rect.right >= SCREEN_WIDTH:
        score1 += 1
        if score_sound:
            score_sound.play()
        reset_ball()

    # Отрисовка
    screen.fill(BLACK)

    # Ракетки и мяч
    pygame.draw.rect(screen, WHITE, paddle1_rect)
    pygame.draw.rect(screen, WHITE, paddle2_rect)
    pygame.draw.ellipse(screen, WHITE, ball_rect)

    # Разделительная линия
    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), 1)

    # Счет
    score_text = font.render(f'{score1} : {score2}', True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 10))

    # Скорость (целое число)
    speed_text = speed_font.render(f"Скорость: {current_speed}/{MAX_BALL_SPEED}", True, WHITE)
    screen.blit(speed_text, (SCREEN_WIDTH - speed_text.get_width() - 20, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

#python.exe 5_1.py
#python.exe 5_1.py  --human
#добавить звуки при отскоке от рокетки скорость +и текст очки макс скорость 30 и 