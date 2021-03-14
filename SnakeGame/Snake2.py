import pygame
import random
from typing import Union


class Snake:
    def __init__(self, color, direction, fields):
        self.color = color
        self.dir = direction
        self.body = fields
        self.moves = 0
        self.has_eaten = False

    def change_dir(self, dir):
        if dir == "N" and not(self.dir == "S"):
            self.dir = dir
        elif dir == "S" and not (self.dir == "N"):
            self.dir = dir
        elif dir == "E" and not (self.dir == "W"):
            self.dir = dir
        elif dir == "W" and not (self.dir == "E"):
            self.dir = dir

    def move(self):
        self.moves += 1
        if self.dir == "N":
            self.move_up()
        elif self.dir == "S":
            self.move_down()
        elif self.dir == "E":
            self.move_right()
        elif self.dir == "W":
            self.move_left()
        if self.has_eaten:
            self.has_eaten = False
        else:
            self.body.pop()

    def move_left(self):
        self.body.insert(0, (self.body[0][0] - 1, self.body[0][1]))

    def move_right(self):
        self.body.insert(0, (self.body[0][0] + 1, self.body[0][1]))

    def move_up(self):
        self.body.insert(0, (self.body[0][0], self.body[0][1] - 1))

    def move_down(self):
        self.body.insert(0, (self.body[0][0], self.body[0][1] + 1))

    def reset(self):
        self.dir, self.body, self.moves, self.has_eaten = "E", start_fields[:], 0, False


class Fruit:
    def __init__(self, pos):
        self.pos = pos
        self.color = RED


class Zombie:
    def __init__(self, pos, dir):
        self.color = GREEN
        self.pos = pos
        self.dir = dir

    def move(self):
        if self.dir == "N" and self.pos[1] == 0:
            self.dir = "S"
        elif self.dir == "S" and self.pos[1] == 20 - 1:
            self.dir = "N"
        if self.dir == "N":
            self.pos = self.pos[0], self.pos[1] - 1
        else:
            self.pos = self.pos[0], self.pos[1] + 1


class Flame:
    def __init__(self, pos, dir):
        self.color = YELLOW
        self.pos = pos
        self.dir = dir

    def move(self):
        if self.dir == "W" and self.pos[0] == 0:
            self.dir = "E"
        elif self.dir == "E" and self.pos[0] == 20 - 1:
            self.dir = "W"
        if self.dir == "E":
            self.pos = self.pos[0] + 1, self.pos[1]
        else:
            self.pos = self.pos[0] - 1, self.pos[1]




#Enemy = Union[Zombie, Flame]





class Board:
    def __init__(self, snake, size = 20, zoom = 50, state = "start"):
        self.snake = snake
        self.size = size
        self.zoom = zoom
        self.fruits = []
        self.spawn_rate = 20
        self.enemies = []
        self.grid = [[ 1 if (x % 2 == 0 and y % 2 == 1) or (x % 2 == 1 and y % 2 == 0) else 0 for x in range(self.size)] for y in range(self.size)]
        self.points = 0
        self.speed = fps
        self.level = 0
        self.state = state
        self.mode = 0

    def check_pos(self, pos):
        return not(pos in self.snake.body or pos in self.fruits)

    def add_fruit(self):
        pos = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
        while not(self.check_pos(pos)):
            pos = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
        self.fruits.append(Fruit(pos))

    def control_snake(self):
        x, y = self.snake.body[0][0], self.snake.body[0][1]
        return x < 0 or x >= self.size or y < 0 or y >= self.size or self.snake.body[0] in self.snake.body[1:]

    def control_fruit(self):
        for fruit in self.fruits:
            if self.snake.body[0] == fruit.pos:
                self.snake.has_eaten = True
                self.points += 1
                self.speed += 1
                self.fruits.remove(fruit)
                break

    def control_enemy(self):
        for enemy in self.enemies:
            if enemy.pos in self.snake.body:
                self.state = "game over"

    def control(self):
        if self.control_snake():
            self.state = "game over"
        else:
            self.control_fruit()
            self.control_enemy()

    def update(self):
        if self.snake.moves % self.spawn_rate == 0 and len(self.fruits) < 5:
            self.add_fruit()

    def draw_grid(self):
        for i in range(game.size):
            for j in range(game.size):
                if self.grid[i][j] == 1:
                    pygame.draw.rect(screen, WHITE, [j * zoom, i * zoom, zoom, zoom])
                else:
                    pygame.draw.rect(screen, BLACK, [j * zoom, i * zoom, zoom, zoom])

    def draw_interface(self):
        pygame.draw.rect(screen, GRAY, [0, self.size * zoom, self.size * zoom, 100])
        screen.blit(font.render(f"Moves: {self.snake.moves}", True, RED), (200, 1050))
        screen.blit(font.render(f"Points: {self.points}", True, RED), (400, 1050))
        screen.blit(font.render(f"Level: {self.level}", True, RED), (600, 1050))

    def draw_snake(self):
        for part in self.snake.body:
            pygame.draw.rect(screen, self.snake.color, [part[0] * zoom, part[1] * zoom, zoom, zoom])

    def draw_fruits(self):
        for fruit in self.fruits:
            pygame.draw.rect(screen, fruit.color, [fruit.pos[0] * zoom, fruit.pos[1] * zoom, zoom, zoom])

    def draw_enemies(self):
        for enemy in self.enemies:
            pygame.draw.rect(screen, enemy.color, [enemy.pos[0] * zoom, enemy.pos[1] * zoom, zoom, zoom])

    def draw(self):
        screen.fill(color=WHITE)
        self.draw_grid()
        self.draw_fruits()
        self.draw_snake()
        self.draw_enemies()
        self.draw_interface()
        pygame.display.flip()



    def reset(self):
        self.snake.reset()
        self.fruits, self.enemies, self.points, self.speed, self.level, self.state, self.mode = [], [], 0, fps, 0, "start", 0


