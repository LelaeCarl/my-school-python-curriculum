'''
Pao类
'''
from day8.NexonObject import  NexonObject
class Pao(NexonObject):
    # 1.初始化区域
    def __init__(self,screen,images,row,col,type):
        self.screen = screen
        self.images = images
        self.image = self.images[0]
        self.row = row
        self.col = col
        self.type = type # 0 宝宝  1海海 2......
        super().__init__(screen,self.image,self.row,self.col)
        # 动画效果计数值
        self.index = 0
        # 延长属性  1,2,6(添加炸弹且无延伸) 0,3,4,5(无炸弹无延伸) 7(有炸弹有延伸)
        self.UP = True
        self.DOWN = True
        self.LEFT = True
        self.RIGHT = True

    # 2.动画效果
    def step(self):
        # 2.1 计算动画效果下标
        self.index += 1
        ix = int(self.index/10%len(self.images))
        self.image = self.images[ix]
