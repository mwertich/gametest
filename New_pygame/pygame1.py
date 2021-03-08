import pygame
pygame.init()
win_size = 500
win = pygame.display.set_mode((win_size, win_size))
color_red = (255, 0, 0)
pygame.display.set_caption("First game")

x, y, width, height, vel  = 50, 50, 50, 50, 10

run = True




while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
        if x <= 0:
            x = 0

    if keys[pygame.K_RIGHT]:
        x += vel
        if x > win_size - width:
            x = win_size -width

    if keys[pygame.K_UP]:
        y -= vel
        if y <= 0:
            y = 0

    if keys[pygame.K_DOWN]:
        y += vel
        if y > win_size - height:
            y = win_size - height

    if keys[pygame.K_SPACE]:
        isJump = True

    win.fill((0, 0, 0))
    pygame.draw.rect(win, color_red, (x, y, width, height))
    pygame.display.update()

pygame.quit()
