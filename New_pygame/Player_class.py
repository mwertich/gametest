from Board_class import *


class Player(Board):
    def __init__(self, x, y, width, height, vel):
        self.x, self.y, self.width, self.height, self.vel = x, y, width, height, vel
        self.win_size = win_size

    def move_left(self, vel):
        self.x -= vel
        if self.x < 0:
            self.x = 0

    def move_right(self, vel):
        self.x += vel
        if self.x > self.win_size - self.width:
            self.x = self.win_size - self.width

    def move_up(self, vel):
        self.y -= vel
        if self.y < 0:
            self.y = 0

    def move_down(self, vel):
        self.y += vel
        if self.y > self.win_size - self.width:
            self.y = self.win_size - self.width