import pygame
import sys
import random

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
    def __init__(self, color, grain, length, start: tuple):
        self.grain = grain
        self.direction = 1
        self.size = (grain, grain)
        self.body = [(start[0] + i * 50, start[1]) for i in range(length)]
        self.bodyrect = None
        self.alive = True
        self.fed_fruit = False

    def update(self):
        self.move_head()
        self.bodyrect = []
        for i in range(len(self.body)):
            self.bodyrect.append(pygame.Rect(self.body[i], self.size))

    def check_keys(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP] and self.direction != 2:
            self.direction = 0
        if keystate[pygame.K_RIGHT] and self.direction != 3:
            self.direction = 1
        if keystate[pygame.K_DOWN] and self.direction != 0:
            self.direction = 2
        if keystate[pygame.K_LEFT] and self.direction != 1:
            self.direction = 3

    def move_head(self):
        self.check_keys()
        if self.direction == 0:
            new_head = (self.body[-1][0], self.body[-1][1] - self.grain)
        if self.direction == 1:
            new_head = (self.body[-1][0] + self.grain, self.body[-1][1])
        if self.direction == 2:
            new_head = (self.body[-1][0], self.body[-1][1] + self.grain)
        if self.direction == 3:
            new_head = (self.body[-1][0] - self.grain, self.body[-1][1])

        self.body.append(new_head)
        if not self.fed_fruit:
            self.body.pop(0)
        self.fed_fruit = False


class Collisions:
    def __init__(self, player: Snake):
        self.player = player
        self.feedback = [pygame.font.SysFont('comicsansms', 50)]

    def snake_col(self):
        if len(self.player.body) != len(set(self.player.body)):
            screen.blit(self.feedback[0].render('Game over', 0, ROSA), (250, 250))
            snake.alive = False


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


class Fruit:
    def __init__(self, pos: tuple, color=RED):
        self.color = color
        self.pos = pos

class Board:
    def __init__(self, player, fps, size=1000):
        self.fruits = []
        self.player = player
        self.size = size
        self.counter = 0
        self.fps = fps

    def gen_pos(self):
        return random.randint(0, 20), random.randint(0, 20)

    def check_pos(self, pos):
        if pos in self.player.body:
            return False
        for fruit in self.fruits:
            if fruit.pos == pos:
                return False
        return True

    def spawn_fruit(self):
        pos = self.gen_pos()
        while not self.check_pos(pos):
            pos = self.gen_pos()

        self.fruits.append(Fruit(pos))

    def check_fruits(self):
        for fruit in self.fruits:
            if self.player.body[-1] == (fruit.pos[0] * 50, fruit.pos[1] * 50):
                self.fps += 1
                self.fruits.remove(fruit)
                self.player.fed_fruit = True

    def update(self):
        if self.counter % 50 == 0:
            self.spawn_fruit()
        self.check_fruits()

    def draw(self):
        self.player.update()
        for fruit in self.fruits:
            pygame.draw.rect(screen, fruit.color, [fruit.pos[0]* 50, fruit.pos[1] * 50, 50, 50])





snake = Snake(ROSA, 50, 5, (300, 300))
colis = Collisions(snake)
board = Board(snake, 10)

while True:
    fps_control.tick(board.fps)
    board.counter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_grid()
    board.update()
    board.draw()
    colis.snake_col()
    if not snake.alive:
        pygame.quit()
        sys.exit()
    for part in snake.bodyrect:
        pygame.draw.rect(screen, ROSA, part)
    pygame.display.flip()

