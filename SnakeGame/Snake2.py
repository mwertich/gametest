import pygame
import random


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


class Board:
    def __init__(self, snake, size = 20, zoom = 50, state = "start"):
        self.snake = snake
        self.size = size
        self.zoom = zoom
        self.fruits = []
        self.spawn_rate = 20
        self.state = state
        self.grid = [[ 1 if (x % 2 == 0 and y % 2 == 1) or (x % 2 == 1 and y % 2 == 0) else 0 for x in range(self.size)] for y in range(self.size)]
        self.points = 0
        self.speed = fps
        self.level = 1

    def add_fruit(self):
        pos = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
        while not(self.check_pos(pos)):
            pos = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
        self.fruits.append(Fruit(pos))

    def check_pos(self, pos):
        return not(pos in self.snake.body or pos in self.fruits)

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

    def control(self):
        if self.control_snake():
            self.state = "game over"
        else:
            self.control_fruit()

    def update(self):
        if self.snake.moves % self.spawn_rate == 0:
            self.add_fruit()

    def draw(self):
        screen.fill(color=WHITE)
        self.draw_grid()
        self.draw_fruits()
        self.draw_snake()
        self.draw_interface()
        pygame.display.flip()

    def reset(self):
        self.snake.reset()
        self.fruits, self.points, self.speed, self.level, self.state = [], 0, fps, 1, "start"


class Menu:
    def __init__(self, size):
        self.size = size

    def draw(self):
        screen.fill(color=WHITE)
        pygame.draw.rect(screen, GRAY, [400, 450, 200, 200])
        screen.blit(font_menu.render("New Game", True, RED), (370, 400))
        screen.blit(font_menu.render("Start", True, RED), (460, 530))
        pygame.display.flip()

    def control_click(self, pos):
        x, y = pos[0], pos[1]
        if x >= 400 and x <= 600 and y >= 450 and y <= 650:
            game.state = "run"


pygame.init()
SIZE = (1000, 1100)
screen = pygame.display.set_mode((SIZE[0], SIZE[1]))
pygame.display.set_caption("Snake")

done = False
fps = 6
clock = pygame.time.Clock()
zoom = 50
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
start_fields = [(4, 10), (3, 10), (2, 10), (1, 10), (0, 10)]
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
        game.snake.move()
        game.control()
        if not(game.state == "game over"):
            game.update()
            game.draw()
        else:
            game.reset()
pygame.quit()
