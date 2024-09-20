import pygame
import mechanics as mec
import constants as consts
from random import randrange as rand

from mechanics import ball_dx, ball_hit_paddle

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
left_red_block = pygame.Rect(0,50,10,40)
right_red_block = pygame.Rect(consts.WINDOW_WIDTH-10,50,10,40)
left_orange_block = pygame.Rect(0,95,10,40)
right_orange_block = pygame.Rect(consts.WINDOW_WIDTH-10,95,10,40)
left_green_block = pygame.Rect(0,140,10,40)
right_green_block = pygame.Rect(consts.WINDOW_WIDTH-10,140,10,40)
left_yellow_block = pygame.Rect(0,185,10,40)
right_yellow_block = pygame.Rect(consts.WINDOW_WIDTH-10,185,10,40)
left_blue_block= pygame.Rect(0,consts.WINDOW_HEIGHT - consts.PADDLE_HEIGHT - 20,10,consts.PADDLE_HEIGHT)
right_blue_block = pygame.Rect(consts.WINDOW_WIDTH-10,consts.WINDOW_HEIGHT - consts.PADDLE_HEIGHT - 20,10,consts.PADDLE_HEIGHT)

pygame.init()

#soundeffects
pygame.mixer.init()


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
    pygame.draw.rect(screen, consts.RED, left_red_block)
    pygame.draw.rect(screen, consts.RED, right_red_block)
    pygame.draw.rect(screen, consts.ORANGE, left_orange_block)
    pygame.draw.rect(screen, consts.ORANGE, right_orange_block)
    pygame.draw.rect(screen ,consts.GREEN, left_green_block)
    pygame.draw.rect(screen, consts.GREEN, right_green_block)
    pygame.draw.rect(screen, consts.YELLOW,left_yellow_block)
    pygame.draw.rect(screen, consts.YELLOW, right_yellow_block)
    pygame.draw.rect(screen, consts.BLUE, left_blue_block)
    pygame.draw.rect(screen, consts.BLUE, right_blue_block)


    #ball movement
    ball.x += consts.BALL_SPEED * mec.ball_dx
    ball.y += consts.BALL_SPEED * mec.ball_dy

    #ball collision with walls

    if ball.x > consts.WINDOW_WIDTH - 10:
        mec.ball_hit_wall()
        pygame.mixer.music.load(consts.BALL_HIT_WALL)
        pygame.mixer.music.play()

    if ball.x < 10:
        mec.ball_hit_wall()
        pygame.mixer.music.load(consts.BALL_HIT_WALL)
        pygame.mixer.music.play()

    if ball.colliderect(upper_wall):
        mec.ball_dy = -mec.ball_dy
        pygame.mixer.music.load(consts.BALL_HIT_WALL)
        pygame.mixer.music.play()

    if ball.colliderect(paddle) and mec.ball_dy > 0:
        mec.ball_hit_paddle(paddle.x,ball.x)
        pygame.mixer.music.load(consts.BALL_HIT_PADDLE)
        pygame.mixer.music.play()

    if ball.y > consts.WINDOW_HEIGHT:
        ball = pygame.Rect(rand(ball_size, consts.WINDOW_WIDTH - ball_size), consts.WINDOW_HEIGHT // 2, ball_size,
                           ball_size)

    # controls

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= consts.PADDLE_SPEED
    if key[pygame.K_RIGHT] and paddle.right < consts.WINDOW_WIDTH:
        paddle.right += consts.PADDLE_SPEED

    # Blocos

    #Red
    desenho_posicao_x = 5
    desenho_posicao_y = 50
    for i in range(1,17):
        pygame.draw.rect(screen, (consts.RED), (desenho_posicao_x, desenho_posicao_y, 50, 14))
        pygame.draw.rect(screen, (consts.RED), (desenho_posicao_x, desenho_posicao_y + 24, 50, 14))
        desenho_posicao_x += 55
    #Orange
    desenho_posicao_x = 5
    desenho_posicao_y = 96
    for i in range(1, 17):
        pygame.draw.rect(screen, (consts.ORANGE), (desenho_posicao_x, desenho_posicao_y, 50, 15))
        pygame.draw.rect(screen, (consts.ORANGE), (desenho_posicao_x, desenho_posicao_y + 23, 50, 15))
        desenho_posicao_x += 55
    #Green
    desenho_posicao_x = 5
    desenho_posicao_y = 140
    for i in range(1, 17):
        pygame.draw.rect(screen, (consts.GREEN), (desenho_posicao_x, desenho_posicao_y, 50, 15))
        pygame.draw.rect(screen, (consts.GREEN), (desenho_posicao_x, desenho_posicao_y + 23, 50, 15))
        desenho_posicao_x += 55
    #Yellow
    desenho_posicao_x = 5
    desenho_posicao_y = 186
    for i in range(1, 17):
        pygame.draw.rect(screen, (consts.YELLOW), (desenho_posicao_x, desenho_posicao_y, 50, 15))
        pygame.draw.rect(screen, (consts.YELLOW), (desenho_posicao_x, desenho_posicao_y + 24, 50, 15))
        desenho_posicao_x += 55


    # update screen

    pygame.display.flip()
    clock.tick(consts.FPS)
