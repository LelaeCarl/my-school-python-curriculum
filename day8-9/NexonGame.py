'''
NexonGame

Build the main project structure
1.1 Window size 925*700
Draw background image
2.1 Create a new class SetImage (utility class to load all images)
2.2 Area 1: 1.2 Set the SetImage object self.setImg
2.3 Area 4: 4.1 Draw background image
Draw floor image
3.1 Area 1: 1.3 Set the floor image list self.floorMap
3.2 Area 4: 4.2 Call self.paintFloor() function
Draw building images
4.1 In SetImage, set self.builderImgs
Tree: 0
Red module: 1
Orange module: 2
Red house: 3
Yellow house: 4
Blue house: 5
Box: 6
Blank: 7
4.2 Area 1: 1.4 Set building image self.builderMap
4.3 Area 4: 4.3 Call self.paintBuilder()
Draw the baby
5.1 Create a new class NexonObject to set x, y, screen, img, and the blitMe function
5.2 Create a new class BaoBao inheriting from NexonObject
5.3 In SetImage class, add baoImgs
5.4 Area 1: 1.5 Set the baby object self.bao
5.5 Area 4: 4.4 Call to draw baby object
5.6 Area 3: 3.3 Keyboard event listening for wasd
5.7 Area 3: In baby keyboard event listening, call step function
5.8 Area 3: step function calls judgeOutType function
Draw bubbles
6.1 Create a new class Pao inheriting from NexonObject
6.2 In SetImage class, add paoImgs
6.3 Area 1: 1.6 Add self.paos list
6.4 Area 3: 3.3 Check if the j key is pressed to add a bubble
6.5 Area 4: 4.5 Call self.paintPao() function to draw bubbles
6.6 In Pao class, add the step function for animation
6.7 Area 3: 3.4 Call stepAction() function to animate all objects (align to 3.1)
6.8 Area 3: 3.4 Set the disappearance of the bubble
Draw bombs
7.1 Create a new class Bomb inheriting from NexonObject (screen, images, row, col)
7.2 In SetImage class, add bombImgs (two images)
7.3 Area 1: 1.7 Add bomb list self.bombs
7.4 Area 3: 3.4 When bubbles disappear, call self.createBomb(pao)
7.5 Area 3: 3.4.1 In createBomb, create 5 bombs and add them to self.bombs
7.6 In Bomb class, add attribute self.index and method step to increment index += 1
7.7 Area 3: 3.4 In stepAction, loop through bombs to check if they disappear
7.8 Area 4: 4.6 Call self.paintBomb() to loop through bombs and draw them
7.9 Area 3: 3.4.1 In createBomb, add checks for out-of-bounds and type issues
7.10 Area 3: 3.4.1.1 judgeOutType2
Non-explodable types: 0, 3, 4, 5
7.11 Area 3: 3.4 In stepAction, delete bombs and buildings
Draw destroyed objects
8.1 Create a Destroy object inheriting from NexonObject
8.2 In SetImage, add self.destroyImgs
8.3 Area 1: 1.8 Add self.destroys = []
8.4 Area 3: 3.4 In stepAction, loop through bombs to check if buildings are destroyed
If the type is 1, 2, or 6, create a Destroy object and add it
8.5 Area 4: 4.7 Call self.paintDestroy() function
8.6 Area 3: 3.4 In stepAction, loop through destroy objects and call step function for destruction animation (index: 0-5, 6-10, 10-15, 15-20)
8.7 Area 3: 3.4 In stepAction, loop through destroy objects to check if index exceeds 20 and delete destroyed objects
Props
9.1 Create a new class Prop inheriting from NexonObject
9.2 In SetImage, add propImgs
0 Potion
1 Bubble
2 Roller skates
9.3 Area 1: 1.9 Add self.props
9.4 Area 3: 3.4.3 In stepAction, loop through destroyed objects to randomly add props
9.5 Area 4: 4.8 Call to draw prop objects using self.paintProp()
9.6 Area 3: 3.3 Call function to collect props self.coincideProp()
9.7 In Bao class, add three prop attributes: number (bubble), power (potion), speed (roller skates)
Implement prop effects
10.1 In Pao class, add a type attribute and set it in self.paos
10.2 Area 3: 3.3 When the j key is pressed, check the number of bubbles to be placed
10.3 Area 3: 3.4 In stepAction, adjust the number of bubbles
10.4 Area 3: In createBomb(), loop through objects based on values
10.5 In Pao class, add extension attributes: UP, DOWN, LEFT, RIGHT
Complete Haihai-related operations for two-player game functionality
Determine Win or Loss
12.1 If a bubble exists in a row/column, the main character cannot move
12.2 Area 3: In stepAction, loop through bombs
If bomb’s row/column matches the baby or Haihai’s row/column, it indicates death => change to death status image
12.3 Draw score image
State settings
13.1 When the game starts, enter the welcome screen and click the two-player button
Enter game state
13.2 Area 1: Set game state values
self.state = 0, 1, 2, 3
0: Welcome screen
1: Game screen
2: Baby wins
3: Haihai wins
Complete music playback
'''
import random
import sys

