

class Color:
    # colors
    ROSA = (200, 100, 200)
    RED = (200, 0, 0)
    GREEN = (0, 255, 0)
    WIDTH, HEIGHT = 1000, 1000
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)


class Map:
    # size
    WIDTH, HEIGHT = 1500, 1000
    SIZE_FIELD = 10
    AMOUNT = round(1000 / 10)

    def __init__(self):
        self.map = [[Color.BLACK for x in range(self.AMOUNT)] for y in range(self.AMOUNT)]


