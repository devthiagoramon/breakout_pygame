import main as main
import constants as consts

ball_dx = consts.BALL_SPEED
ball_dy = consts.BALL_SPEED


def ball_hit_wall():
    global ball_dx
    ball_dx = ball_dx * -1


def ball_hit_paddle(paddle_x, ball_x):
    global ball_dy
    ball_dy = ball_dy * -1
    hit_paddle_position = paddle_x + main.paddle_width






