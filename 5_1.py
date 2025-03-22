import pygame
import sys
pygame.init()
from all_colors import *

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH ,SCREEN_HEIGHT))
pygame.display.set_caption("новая игра")
BACKGROUND = (255,255,255)
screen.fill(BLACK)

COLORS = [BLACK, WHITE, RED, GREEN, YELLOW, CYAN, MAGENTA, GRAY,
          ORANGE, PINK, BROWN, PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, COLD]

PADDLE_WIDTH = 25
PADDLE_HEIGHT = 100
PADDLE_SPEED = 10

BALL_SIZE = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

paddle1_rect = pygame.Rect(0,SCREEN_HEIGHT//2 - PADDLE_HEIGHT //2,
                          PADDLE_WIDTH,PADDLE_HEIGHT)

paddle2_rect = pygame.Rect(SCREEN_WIDTH - PADDLE_WIDTH,
                           SCREEN_HEIGHT//2 - PADDLE_HEIGHT //2,
                           PADDLE_WIDTH,PADDLE_HEIGHT)

ball_rect = pygame.Rect(SCREEN_WIDTH//2 - BALL_SIZE //2,
                        SCREEN_HEIGHT//2 - BALL_SIZE //2,
                        BALL_SIZE,BALL_SIZE)

score1 =0
score2 =0

font = pygame.font.SysFont(None,32)

FPS = 60
clock = pygame.time.Clock()
running = True
ai_mode = True
if len(sys.argv) >1:
    if sys.argv[1] == '--human':
        ai_mode = False

def update_ai():
    if ball_rect.x > SCREEN_HEIGHT//2:
        if ball_rect.centery < paddle2_rect.centery:
            paddle2_rect.y -= PADDLE_SPEED
        elif ball_rect.centery > paddle2_rect.centery:
            paddle2_rect.y += PADDLE_SPEED

        if paddle2_rect.top <0:
            paddle2_rect.top = 0
        if paddle2_rect.bottom > SCREEN_HEIGHT:
            paddle2_rect.bottom = SCREEN_HEIGHT

    else:
        paddle2_rect.centery +=(SCREEN_HEIGHT//2 - paddle2_rect.centery)/PADDLE_SPEED

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_rect.y -= PADDLE_SPEED
        if paddle1_rect.top <= 0:
            paddle1_rect.top = 0
    if keys[pygame.K_s]:
        paddle1_rect.y += PADDLE_SPEED
        if paddle1_rect.bottom >= 720:
            paddle1_rect.bottom = 720


    if keys[pygame.K_UP]:
        paddle2_rect.y -= PADDLE_SPEED
        if paddle2_rect.top <= 0:
            paddle2_rect.top = 0
    if keys[pygame.K_DOWN]:
        paddle2_rect.y += PADDLE_SPEED
        if paddle2_rect.bottom >= 720:
            paddle2_rect.bottom = 720

    if ai_mode:
        update_ai()

    ball_rect.x += BALL_SPEED_X
    ball_rect.y += BALL_SPEED_Y

    if ball_rect.top <= 0 or ball_rect.bottom >= SCREEN_HEIGHT:
        BALL_SPEED_Y *=-1


    if ball_rect.colliderect(paddle1_rect) or ball_rect.colliderect(paddle2_rect):
        BALL_SPEED_X *=-1

    if ball_rect.left <= 0:
        ball_rect = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2,
                                SCREEN_HEIGHT // 2 - BALL_SIZE // 2,
                                BALL_SIZE, BALL_SIZE)
    if ball_rect.right >= 1200:
        ball_rect = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2,
                                SCREEN_HEIGHT // 2 - BALL_SIZE // 2,
                                BALL_SIZE, BALL_SIZE)

    screen.fill(BLACK)

    pygame.draw.rect(screen,WHITE,paddle1_rect)
    pygame.draw.rect(screen, WHITE, paddle2_rect)
    pygame.draw.ellipse(screen, WHITE, ball_rect)

    pygame.draw.line(screen,WHITE,(SCREEN_WIDTH // 2,0),
                     (SCREEN_WIDTH // 2,SCREEN_HEIGHT))

    score_text = font.render(f'{score1} : {score2}',True,WHITE)
    screen.blit(score_text,
                (SCREEN_WIDTH //2 - score_text.get_width()//2,10))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
#python.exe 5_1.py
#python.exe 5_1.py  --human
#добавить звуки при отскоке от рокетки скорость +и текст очки макс скорость 30 и 