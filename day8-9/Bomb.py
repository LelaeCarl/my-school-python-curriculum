'''
Bomb
'''
from day8.NexonObject import NexonObject

class Bomb(NexonObject):
    # 1. Initialize the area
    def __init__(self, screen, images, row, col, ix):
        self.screen = screen
        self.images = images
        self.image = self.images[ix]
        self.row = row
        self.col = col
        super().__init__(screen, self.image, self.row, self.col)
        self.index = 0

    # 2. Define the step function
    def step(self):
        self.index += 1

