import sys
import pygame.display


class MyToms():
    '''Region 1: Initialization Area'''
    def __init__(self):
        # 1.1 Set window object
        self.screen = pygame.display.set_mode((320, 512))
        # 1.2 Set background image
        self.back = pygame.image.load("Animations/Eat/eat_00.jpg")
        # 1.3 Set image storage path
        self.imgList = []
        # 1.4 Set image index
        self.index = 0
        # 1.5 Set total number of images
        self.count = -1
        # 1.6 Set image for eating the bird
        self.eatImg = pygame.image.load("Buttons/eat.png")
        # 1.7 Set image for drinking milk
        self.drinkImg = pygame.image.load("Buttons/drink.png")

    '''Region 2: Main Structure Area'''
    def Menu(self):
        # 2.1 Set window title
        pygame.display.set_caption("Tomcat")
        # 2.2 Infinite loop
        while True:
            # 2.3 Call business execution function
            self.action()
            # 2.4 Call drawing function
            self.paint()
            # 2.5 Refresh the screen
            pygame.display.update()

    '''Region 3: Business Execution Function'''
    def action(self):
        # 3.1 Loop through all event listeners
        for event in pygame.event.get():
            # 3.2 Check for quit event
            if event.type == pygame.QUIT:
                sys.exit(0)
            # 3.3 Check for mouse click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 3.3.1 Get mouse coordinates
                mouseX, mouseY = pygame.mouse.get_pos()
                # 3.3.2 Check for left mouse button click
                leftFlag = pygame.mouse.get_pressed()[0]
                # 3.3.3 Eating bird animation
                if 30 < mouseX < 30 + 60 and \
                        300 < mouseY < 300 + 60 and \
                        leftFlag:
                    # Set total image count
                    self.count = 40
                    self.updateImg("eat")
                # 3.3.4 Drinking milk animation
                if 30 < mouseX < 30 + 60 and \
                        380 < mouseY < 380 + 60 and \
                        leftFlag:
                    # Set total image count
                    self.count = 81
                    self.updateImg("drink")

        '''3.4 Animation effect display'''
        if self.count * 10 > self.index:
            ix = int(self.index / 10 % len(self.imgList))
            self.back = pygame.image.load(self.imgList[ix])
            self.index += 1
        else:
            self.count = -1
            self.index = 0
            self.imgList.clear()  # Clear image list

    '''3.3 Update image paths'''
    def updateImg(self, name):
        for i in range(self.count):
            self.imgList.append(
                "Animations/%s/%s_%02d.jpg" % (name, name, i))

    '''Region 4: Drawing Function'''
    def paint(self):
        # 4.1 Draw the background image
        img = pygame.transform.scale(self.back, (320, 512))
        self.screen.blit(img, (0, 0))
        # 4.2 Draw the eat bird image
        self.screen.blit(self.eatImg, (30, 300))
        # 4.3 Draw the drink milk image
        self.screen.blit(self.drinkImg, (30, 380))


if __name__ == '__main__':
    MyToms().Menu()
