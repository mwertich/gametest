import pygame
import sys
import cv2
from Map import *

# colors

pygame.init()
# main settings
map = Map()
screen = pygame.display.set_mode((map.WIDTH, map.HEIGHT))
pygame.display.set_caption('Paintmap')
fps_control = pygame.time.Clock()
myfont = pygame.font.SysFont("Color:", 25)
pygame.draw.rect(screen, Color.WHITE, (1000, 0, 500, 1000))
for y in range(256):
    pygame.draw.rect(screen, (y, 0, 0), (1100, y + 400, 50, 1))
    pygame.draw.rect(screen, (0, y, 0), (1200, y + 400, 50, 1))
    pygame.draw.rect(screen, (0, 0, y), (1300, y + 400, 50, 1))


pygame.draw.rect(screen, Color.WHITE, (1100, 700, 50, 50))
pygame.draw.rect(screen, Color.WHITE, (1200, 700, 50, 50))
pygame.draw.rect(screen, Color.WHITE, (1300, 700, 50, 50))
pygame.draw.rect(screen, Color.WHITE, (1150, 800, 150, 150))



class Mouse():
    pressed = False
    ac_color = Color.WHITE


def check_event(event):
    keystate = pygame.key.get_pressed()
    pos = pygame.mouse.get_pos()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN:
        Mouse.pressed = True

    if event.type == pygame.MOUSEBUTTONUP:
        Mouse.pressed = False

    if keystate[pygame.K_ESCAPE]:
        pygame.draw.rect(screen, Color.BLACK, (0, 0, 1000, 1000))

    if Mouse.pressed:
        x, y = pos[0], pos[1]
        if x < 1000:
            draw_rect(calc_pos(pos))
        elif x >= 1100 and x <= 1150 and y >= 400 and y <= 655:
            Mouse.ac_color = (y - 400, Mouse.ac_color[1], Mouse.ac_color[2])
            pygame.draw.rect(screen, (y - 400, 0, 0), (1100, 700, 50, 50))
            pygame.draw.rect(screen, Mouse.ac_color, (1150, 800, 150, 150))

        elif x >= 1200 and x <= 1250 and y >= 400 and y <= 655:
            Mouse.ac_color = (Mouse.ac_color[0], y - 400, Mouse.ac_color[2])
            pygame.draw.rect(screen, (0, y - 400, 0), (1200, 700, 50, 50))
            pygame.draw.rect(screen, Mouse.ac_color, (1150, 800, 150, 150))

        elif x >= 1300 and x <= 1350 and y >= 400 and y <= 655:
            Mouse.ac_color = (Mouse.ac_color[0], Mouse.ac_color[1], y - 400)
            pygame.draw.rect(screen, (0, 0, y - 400), (1300, 700, 50, 50))
            pygame.draw.rect(screen, Mouse.ac_color, (1150, 800, 150, 150))
        pygame.draw.rect(screen, Color.WHITE, (1000, 0, 400, 300))
        screen.blit(myfont.render(f"Color: {Mouse.ac_color}", True, Color.RED), (1200, 200))


def calc_pos(t):
    return ((t[0] // map.SIZE_FIELD) * map.SIZE_FIELD, (t[1] // map.SIZE_FIELD) * map.SIZE_FIELD)


def draw_rect(t):
    pygame.draw.rect(screen, Mouse.ac_color, (t[0], t[1], Map.SIZE_FIELD, map.SIZE_FIELD))


while True:
    pygame.time.wait(1)
    for event in pygame.event.get():
        check_event(event)
    pygame.display.flip()
