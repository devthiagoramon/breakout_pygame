import pygame

WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
fps = 60

#creating paddle with rect
paddle_width = 330
paddle_height = 35
paddle_speed = 15
paddle = pygame.Rect(WINDOW_WIDTH//2 - paddle_width//2,WINDOW_HEIGHT - paddle_height -10,paddle_width,paddle_height)


pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()



#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    #controls
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed

    if key[pygame.K_RIGHT] and paddle.right <WINDOW_WIDTH:
        paddle.right += paddle_speed




    #draw the game
    pygame.draw.rect(screen,pygame.Color('blue'),paddle)
    #update screen
    pygame.display.update()
    clock.tick(fps)
