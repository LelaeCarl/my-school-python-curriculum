'''
Destroy object
'''
from day8.NexonObject import  NexonObject

class Destroy(NexonObject):
    # 1.Initialization function
    def __init__(self,screen,images,row,col):
        self.screen = screen
        self.images  = images
        self.image = self.images[0]
        self.row = row
        self.col = col
        super().__init__(screen,self.image,self.row,self.col)
        self.index  = 0

    def step(self):
        self.index += 1
        ix = int(self.index/5%len(self.images))
        self.image = self.images[ix]