import pygame.display

from day8.SetImage import SetImage
from day8.Bao import Bao
from day8.Pao import Pao
from day8.Bomb import  Bomb
from day8.Destroy import  Destroy
from day8.Prop import  Prop
class NexonGame():
    '''First area: Initialization area'''
    def __init__(self):
        # 1.1 创建窗口对象
        self.screen = pygame.display.set_mode((925,700))
        # 1.2 设置图片加载类
        self.setImg = SetImage()
        # 1.3 设置地板图
        self.floorMap = [
            [0,0,0,0,0,0,1,2,1,0,0,0,0,0,0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0]
        ]
        # 1.4 设置建筑物图
        self.builderMap = [
            [7, 2, 1, 2, 1, 0, 7, 7, 6, 0, 5, 3, 5, 7, 5],
            [7, 3, 6, 3, 7, 0, 6, 7, 7, 0, 1, 2, 7, 7, 7],
            [7, 7, 2, 1, 2, 0, 7, 6, 6, 0, 5, 6, 5, 6, 5],
            [6, 5, 6, 5, 6, 0, 6, 7, 7, 0, 2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1, 1, 7, 7, 6, 0, 5, 6, 5, 6, 5],
            [2, 3, 2, 3, 2, 3, 6, 6, 7, 7, 1, 2, 1, 2, 1],
            [0, 0, 0, 0, 0, 0, 7, 7, 6, 0, 0, 0, 0, 0, 0],
            [1, 2, 1, 2, 1, 7, 6, 7, 7, 2, 1, 3, 1, 3, 7],
            [4, 6, 4, 6, 4, 0, 6, 6, 7, 0, 2, 1, 2, 7, 7],
            [2, 1, 2, 1, 2, 0, 7, 7, 7, 0, 6, 3, 6, 3, 7],
            [4, 7, 4, 6, 4, 0, 7, 6, 7, 0, 1, 2, 1, 2, 7],
            [7, 7, 1, 2, 1, 0, 6, 7, 7, 0, 6, 3, 7, 3, 7],
            [4, 7, 4, 1, 4, 0, 7, 6, 7, 0, 2, 7, 7, 7, 7]
        ]
        # 1.5 设置宝宝对象
        self.bao = Bao(self.screen,self.setImg.baoImgs)
        # 1.6 设置泡泡列表
        self.paos = []
        # 1.7 设置炸弹列表
        self.bombs = []
        # 1.8 设置销毁列表
        self.destroys = []
        # 1.9 设置道具列表
        self.props = []

    '''第二区域:主架构区域'''
    def Menu(self):
        # 2.1 设置窗口标题
        pygame.display.set_caption("泡泡堂")
        # 2.2 死循环
        while True:
            # 2.3 调用业务执行函数
            self.action()
            # 2.4 调用绘制函数
            self.paint()
            # 2.5 设置屏幕刷新
            pygame.display.update()

    '''第三区域:业务执行函数'''
    def action(self):
        # 3.1 循环遍历所有的监听事件
        for event in pygame.event.get():
            # 3.2 判断是否退出
            if event.type == pygame.QUIT:
                sys.exit(0)
            '''3.3 判断键盘监听事件'''
            if event.type == pygame.KEYDOWN:
                '''3.3.1 宝宝键盘监听'''
                if event.key == pygame.K_w:
                    self.step(self.bao,0)
                elif event.key == pygame.K_s:
                    self.step(self.bao,1)
                elif event.key == pygame.K_a:
                    self.step(self.bao,2)
                elif event.key == pygame.K_d:
                    self.step(self.bao,3)
                elif event.key == pygame.K_j \
                        and self.bao.number >= 1:
                    # 减少泡泡放置的数量
                    self.bao.number -= 1
                    # 添加泡泡对象
                    pao = Pao(self.screen,
                              self.setImg.paoImgs,
                              self.bao.row,self.bao.col,0)
                    self.paos.append(pao)

        # 3.4 走一步函数
        self.stepAction()

    '''3.3 移动函数'''
    def step(self,obj,dir):
        # 3.3.3 获取对象当前的行和列
        row = obj.row
        col = obj.col

        # 3.3.1 根据移动方向修改行列值
        if dir == 0 and self.judgeOutType(row-1,col):
            obj.row -= 1
        elif dir == 1 and self.judgeOutType(row+1,col):
            obj.row += 1
        elif dir == 2 and self.judgeOutType(row,col-1):
            obj.col -= 1
        elif dir == 3 and self.judgeOutType(row,col+1):
            obj.col += 1
        # 3.3.2 根据方向修改图片 (上下左右)
        obj.image = obj.images[dir]

        # 3.3.4 调用捡取道具功能
        self.coincideProp(obj)
    '''3.3.4 捡取道具功能'''
    def coincideProp(self,obj):
        for prop in self.props:
            # 判断是否重合
            if prop.row == obj.row and \
                prop.col == obj.col:
                # 根据道具类型添加obj道具属性中
                if prop.type == 0:
                    obj.power += 1
                elif prop.type == 1:
                    obj.number += 1
                elif prop.type == 2:
                    obj.speed += 1
                # 删除道具
                self.props.remove(prop)

    '''3.3.1 判断是否出界以及建筑物类型'''
    def judgeOutType(self,nextRow,nextCol):
        # 判断是否出界
        if 0<=nextRow<13 and \
            0<=nextCol<15:
            return self.builderMap[nextRow][nextCol] == 7
        return  False

    '''3.4 走一步函数'''
    def stepAction(self):
        # 3.4.1 循环遍历泡泡对象
        for pao in self.paos:
            pao.step()
            if pao.index > 80:
                # 添加炸弹
                self.createBomb(pao)
                # 根据pao的类型恢复宝宝或海海放置泡泡的数量
                if pao.type == 0:
                    self.bao.number += 1
                # 删除泡泡
                self.paos.remove(pao)

        # 3.4.2 循环遍历炸弹对象
        for bomb in self.bombs:
            bomb.step()
            if bomb.index > 40:
                # 判断是否为1,2,6 三种类型
                if self.builderMap[bomb.row][bomb.col] \
                        in [1,2,6]:
                    destroy = Destroy(self.screen,
                                      self.setImg.destroyImgs,
                                      bomb.row,bomb.col)
                    self.destroys.append(destroy)
                # 清空建筑物
                self.builderMap[bomb.row][bomb.col] = 7
                # 删除炸弹
                self.bombs.remove(bomb)

        # 3.4.3 循环遍历销毁对象
        for destroy in self.destroys:
            destroy.step()
            if destroy.index >= 20:
                # 添加道具
                if random.randint(0,20) < 5:
                    prop = Prop(self.screen,
                                self.setImg.propImgs,
                                destroy.row,destroy.col)
                    self.props.append(prop)
                # 删除销毁对象
                self.destroys.remove(destroy)


    '''3.4.1. 创建炸弹'''
    def createBomb(self,obj):
        # 1) 获取当前泡泡所在行列值
        pRow = obj.row
        pCol = obj.col
        # 根据泡泡的type类型判断是哪个主角放置的泡泡
        # 后面的1 后期需要改成 self.hai.power
        power = self.bao.power if obj.type == 0 else 1
        # 2)  中间炸弹
        centerBomb = Bomb(self.screen,
                          self.setImg.bombImgs,
                          pRow,pCol,0)
        self.bombs.append(centerBomb)
        '''3) 根据power循环遍历'''
        for i in range(1,power+1):
            # 3) 上炸弹
            if obj.UP and \
                    self.judgeOutType2(pRow - i, pCol)[0]:
                upBomb = Bomb(self.screen,
                              self.setImg.bombImgs,
                              pRow - i, pCol, 0)
                self.bombs.append(upBomb)
                # 停止延伸
                obj.UP = False
            elif obj.UP and \
                    self.judgeOutType2(pRow - i, pCol)[1]:
                # 停止延伸
                obj.UP = False
            elif obj.UP and \
                    self.judgeOutType2(pRow - i, pCol)[2]:
                # 生成炸弹
                upBomb = Bomb(self.screen,
                              self.setImg.bombImgs,
                              pRow - i, pCol, 0)
                self.bombs.append(upBomb)



            # 4) 下炸弹
            if obj.DOWN and \
                    self.judgeOutType2(pRow + i, pCol)[0]:
                downBomb = Bomb(self.screen,
                                self.setImg.bombImgs,
                                pRow + i, pCol, 0)
                self.bombs.append(downBomb)
                # 停止延伸
                obj.DOWN = False
            elif obj.DOWN and \
                    self.judgeOutType2(pRow + i, pCol)[1]:
                # 停止延伸
                obj.DOWN = False
            elif obj.DOWN and \
                    self.judgeOutType2(pRow + i, pCol)[2]:
                # 生成炸弹
                downBomb = Bomb(self.screen,
                                self.setImg.bombImgs,
                                pRow + i, pCol, 0)
                self.bombs.append(downBomb)


            # 5.左炸弹
            if obj.LEFT and \
                    self.judgeOutType2(pRow, pCol - i)[0]:
                leftBomb = Bomb(self.screen,
                                self.setImg.bombImgs,
                                pRow, pCol - i, 1)
                self.bombs.append(leftBomb)
                # 停止延伸
                obj.LEFT = False
            elif obj.LEFT and \
                    self.judgeOutType2(pRow, pCol - i)[1]:
                # 停止延伸
                obj.LEFT = False
            elif obj.LEFT and \
                    self.judgeOutType2(pRow, pCol - i)[2]:
                leftBomb = Bomb(self.screen,
                                self.setImg.bombImgs,
                                pRow, pCol - i, 1)
                self.bombs.append(leftBomb)


            # 6.右炸弹
            if obj.RIGHT and \
                    self.judgeOutType2(pRow, pCol + i)[0]:
                rightBomb = Bomb(self.screen,
                                 self.setImg.bombImgs,
                                 pRow, pCol + i, 1)
                self.bombs.append(rightBomb)
                # 停止延伸
                obj.RIGHT = False
            elif obj.RIGHT and \
                    self.judgeOutType2(pRow, pCol + i)[1]:
                # 停止延伸
                obj.RIGHT = False
            elif obj.RIGHT and \
                    self.judgeOutType2(pRow, pCol + i)[2]:
                rightBomb = Bomb(self.screen,
                                 self.setImg.bombImgs,
                                 pRow, pCol + i, 1)
                self.bombs.append(rightBomb)


    '''3.4.1.1 判断是否出界以及建筑物类型'''
    def judgeOutType2(self,nextRow,nextCol):
        # 设置返回值
        one = False
        two = False
        three = False

        if 0<= nextRow < 13 and \
            0<= nextCol < 15:
            # 1,2,6(添加炸弹且无延伸)
            # 0,3,4,5(无炸弹无延伸)
            # 7(有炸弹有延伸)
            # 获取建筑物类型
            tp = self.builderMap[nextRow][nextCol]
            # 判断
            if tp in [1,2,6]:
                one = True
            elif tp in [0,3,4,5]:
                two = True
            elif tp in [7]:
                three = True
            return one,two,three
        return one,two,three  # (False,False,False)

    '''第四区域:绘制函数'''
    def paint(self):
        # 4.1 绘制背景图
        self.screen.blit(self.setImg.back,(0,0))
        # 4.2 调用绘制地板图
        self.paintFloor()
        # 4.3 调用绘制建筑物图
        self.paintBuilder()
        # 4.4 绘制宝宝
        self.bao.blitMe()
        # 4.5 绘制泡泡
        self.paintPao()
        # 4.6 绘制炸弹
        self.paintBomb()
        # 4.7 绘制销毁
        self.paintDestroy()
        # 4.8 绘制道具
        self.paintProp()

    '''4.2 绘制地板图函数'''
    def paintFloor(self):
        # 4.2.1 根据floorMap循环遍历绘制地板图
        for row in range(len(self.floorMap)):
            for col in range(len(self.floorMap[row])):
                # 4.2.2 计算x,y坐标
                fx = 25 + 50*col
                fy = 25 + 50*row
                # 4.2.3 获取列表元素值
                num = self.floorMap[row][col]
                # 4.2.4 绘制背景图片
                self.screen.blit(self.setImg.floorImgs[num],
                                 (fx,fy))

    '''4.3 绘制建筑物图函数'''
    def paintBuilder(self):
        # 4.3.1 循环遍历绘制建筑物图
        for row in range(len(self.builderMap)):
            for col in range(len(self.builderMap[row])):
                # 4.3.2 计算坐标值
                bx = 25 + 50 * col
                by = 25 + 50 * row
                # 4.3.3 获取建筑物图纸
                num = self.builderMap[row][col]
                # 4.3.4 判断是否为空表
                if num != 7:
                    self.screen.blit(
                        self.setImg.builderImgs[num],
                        (bx,by))

    '''4.5 绘制泡泡对象'''
    def paintPao(self):
        for p in self.paos:
            p.blitMe()

    '''4.6 绘制炸弹对象'''
    def paintBomb(self):
        for bomb in self.bombs:
            bomb.blitMe()

    '''4.7 绘制销毁对象'''
    def paintDestroy(self):
        for destroy in self.destroys:
            destroy.blitMe()

    '''4.8 绘制道具对象'''
    def paintProp(self):
        for prop in self.props:
            prop.blitMe()

if __name__ == '__main__':
    NexonGame().Menu()


