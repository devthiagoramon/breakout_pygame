import pygame
import mechanics as mec
import constants as consts

paddle = pygame.Rect(consts.WINDOW_WIDTH // 2 - consts.PADDLE_WIDTH // 2,
                     consts.WINDOW_HEIGHT - consts.PADDLE_HEIGHT - 20, consts.PADDLE_WIDTH,
                     consts.PADDLE_HEIGHT)

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
    pygame.draw.rect(screen, pygame.Color('blue'), paddle)

    # controls

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= consts.PADDLE_SPEED
    if key[pygame.K_RIGHT] and paddle.right < consts.WINDOW_WIDTH:
        paddle.right += consts.PADDLE_SPEED

    # update screen

    pygame.display.flip()
    clock.tick(consts.FPS)
