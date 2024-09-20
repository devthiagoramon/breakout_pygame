import pygame
import mechanics as mec
import constants as consts
from random import randrange as rand

#paddle
paddle = pygame.Rect(consts.WINDOW_WIDTH // 2 - consts.PADDLE_WIDTH // 2,
                     consts.WINDOW_HEIGHT - consts.PADDLE_HEIGHT - 20, consts.PADDLE_WIDTH,
                     consts.PADDLE_HEIGHT)
#ball
ball_size = 10
ball = pygame.Rect(rand(ball_size, consts.WINDOW_WIDTH - ball_size),consts.WINDOW_HEIGHT//2,ball_size,ball_size)
ball_dx = -1
ball_dy = -1


pygame.init()
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
clock = pygame.time.Clock()
# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(consts.BLACK)

    # draw
    pygame.draw.rect(screen, consts.BLUE, paddle)
    pygame.draw.rect(screen, consts.WHITE, ball)

    # controls

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= consts.PADDLE_SPEED
    if key[pygame.K_RIGHT] and paddle.right < consts.WINDOW_WIDTH:
        paddle.right += consts.PADDLE_SPEED

    # update screen

    pygame.display.flip()
    clock.tick(consts.FPS)
