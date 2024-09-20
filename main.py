import pygame
import mechanics as mec
import constants as consts
from random import randrange as rand

from lpc2024.atividade004.breakout_pygame.mechanics import ball_dx, ball_hit_paddle

#paddle
paddle = pygame.Rect(consts.WINDOW_WIDTH // 2 - consts.PADDLE_WIDTH // 2,
                     consts.WINDOW_HEIGHT - consts.PADDLE_HEIGHT - 20, consts.PADDLE_WIDTH,
                     consts.PADDLE_HEIGHT)
#ball
ball_size = 10
ball = pygame.Rect(rand(ball_size, consts.WINDOW_WIDTH - ball_size),consts.WINDOW_HEIGHT//2,ball_size,ball_size)

#walls
left_wall = pygame.Rect(0,0,10,consts.WINDOW_HEIGHT)
right_wall  = pygame.Rect(consts.WINDOW_WIDTH-10,0,10,consts.WINDOW_HEIGHT)
upper_wall = pygame.Rect(0,0,consts.WINDOW_WIDTH,30)

pygame.init()
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
clock = pygame.time.Clock()
# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(consts.BLACK)

    # drawing the game
    pygame.draw.rect(screen, consts.BLUE, paddle)
    pygame.draw.rect(screen, consts.WHITE, ball)
    pygame.draw.rect(screen, consts.WHITE, left_wall)
    pygame.draw.rect(screen, consts.WHITE, right_wall)
    pygame.draw.rect(screen, consts.WHITE, upper_wall)

    #ball movement
    ball.x += consts.BALL_SPEED * mec.ball_dx
    ball.y += consts.BALL_SPEED * mec.ball_dy

    #ball collision with walls

    if ball.x > consts.WINDOW_WIDTH - 10:
        mec.ball_hit_wall()

    if ball.x < 10:
        mec.ball_hit_wall()

    if ball.colliderect(upper_wall):
        mec.ball_dy = -mec.ball_dy

    if ball.colliderect(paddle) and mec.ball_dy > 0:
        mec.ball_hit_paddle(paddle.x,ball.x)




    # controls

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= consts.PADDLE_SPEED
    if key[pygame.K_RIGHT] and paddle.right < consts.WINDOW_WIDTH:
        paddle.right += consts.PADDLE_SPEED

    # update screen

    pygame.display.flip()
    clock.tick(consts.FPS)
