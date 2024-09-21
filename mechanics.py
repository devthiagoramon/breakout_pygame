import constants as consts

ball_dx = 1
ball_dy = 1
actual_max_speed = consts.MAX_BALL_SPEED_LEVEL_1
actual_paddle_width = consts.PADDLE_WIDTH_LEVEL_1
ball_is_ghost = False


def ball_hit_wall():
    global ball_dx,ball_is_ghost
    ball_dx = ball_dx * -1
    ball_is_ghost = False


def ball_hit_ceiling():
    global ball_dy, ball_dx, ball_is_ghost
    ball_dy = ball_dy * -1
    ball_dx = ball_dx * -1
    ball_is_ghost = False


def ball_hit_paddle(paddle_x, ball_x):
    global ball_dy, ball_dx, ball_is_ghost
    ball_dy = ball_dy * -1
    # ball_dx = ball_dx * -1
    middle_paddle = (paddle_x + actual_paddle_width) // 2
    ball_is_ghost = False
    if abs(ball_dy) >= actual_max_speed:
        return
    if ball_x < middle_paddle + paddle_x:
        dy_velocity_updated = abs(ball_x / middle_paddle)
        ball_dx = abs(ball_dx) * -1
        if ball_dy < 0:
            ball_dy -= dy_velocity_updated
        else:
            ball_dy += dy_velocity_updated
    if ball_x > middle_paddle + paddle_x:
        dy_velocity_updated = abs(middle_paddle / ball_x)
        ball_dx = abs(ball_dx)
        if ball_dy < 0:
            ball_dy -= dy_velocity_updated
        else:
            ball_dy += dy_velocity_updated


def ball_hit_block():
    global ball_dy, ball_is_ghost
    ball_dy *= -1
    ball_is_ghost = True


def next_level(level):
    global actual_max_speed, actual_paddle_width
    match level:
        case 2:
            actual_max_speed = consts.MAX_BALL_SPEED_LEVEL_2
            actual_paddle_width = consts.PADDLE_WIDTH_LEVEL_2
        case 3:
            actual_max_speed = consts.MAX_BALL_SPEED_LEVEL_3
            actual_paddle_width = consts.PADDLE_WIDTH_LEVEL_3
        case 4:
            actual_max_speed = consts.MAX_BALL_SPEED_LEVEL_4
            actual_paddle_width = consts.PADDLE_WIDTH_LEVEL_4


def get_paddle_width_by_level():
    return actual_paddle_width


def increase_speed_based_on_block (color):
    global actual_max_speed
    if color == consts.GREEN:
        return 3
    if color == consts.ORANGE:
        return 4
    if color == consts.RED:
        return 5


