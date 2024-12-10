import sys

import pygame.display

class MyTom():
    '''Region 1: Initialization Area'''
    def __init__(self):
        # 1.1 Set window object
        self.screen = pygame.display.set_mode((320, 512))
        # 1.2 Set background image
        self.back = pygame.image.load("Animations/Eat/eat_00.jpg")
        # 1.3 Set animation list for eating birds
        # Animations/Eat/eat_00.jpg
        # Animations/Eat/eat_39.jpg
        self.eatList = ["Animations/Eat/eat_%02d.jpg" % i for i in range(0, 40)]
        # 1.4 Set count value
        self.index = 0
        # 1.5 Set eat bird image
        self.eatImg = pygame.image.load("Buttons/eat.png")
        # 1.6 Set total count
        self.count = -1

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
            # 2.5 Set delay
            # pygame.time.delay(10)
            # 2.6 Refresh screen
            pygame.display.update()

    '''Region 3: Business Execution Function'''
    def action(self):
        # 3.1 Loop through all event listeners
        for event in pygame.event.get():
            # 3.2 Check if window is closed
            if event.type == pygame.QUIT:
                sys.exit(0)
            # 3.4 Check mouse event
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 3.4.1 Get mouse coordinates
                mouseX, mouseY = pygame.mouse.get_pos()
                # 3.4.2 Get mouse click event (single click, double click, right click)
                leftFlag = pygame.mouse.get_pressed()[0]
                # 3.4.3 Check if the "eat bird" image is clicked
                if 30 < mouseX < 30 + 60 and \
                        300 < mouseY < 300 + 60 and \
                        leftFlag:
                    # Modify total count value
                    self.count = 40

        '''3.3 Animation effect implementation'''
        # 3.3.1 Normal animation  count -1  index 0
        # count 40 index 400
        if self.count * 10 > self.index:
            ix = int(self.index / 10 % len(self.eatList))
            self.back = pygame.image.load(self.eatList[ix])
            self.index += 1
        else:
            self.count = -1
            self.index = 0

    '''Region 4: Drawing Function'''
    def paint(self):
        # 4.1 Draw background image
        img = pygame.transform.scale(self.back, (320, 512))
        self.screen.blit(img, (0, 0))
        # 4.2 Draw "eat bird" image
        self.screen.blit(self.eatImg, (30, 300))

        pygame.draw.rect(self.screen, (255, 0, 0),
                         (80, 100, 180, 150), 5)

if __name__ == '__main__':
    MyTom().Menu()
