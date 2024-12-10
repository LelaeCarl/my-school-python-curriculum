'''
NexonObject
'''
class NexonObject():
    # 1.初始化区域
    def __init__(self,screen,image,row,col):
        self.screen = screen
        self.image = image
        self.row = row
        self.col = col

    # 2.绘制自己
    def blitMe(self):
        # 2.1 根据row,col计算x,y
        bx = 25 + 50 * self.col
        by = 25 + 50 * self.row
        # 2.2 绘制图片
        self.screen.blit(self.image,(bx,by))

