import pygame
import sys
import random
from Player_class import *

win_size = 500
color_red = (255, 0, 0)

width, height, vel = 50, 50, 10




def check_event(keys):
    if keys[pygame.K_LEFT]:
        player.move_left(player.vel)

    if keys[pygame.K_RIGHT]:
        player.move_right(player.vel)

    if keys[pygame.K_UP]:
        player.move_up(player.vel)

    if keys[pygame.K_DOWN]:
        player.move_down(player.vel)

    if keys[pygame.K_SPACE]:
        pass
    update_win()




def update_win():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, color_red, (player.x, player.y, player.width, player.height))
    pygame.display.update()




pygame.init()
win = pygame.display.set_mode((win_size, win_size))
pygame.display.set_caption("First game")
player = Player(random.randint(0, win_size-width), random.randint(0, win_size-height), width, height, vel)
board = Board(win_size)


run = True


while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    check_event(pygame.key.get_pressed())


pygame.quit()
sys.exit()
