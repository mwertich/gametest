import pygame
import sys

# colors
ROSA = (200, 100, 200)
RED = (200, 0, 0)
GREEN = (0, 255, 0)
WIDTH, HEIGHT = 1000, 1000
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
# main settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
fps_control = pygame.time.Clock()

all_sprites = pygame.sprite.Group()


class Snake(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((300, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (, HEIGHT/2)
        self.speed = 5

    def update(self):
        keystate = pygame.key.get_pressed()
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if keystate[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keystate[pygame.K_RIGHT]:
            self.rect.x += self.speed


class Board:
    def __init__(self):
        all_tiles = []
        tile_b = pygame.Surface((10, 10))
        tile_b.fill(BLACK)
        all_tiles.append(tile_b)

        tile_w = pygame.Surface((10, 10))
        tile_w.fill(BLACK)
        all_tiles.append(tile_w)


class App:
    def __init__(self):
        pass


snake = Snake(ROSA)
all_sprites.add(snake)



while True:
    fps_control.tick(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    all_sprites.update()

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

    all_sprites.draw(screen)
    pygame.display.flip()
