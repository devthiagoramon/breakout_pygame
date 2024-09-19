import pygame

WIDTH,HEIGHT = 1280,720
fps = 60

#creating paddle with rect
paddle_width = 330
paddle_height = 35
paddle_speed = 15
paddle = pygame.Rect(WIDTH//2 - paddle_width//2,HEIGHT - paddle_height -10,paddle_width,paddle_height)


pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()


#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    #draw the game
    pygame.draw.rect(screen,pygame.Color('blue'),paddle)
    #update screen
    pygame.display.update()
    clock.tick(fps)
