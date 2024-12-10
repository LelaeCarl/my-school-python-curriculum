'''
SetImage
工具类 加载所有的图片资源
'''
import pygame.image


class SetImage():
    # 1. 初始化区域
    def __init__(self):
        # 1.1 背景图片
        self.back = pygame.image.load("img/zhan2.jpg")
        # 1.2 地板图片列表
        self.floorImgs = [
            pygame.image.load("img/diban1.png"),
            pygame.image.load("img/diban3.png"),
            pygame.image.load("img/diban4.png")
        ]
        # 1.3 建筑物图列表
        self.builderImgs = [
            pygame.image.load("img/shu.png"),
            pygame.image.load("img/red.png"),
            pygame.image.load("img/orange.png"),
            pygame.image.load("img/redHouse.png"),
            pygame.image.load("img/yellowHose.png"),
            pygame.image.load("img/blueHose.png"),
            pygame.image.load("img/box.png")
        ]
        # 1.4 宝宝图片列表
        self.baoImgs = [
            pygame.image.load("img/up.png"),
            pygame.image.load("img/down.png"),
            pygame.image.load("img/left.png"),
            pygame.image.load("img/right.png")
        ]
        # 1.5 泡泡图片列表
        self.paoImgs = [
            pygame.image.load("img/PP1.png"),
            pygame.image.load("img/PP2.png")
        ]
        # 1.6 炸弹图片列表
        self.bombImgs = [
            pygame.image.load("img/bombUp.png"),
            pygame.image.load("img/Bombing.png")
        ]
        # 1.7 销毁图片列表
        self.destroyImgs = [
            pygame.image.load("img/destroy0.png"),
            pygame.image.load("img/destroy1.png"),
            pygame.image.load("img/destroy2.png"),
            pygame.image.load("img/destroy3.png")
        ]
        # 1.8 道具图片列表
        self.propImgs = [
            pygame.image.load("img/yaoshui.png"),
            pygame.image.load("img/paoPower.png"),
            pygame.image.load("img/hanbingxie.png")
        ]
