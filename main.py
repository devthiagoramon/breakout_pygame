import time

import pygame
import mechanics as mec
import constants as consts
from random import randrange as rand
from random import uniform as randun

#affffff


from lpc2024.atividade004.breakout_pygame.mechanics import increase_speed_based_on_block
from mechanics import ball_dx, ball_hit_paddle

pygame.init()

# variables
level = 1
points = 0
lifes = 4
bricks_destroyed = 0
game_idle = True
show_level_completed = False
show_game_over = False

initial_paddle_rect = pygame.Rect(0,
                                  consts.WINDOW_HEIGHT - consts.PADDLE_HEIGHT - 20, consts.WINDOW_WIDTH,
                                  consts.PADDLE_HEIGHT)

# paddle
paddle = initial_paddle_rect

# ball
ball_size = 10
ball = pygame.Rect(rand(ball_size, consts.WINDOW_WIDTH - ball_size), consts.WINDOW_HEIGHT // 2, ball_size, ball_size)

# walls
left_wall = pygame.Rect(0, 0, 10, consts.WINDOW_HEIGHT)
right_wall = pygame.Rect(consts.WINDOW_WIDTH - 10, 0, 10, consts.WINDOW_HEIGHT)
upper_wall = pygame.Rect(0, 0, consts.WINDOW_WIDTH, 30)
left_blue_block = pygame.Rect(0, consts.WINDOW_HEIGHT - consts.PADDLE_HEIGHT - 20, 10, consts.PADDLE_HEIGHT)
right_blue_block = pygame.Rect(consts.WINDOW_WIDTH - 10, consts.WINDOW_HEIGHT - consts.PADDLE_HEIGHT - 20, 10,
                               consts.PADDLE_HEIGHT)

# defining font
font = pygame.font.Font("assets/fonts/breakout.ttf", 72)
font_60 = pygame.font.Font("assets/fonts/breakout.ttf", 60)
font_40 = pygame.font.Font("assets/fonts/breakout.ttf", 40)

# texts
level_text = font.render(str(level), True, consts.WHITE)
level_rect = level_text.get_rect().move(20, 30)

lifes_text = font.render(str(lifes), True, consts.WHITE)
lifes_rect = lifes_text.get_rect().move(consts.WINDOW_WIDTH // 2 + 40, 30)

points_text = font.render(str(points), True, consts.WHITE)
points_rect = points_text.get_rect().move(consts.WINDOW_WIDTH // 2 + 40, 110)

game_start_text = font_60.render("Press enter to start", True, consts.WHITE)
game_start_rect = game_start_text.get_rect(center=(consts.WINDOW_WIDTH // 2, consts.WINDOW_HEIGHT // 2))

level_completed_text = font_60.render("Level Completed", True, consts.WHITE)
level_completed_rect = level_completed_text.get_rect(center=(consts.WINDOW_WIDTH // 2, consts.WINDOW_HEIGHT // 2))

level_completed_subtext = font_40.render("Press ENTER to continue", True, consts.WHITE)
level_completed_subtext_rect = level_completed_subtext.get_rect(
    center=(consts.WINDOW_WIDTH // 2, (consts.WINDOW_HEIGHT // 2) + 80))

game_over_text = font_60.render("GAME OVER", True, consts.WHITE)
game_over_rect = game_over_text.get_rect(center=(consts.WINDOW_WIDTH // 2, consts.WINDOW_HEIGHT // 2))

game_over_subtext = font_40.render("Press ENTER to restart", True, consts.WHITE)
game_over_subtext_rect = game_over_subtext.get_rect(center=(consts.WINDOW_WIDTH // 2, (consts.WINDOW_HEIGHT // 2) + 80))

# soundeffects
pygame.mixer.init()

#screen
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
    global points, points_text, bricks_destroyed
    for i in range(len(array_bricks)):
        left_color_in_wall = pygame.rect.Rect(0, array_bricks[i][0]["rect"].y - 5, 10,
                                              consts.BRICK_HEIGHT * len(array_bricks) + consts.BRICK_SPACING)
        rigth_color_in_wall = pygame.rect.Rect(consts.WINDOW_WIDTH - 10, array_bricks[i][0]["rect"].y - 5, 10,
                                               consts.BRICK_HEIGHT * len(array_bricks))
        pygame.draw.rect(screen, array_bricks[0][0]["color"], left_color_in_wall)
        pygame.draw.rect(screen, array_bricks[0][0]["color"], rigth_color_in_wall)
        for j in range(len(array_bricks[i])):
            if (ball.colliderect(array_bricks[i][j]["rect"])
                    and array_bricks[i][j]["visible"] and not mec.ball_is_ghost and not game_idle):
                array_bricks[i][j]["visible"] = False
                mec.ball_hit_block()
                if array_bricks[i][j]["color"] == consts.YELLOW:
                    pygame.mixer.music.load(consts.BALL_HIT_BLOCK)
                    pygame.mixer.music.play()

                if array_bricks[i][j]["color"] == consts.GREEN:
                    pygame.mixer.music.load(consts.BALL_HIT_GREEN)
                    pygame.mixer.music.play()

                    rebound_speed = increase_speed_based_on_block(array_bricks[i][j]["color"])
                    if mec.ball_dx < 0:
                        mec.ball_dx = -1 * rebound_speed * randun(0.8,1.1)
                        mec.ball_dy =  rebound_speed * randun(0.8,1.1)
                    else:
                        mec.ball_dx = rebound_speed  * randun(0.8,1.1)
                        mec.ball_dy = rebound_speed  * randun(0.8,1.1)
                if array_bricks[i][j]["color"] == consts.ORANGE:
                    pygame.mixer.music.load(consts.BALL_HIT_ORANGE)
                    pygame.mixer.music.play()

                    rebound_speed = increase_speed_based_on_block(array_bricks[i][j]["color"])
                    if mec.ball_dx < 0:
                        mec.ball_dx = -1 * rebound_speed  * randun(0.8,1.1)
                        mec.ball_dy =  rebound_speed  * randun(0.8,1.1)
                    else:
                        mec.ball_dx = rebound_speed  * randun(0.8,1.1)
                        mec.ball_dy = rebound_speed  * randun(0.8,1.1)
                if array_bricks[i][j]["color"] == consts.RED:
                    pygame.mixer.music.load(consts.BALL_HIT_RED)
                    pygame.mixer.music.play()
                    rebound_speed = increase_speed_based_on_block(array_bricks[i][j]["color"])
                    if mec.ball_dx < 0:
                        mec.ball_dx = -1 * rebound_speed  * randun(0.8,1.1)
                        mec.ball_dy =  rebound_speed  * randun(0.8,1.1)
                    else:
                        mec.ball_dx = rebound_speed  * randun(0.8,1.1)
                        mec.ball_dy = rebound_speed  * randun(0.8,1.1)

                points += array_bricks[i][j]["point"]
                points_text = font.render(str(points), True, consts.WHITE)
                bricks_destroyed += 1
                pygame.time.delay(100)
            if array_bricks[i][j]["visible"]:
                pygame.draw.rect(screen, array_bricks[i][j]["color"], array_bricks[i][j]["rect"])


def set_all_blocks_visible(array_bricks):
    for i in range(len(array_bricks)):
        for j in range(len(array_bricks[i])):
            array_bricks[i][j]["visible"] = True


def start_game():
    global paddle, game_idle, game_start_text, ball, show_game_over, lifes, level, lifes_text, level_text, points, points_text, show_level_completed
    if game_idle:
        if show_game_over:
            show_game_over = False
            lifes = 4
            lifes_text = font.render(str(lifes), True, consts.WHITE)
            level = 1
            level_text = font.render(str(level), True, consts.WHITE)
            points = 0
            points_text = font.render(str(points), True, consts.WHITE)
        if show_level_completed:
            show_level_completed = False
        game_idle = False
        game_start_text = font.render("", True, consts.WHITE)
        paddle = pygame.Rect(consts.WINDOW_WIDTH // 2 - mec.get_paddle_width_by_level() // 2,
                             consts.WINDOW_HEIGHT - consts.PADDLE_HEIGHT - 20, mec.get_paddle_width_by_level(),
                             consts.PADDLE_HEIGHT)
        ball = pygame.Rect(rand(ball_size, consts.WINDOW_WIDTH - ball_size), consts.WINDOW_HEIGHT // 2 + 50, ball_size,
                           ball_size)


def reset_game():
    global game_idle, ball, paddle
    game_idle = True
    set_all_blocks_visible(bricks_red)
    set_all_blocks_visible(bricks_orange)
    set_all_blocks_visible(bricks_green)
    set_all_blocks_visible(bricks_yellow)
    ball = pygame.Rect(rand(ball_size, consts.WINDOW_WIDTH - ball_size), consts.WINDOW_HEIGHT // 2 + 50, ball_size,
                       ball_size)

    paddle = initial_paddle_rect


def game_over():
    global game_idle, show_game_over
    reset_game()
    show_game_over = True


def go_to_next_level():
    global level, level_text, bricks_destroyed, show_level_completed
    show_level_completed = True
    bricks_destroyed = 0
    level += 1
    level_text = font.render(str(level), True, consts.WHITE)
    mec.next_level(level)
    reset_game()


def verify_if_all_bricks_destroyed():
    if not game_idle:
        if bricks_destroyed == consts.BRICK_ROWS * consts.BRICK_COLS * 4 and level < 4:
            go_to_next_level()


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
        pygame.mixer.music.load(consts.BALL_HIT_PADDLE)
        pygame.mixer.music.play()

    if ball.y > consts.WINDOW_HEIGHT:
        ball = pygame.Rect(rand(ball_size, consts.WINDOW_WIDTH - ball_size), consts.WINDOW_HEIGHT // 2 + 50, ball_size,
                           ball_size)
        mec.ball_dx = 1
        mec.ball_dy = 1
        if lifes == 1:
            game_over()
            lifes -= 1
        else:
            lifes -= 1
            lifes_text = font.render(str(lifes), True, consts.WHITE)
        pygame.mixer.music.load(consts.BALL_HIT_PADDLE)

    # controls

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        pygame.quit()
    if key[pygame.K_RETURN]:
        start_game()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= consts.PADDLE_SPEED
    if key[pygame.K_RIGHT] and paddle.right < consts.WINDOW_WIDTH:
        paddle.right += consts.PADDLE_SPEED
    if key[pygame.K_s]:
        pygame.image.save(screen, 'SCREEN_IMAGE.jpg')
    # Blocos

    # RED
    draw_bricks(bricks_red)
    # ORANGE
    draw_bricks(bricks_orange)
    # GREEN
    draw_bricks(bricks_green)
    # YELLOW
    draw_bricks(bricks_yellow)

    verify_if_all_bricks_destroyed()

    # Texts
    screen.blit(level_text, level_rect)
    screen.blit(points_text, points_rect)
    screen.blit(lifes_text, lifes_rect)
    if show_level_completed:
        screen.blit(level_completed_text, level_completed_rect)
        screen.blit(level_completed_subtext, level_completed_subtext_rect)
    else:
        screen.blit(game_start_text, game_start_rect)
    if show_game_over:
        screen.blit(game_over_text, game_over_rect)
        screen.blit(game_over_subtext, game_over_subtext_rect)

    # update screen
    pygame.display.flip()
    clock.tick(consts.FPS)
