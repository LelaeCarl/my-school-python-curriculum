'''
Prop
'''
import random

from day8.NexonObject import  NexonObject
class Prop(NexonObject):
    # 1.初始化区域
    def __init__(self,screen,images,row,col):
        self.screen = screen
        self.images = images
        # 随机出道具类型 0药水 1泡泡  2旱冰鞋
        self.type = random.randint(0,2)
        self.image = self.images[self.type]
        self.row = row
        self.col = col
        super().__init__(screen,self.image,self.row,self.col)