'''
Baby Object
'''
from day8.NexonObject import NexonObject
class Bao(NexonObject):
    # 1.初始化区域
    def __init__(self,screen,images):
        self.screen = screen
        self.images = images # 图片列表(上下左右)
        self.image = self.images[1] # 单张图片
        self.row = 0
        self.col = 13
        super().__init__(screen,self.image,self.row,self.col)
        self.number = 1
        self.power = 1
        self.speed = 1

