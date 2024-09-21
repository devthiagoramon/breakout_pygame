import pygame
import mechanics as mec
import constants as consts
from random import randrange as rand

from mechanics import ball_dx, ball_hit_paddle

pygame.init()

# variables
level = 1
points = 0
lifes = 4
bricks_destroyed = 0
start_game = False

# paddle
paddle = pygame.Rect(consts.WINDOW_WIDTH // 2 - consts.PADDLE_WIDTH // 2,
                     consts.WINDOW_HEIGHT - consts.PADDLE_HEIGHT - 20, consts.PADDLE_WIDTH,
                     consts.PADDLE_HEIGHT)
# ball
ball_size = 10
ball = pygame.Rect(rand(ball_size, consts.WINDOW_WIDTH - ball_size), consts.WINDOW_HEIGHT // 2, ball_size, ball_size)
ball_is_ghost = False

# walls
left_wall = pygame.Rect(0, 0, 10, consts.WINDOW_HEIGHT)
right_wall = pygame.Rect(consts.WINDOW_WIDTH - 10, 0, 10, consts.WINDOW_HEIGHT)
upper_wall = pygame.Rect(0, 0, consts.WINDOW_WIDTH, 30)
left_blue_block = pygame.Rect(0, consts.WINDOW_HEIGHT - consts.PADDLE_HEIGHT - 20, 10, consts.PADDLE_HEIGHT)
right_blue_block = pygame.Rect(consts.WINDOW_WIDTH - 10, consts.WINDOW_HEIGHT - consts.PADDLE_HEIGHT - 20, 10,
                               consts.PADDLE_HEIGHT)

# defining font
font = pygame.font.Font("assets/fonts/breakout.ttf", 72)

# texts
level_text = font.render(str(level), True, consts.WHITE)
level_rect = level_text.get_rect().move(20, 30)

lifes_text = font.render(str(lifes), True, consts.WHITE)
lifes_rect = lifes_text.get_rect().move(consts.WINDOW_WIDTH // 2 + 40, 30)

points_text = font.render(str(points), True, consts.WHITE)
points_rect = points_text.get_rect().move(consts.WINDOW_WIDTH // 2 + 40, 110)

# soundeffects
pygame.mixer.init()
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
clock = pygame.time.Clock()

# generating bricks
bricks_red = []
bricks_orange = []
bricks_green = []
bricks_yellow = []
y_brick = 185


def generate_bricks(array_brick, color, point):
    global y_brick
    for i in range(consts.BRICK_ROWS):
        x_brick = 5
        array_brick.append([])
        for j in range(consts.BRICK_COLS):
            array_brick[i].append(
                {'rect': pygame.Rect(x_brick, y_brick, consts.BRICK_WIDTH, consts.BRICK_HEIGHT), 'visible': True,
                 'color': color, 'point': point})
            x_brick += consts.BRICK_WIDTH + consts.BRICK_SPACING
        y_brick += consts.BRICK_HEIGHT + consts.BRICK_SPACING


generate_bricks(bricks_red, consts.RED, 7)
generate_bricks(bricks_orange, consts.ORANGE, 5)
generate_bricks(bricks_green, consts.GREEN, 3)
generate_bricks(bricks_yellow, consts.YELLOW, 1)


def draw_bricks(array_bricks):
    global ball_is_ghost, points, points_text, bricks_destroyed
    for i in range(len(array_bricks)):
        left_color_in_wall = pygame.rect.Rect(0, array_bricks[i][0]["rect"].y - 5, 10,
                                              consts.BRICK_HEIGHT * len(array_bricks) + consts.BRICK_SPACING)
        rigth_color_in_wall = pygame.rect.Rect(consts.WINDOW_WIDTH - 10, array_bricks[i][0]["rect"].y - 5, 10,
                                               consts.BRICK_HEIGHT * len(array_bricks))
        pygame.draw.rect(screen, array_bricks[0][0]["color"], left_color_in_wall)
        pygame.draw.rect(screen, array_bricks[0][0]["color"], rigth_color_in_wall)
        for j in range(len(array_bricks[i])):
            if ball.colliderect(array_bricks[i][j]["rect"]) and array_bricks[i][j]["visible"] and not ball_is_ghost:
                array_bricks[i][j]["visible"] = False
                mec.ball_hit_block()
                ball_is_ghost = True
                points += array_bricks[i][j]["point"]
                points_text = font.render(str(points), True, consts.WHITE)
                bricks_destroyed += 1
            if array_bricks[i][j]["visible"]:
                pygame.draw.rect(screen, array_bricks[i][j]["color"], array_bricks[i][j]["rect"])


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
    pygame.draw.rect(screen, consts.BLUE, left_blue_block)
    pygame.draw.rect(screen, consts.BLUE, right_blue_block)

    # ball movement
    ball.x += consts.BALL_SPEED * mec.ball_dx
    ball.y += consts.BALL_SPEED * mec.ball_dy

    # ball collision with walls

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
        mec.ball_hit_paddle(paddle.x, ball.x)
        if ball_is_ghost:
            ball_is_ghost = False
        pygame.mixer.music.load(consts.BALL_HIT_PADDLE)
        pygame.mixer.music.play()

    if ball.y > consts.WINDOW_HEIGHT:
        ball = pygame.Rect(rand(ball_size, consts.WINDOW_WIDTH - ball_size), consts.WINDOW_HEIGHT // 2, ball_size,
                           ball_size)
        lifes -= 1
        lifes_text = font.render(str(lifes), True, consts.WHITE)

    # controls
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= consts.PADDLE_SPEED
    if key[pygame.K_RIGHT] and paddle.right < consts.WINDOW_WIDTH:
        paddle.right += consts.PADDLE_SPEED

    # Blocos

    # RED
    draw_bricks(bricks_red)
    # ORANGE
    draw_bricks(bricks_orange)
    # GREEN
    draw_bricks(bricks_green)
    # YELLOW
    draw_bricks(bricks_yellow)

    if 28 <= bricks_destroyed < 56 and level < 2:
        level = 2
        level_text = font.render(str(level), True, consts.WHITE)
    elif 56 <= bricks_destroyed < 84 and level < 3:
        level = 3
        level_text = font.render(str(level), True, consts.WHITE)
    elif 84 <= bricks_destroyed < 112 and level < 4:
        level = 4
        level_text = font.render(str(level), True, consts.WHITE)
    elif bricks_destroyed >= 112:
        # Game over
        pass

    # Texts
    screen.blit(level_text, level_rect)
    screen.blit(points_text, points_rect)
    screen.blit(lifes_text, lifes_rect)

    # update screen
    pygame.display.flip()
    clock.tick(consts.FPS)
