import pygame
import sys
import random
from Player_class import *

color_red = (255, 0, 0)
color_blue = (0, 0, 255)
timer_x = 0

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


def draw_rect(color, x, y, w, h):
    pygame.draw.rect(win, color, (x, y, w, h))

def generate_enemy():
    x, y, size = random.randint(0, win_size - width), random.randint(0, win_size - height), random.randint(30, 70)
    sx, sy = 0, 0
    while (sx == 0) or (sy == 0):
        sx = random.randint(-10, 10)
        sy = random.randint(-10, 10)
    board.add_enemy(x, y, size, size, sx, sy)


def update_win():
    board.timer = round(board.timer + 0.1, 1)
    win.fill((0, 0, 0))
    draw_rect(color_red, player.x, player.y, player.width, player.height)
    label = myfont.render(f"Time: {board.timer}", 1, (255, 255, 0))
    win.blit(label, (400, 50))
    if board.timer % 3 == 0:
        generate_enemy()
    for enemy in board.enemies:
        enemy.move()
        if enemy.out_of_border(win_size):
             board.enemies.remove(enemy)
        else:
            draw_rect(color_blue, enemy.x, enemy.y, enemy.width, enemy.height)
    pygame.display.update()




pygame.init()
win = pygame.display.set_mode((win_size, win_size))
pygame.display.set_caption("First game")
player = Player(random.randint(0, win_size-width), random.randint(0, win_size-height), width, height, vel)
board = Board(win_size)
myfont = pygame.font.SysFont("Timer:", 15)
run = True

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    check_event(pygame.key.get_pressed())


pygame.quit()
sys.exit()
