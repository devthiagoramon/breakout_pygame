import main as main
import constants as consts

ball_dx = consts.BALL_SPEED
ball_dy = consts.BALL_SPEED


def ball_hit_wall():
    global ball_dx
    ball_dx = ball_dx * -1


def ball_hit_ceiling():
    global ball_dy, ball_dx
    ball_dy = ball_dy * -1
    ball_dx = ball_dx * -1


def ball_hit_paddle(paddle_x, ball_x):
    global ball_dy, ball_dx
    ball_dy = ball_dy * -1
    ball_dx = ball_dx * -1
    middle_paddle = (paddle_x + consts.PADDLE_WIDTH) // 2

    if ball_x < middle_paddle:
        dy_velocity_updated = abs(ball_x / middle_paddle)
        ball_dy += dy_velocity_updated
    if ball_x > middle_paddle:
        dy_velocity_updated = abs(middle_paddle / ball_x)
        ball_dy += dy_velocity_updated