class Menu:
    def __init__(self, size):
        self.size = size

    def draw_button(self, x, y, w, h):
        pygame.draw.rect(screen, GRAY, [x, y, w, h])

    def draw_level_buttons(self):
        for x in range(0, 6):
            self.draw_button(100 + x * 150, 800, 100, 100)
            screen.blit(font_menu.render(f"{x + 1}", True, RED), (140 + x * 150, 830))
            self.draw_button(100 + x * 150, 950, 100, 100)
            screen.blit(font_menu.render(f"{x + 7}", True, RED), (140 + x * 150, 980))

    def draw(self):
        screen.fill(color=WHITE)
        pygame.draw.rect(screen, GRAY, [400, 450, 200, 200])
        self.draw_button(400, 450, 200, 200)
        self.draw_level_buttons()
        screen.blit(font_menu.render("New Snake Game", True, RED), (300, 350))
        screen.blit(font_menu.render("Start", True, RED), (445, 525))
        screen.blit(font_menu.render("Level:", True, RED), (400, 700))
        pygame.display.flip()

    def control_click(self, pos):
        x, y = pos[0], pos[1]
        if x >= 400 and x <= 600 and y >= 450 and y <= 650:
            game.state = "run"
            game.mode = 0

        elif x >= 100 and x<= 200 and y >= 800 and y <= 900:
            game.state = "run"
            game.level = 1
            game.enemies = [Zombie((4, 0), "S"), Zombie((8, 0), "S"), Zombie((12, 0), "S"), Zombie((16, 0), "S")]

        elif x >= 250 and x<= 350 and y >= 800 and y <= 900:
            game.state = "run"
            game.level = 2
            game.enemies = [Zombie((4, 0), "S"), Zombie((8, 0), "S"), Zombie((12, 0), "S"), Zombie((16, 0), "S"),
                            Zombie((6, 19), "N"), Zombie((10, 19), "N"), Zombie((14, 19), "N")]

        elif x >= 400 and x <= 500 and y >= 800 and y <= 900:
            game.state = "run"
            game.level = 3
            game.enemies = [Zombie((4, 0), "S"), Zombie((8, 0), "S"), Zombie((12, 0), "S"), Zombie((16, 0), "S"),
                    Flame((19, 4), "W"), Flame((19, 8), "W"), Flame((19, 12), "W"), Flame((19, 16), "W")]

        elif x >= 550 and x <= 650 and y >= 800 and y <= 900:
            game.state = "run"
            game.level = 4
            game.enemies = [Zombie((0, 0), "S"), Zombie((4, 19), "N"), Zombie((8, 0), "S"), Zombie((12, 19), "N"), Zombie((16, 0), "S"),
                            Zombie((20, 19), "N"), Flame((19, 4), "W"), Flame((0, 8), "E"), Flame((19, 12), "W"), Flame((0, 16), "E")]


pygame.init()
SIZE = (1000, 1100)
screen = pygame.display.set_mode((SIZE[0], SIZE[1]))
pygame.display.set_caption("Snake")


done = False
fps = 5
clock = pygame.time.Clock()
zoom = 50
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
start_fields = [(2, 10), (1, 10), (0, 10)]
levels = [
    [Zombie((4, 0), "S"), Zombie((8, 0), "S"), Zombie((12, 0), "S"), Zombie((16, 0), "S")]
]
level1 = levels[0]


start_snake = Snake(BLUE, "E", start_fields[:])
start_game = Board(start_snake, 20)
snake = start_snake
game = start_game
menu = Menu((1000, 1100))
font = pygame.font.SysFont("C:", 50)
font_menu = pygame.font.SysFont("C", 70)

while not done:
    if game.state == "start":
        menu.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu.control_click(pygame.mouse.get_pos())

    elif game.state == "run":
        clock.tick(game.speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.snake.change_dir("N")
                elif event.key == pygame.K_DOWN:
                    game.snake.change_dir("S")
                elif event.key == pygame.K_LEFT:
                    game.snake.change_dir("W")
                elif event.key == pygame.K_RIGHT:
                    game.snake.change_dir("E")
                break
        game.snake.move()
        for enemy in game.enemies:
            enemy.move()
        game.control()
        if game.state == "run":
            game.update()
            game.draw()
        else:
            game.reset()
pygame.quit()
