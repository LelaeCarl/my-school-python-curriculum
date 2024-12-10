'''
ZBT
需求如下:
    1.点击左侧/上方的不同点  同时出现两个红色框
    2.点击区域将   x,y,w,h 可以存放到.txt中也可以放在列表
    3.当所有的不同点完成后自动跳转到 第二关
需求如下:
    1.11套tomcat的动画实现
    录制视频发送群里面
    10:00 上课
'''

import sys
import pygame
import os

class MyToms():
    '''Initialization Area'''
    def __init__(self):
        # 1.1 Set up window object
        self.screen = pygame.display.set_mode((320, 512))
        # 1.2 Set background image for the first level
        self.back = pygame.image.load("Animations/Eat/eat_00.jpg")
        # 1.3 Set image storage path for animations
        self.imgList = []
        # 1.4 Set image index
        self.index = 0
        # 1.5 Set total number of images
        self.count = -1
        # 1.6 Set images for interacting with Tomcat (eating and drinking)
        self.eatImg = pygame.image.load("Buttons/eat.png")
        self.drinkImg = pygame.image.load("Buttons/drink.png")
        # 1.7 List to store click coordinates
        self.click_coords = []
        # 1.8 List to store predefined points to click
        self.difference_points = [(50, 100), (200, 300), (150, 400), (100, 50)]  # Example points
        # 1.9 Counter for the number of points clicked
        self.clicked_points = 0

    '''Main structure for game'''
    def Menu(self):
        # 2.1 Set window title
        pygame.display.set_caption("Tomcat Game")
        # 2.2 Infinite loop to keep the game running
        while True:
            # 2.3 Call the event handling function
            self.action()
            # 2.4 Call the drawing function
            self.paint()
            # 2.5 Refresh the screen
            pygame.display.update()

    '''Event handling function'''
    def action(self):
        # 3.1 Loop through all events
        for event in pygame.event.get():
            # 3.2 Check for quit event
            if event.type == pygame.QUIT:
                sys.exit(0)
            # 3.3 Check for mouse click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 3.3.1 Get the mouse coordinates
                mouseX, mouseY = pygame.mouse.get_pos()
                # 3.3.2 Check if the left mouse button is clicked
                leftFlag = pygame.mouse.get_pressed()[0]
                # 3.3.3 If the mouse click is within the clickable area, create red boxes
                for point in self.difference_points:
                    px, py = point
                    if (px - 20 < mouseX < px + 20) and (py - 20 < mouseY < py + 20) and leftFlag:
                        print(f"Clicked on point: {point}")  # Debugging output
                        # Add red box coordinates to the list
                        self.click_coords.append((px - 20, py - 20, 40, 40))
                        self.clicked_points += 1
                        # Store the coordinates in a text file (optional)
                        self.save_to_file(px - 20, py - 20, 40, 40)
                        break
                # 3.3.4 If all points are clicked, transition to the next level
                if self.clicked_points == len(self.difference_points):
                    self.next_level()

    '''Save clicked coordinates to a file'''
    def save_to_file(self, x, y, w, h):
        with open('clicked_points.txt', 'a') as file:
            file.write(f'{x},{y},{w},{h}\n')
            print(f"Saved to file: {x},{y},{w},{h}")  # Debugging output

    '''Transition to the next level (second level)'''
    def next_level(self):
        print("All points clicked! Moving to the second level...")
        self.start_second_level()

    '''Start the second level'''
    def start_second_level(self):
        # Second level animation logic goes here.
        print("Second level is now active. Start Tomcat animations.")
        self.index = 0
        self.count = 40
        self.updateImg("eat")
        # Add the rest of the logic for animations

    '''Update image paths for animations'''
    def updateImg(self, name):
        for i in range(self.count):
            self.imgList.append(f"Animations/{name}/{name}_{i:02d}.jpg")
        print(f"Loaded {len(self.imgList)} images for animation.")  # Debugging output

    '''Drawing function'''
    def paint(self):
        # 4.1 Draw the background image
        img = pygame.transform.scale(self.back, (320, 512))
        self.screen.blit(img, (0, 0))
        # 4.2 Draw the "Eat" and "Drink" images
        self.screen.blit(self.eatImg, (30, 300))
        self.screen.blit(self.drinkImg, (30, 380))
        # 4.3 Draw the red boxes on the screen
        for x, y, w, h in self.click_coords:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, w, h), 2)  # Red border

if __name__ == '__main__':
    pygame.init()  # Make sure to initialize pygame
    MyToms().Menu()

