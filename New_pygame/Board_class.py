from Enemy_class import *
win_size = 500

class Board():
    def __init__(self, win_size):
        self.win_size = win_size
        self.timer = 0
        self.enemies = []

    def add_enemy(self, x, y, w, h, vx, vy):
        self.enemies.append(Enemy(x, y, w, h, vx, vy))
