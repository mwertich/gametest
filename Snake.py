import pygame
import sys

# colors
ROSA = (200, 100, 200)
RED = (200, 0, 0)
GREEN = (0, 255, 0)
WIDTH, HEIGHT = 500, 500

pygame.init()
# main settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
fps_control = pygame.time.Clock()

all_sprites = pygame.sprite.Group()


class Snake(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((100, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.speed = 5

    def update(self):
        keystate = pygame.key.get_pressed()
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if keystate[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keystate[pygame.K_RIGHT]:
            self.rect.x += self.speed

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

    screen.fill(GREEN)
    all_sprites.draw(screen)
    pygame.display.flip()
