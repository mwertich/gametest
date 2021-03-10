

class Enemy:
    def __init__(self, x, y, width, height, vel_x, vel_y):
        self.x, self.y, self.width, self.height, self.vel_x, self.vel_y = x, y, width, height, vel_x, vel_y

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def out_of_border(self, win_size):
        return (self.x < -self.width) or (self.x > win_size) or (self.y < -self.height) or (self.y > win_size)

