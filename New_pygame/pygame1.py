import pygame
import sys
import random

pygame.init()
win_size = 500
win = pygame.display.set_mode((win_size, win_size))
color_red = (255, 0, 0)
pygame.display.set_caption("First game")

x, y, width, height, vel  = 50, 50, 50, 50, 10

run = True



class Player():
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel

    def _check_border(self):
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0

    def move(self, x, y):
        self.x += x
        self.y += y
        self._check_border()




def start_game():
    return Player(random.randint(0, win_size-width), random.randint(0, win_size-height), width, height, vel)


def update_win():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, color_red, (x, y, width, height))
    pygame.display.update()


def run_game(player):

    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.move(-vel, 0)


    if keys[pygame.K_RIGHT]:
        player.move(vel, 0)

    if keys[pygame.K_UP]:
        player.move(0, vel)

    if keys[pygame.K_DOWN]:
        player.move(0, -vel)

    if keys[pygame.K_SPACE]:
        pass

    update_win()




    return True

if __name__ == '__main__':
    player = start_game()
    while run:
        run = run_game(player)

    pygame.quit()
    sys.exit()
