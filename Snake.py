import pygame
import sys

# colors
ROSA = (200, 100, 200)
RED = (200, 0, 0)
GREEN = (0, 255, 0)
WIDTH, HEIGHT = 1000, 1000
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAIN = 50

pygame.init()
# main settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
fps_control = pygame.time.Clock()

all_sprites = pygame.sprite.Group()


class Snake:
    def __init__(self, color, grain):
        self.grain = grain
        self.direction = 1
        self.image = pygame
        self.size = (grain, grain)
        self.headx = 250
        self.heady = 250
        self.head = None

    def check_head(self):
        if self.head.left > WIDTH:
            self.head.right = 0

    def update(self):
        self.move_head()
        self.head = pygame.Rect((self.headx, self.heady), self.size)

    def check_keys(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.direction = 0
        if keystate[pygame.K_RIGHT]:
            self.direction = 1
        if keystate[pygame.K_DOWN]:
            self.direction = 2
        if keystate[pygame.K_LEFT]:
            self.direction = 3

    def move_head(self):
        self.check_keys()
        if self.direction == 0:
            self.heady += self.grain
        if self.direction == 1:
            self.headx += self.grain
        if self.direction == 2:
            self.heady -= self.grain
        if self.direction == 3:
            self.headx -= self.grain

    def check_dir(self):
        pass


class Board:
    def __init__(self):
        all_tiles = []
        tile_b = pygame.Surface((10, 10))
        tile_b.fill(BLACK)
        all_tiles.append(tile_b)

        tile_w = pygame.Surface((10, 10))
        tile_w.fill(BLACK)
        all_tiles.append(tile_w)


def draw_grid():
    all_tiles = []
    tile_b = pygame.Surface((50, 50))
    tile_b.fill(BLACK)
    all_tiles.append(tile_b)

    tile_w = pygame.Surface((50, 50))
    tile_w.fill(WHITE)
    all_tiles.append(tile_w)

    count_col = 0
    for i in range(0, HEIGHT, 50):
        count_col += 1
        count = 0 + count_col
        for j in range(0, WIDTH, 50):
            screen.blit(all_tiles[count % 2], (i, j))
            count += 1


snake = Snake(ROSA, 50)


while True:
    fps_control.tick(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_grid()
    snake.update()
    pygame.draw.rect(screen, ROSA, snake.head)
    pygame.display.flip()
