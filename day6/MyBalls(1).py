import random
import sys
import pygame.display

class MyBall():
    '''Region 1: Initialization Area'''
    def __init__(self):
        # 1.1 Create window object
        self.screen = pygame.display.set_mode((800, 600))
        # 1.2 Set ball coordinates
        self.xx = [random.randint(0, 800) for i in range(5)]
        self.yy = [random.randint(0, 600) for i in range(5)]
        # 1.3 Set ball flight directions
        self.ff = [random.randint(0, 3) for i in range(5)]
        # 1.4 Set ball colors
        self.colors = [self.getColor() for i in range(5)]
        # 1.5 Set score
        self.score = 0
        # 1.6 Set speed
        self.speed = 10

    '''Get random color'''
    def getColor(self):
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        return R, G, B

    '''Region 2: Main Structure Area'''
    def Menu(self):
        # 2.1 Set window title
        pygame.display.set_caption("Bouncing Balls")
        # 2.2 Infinite loop
        while True:
            # 2.3 Set background color
            self.screen.fill((255, 255, 255))
            # 2.4 Call business execution function
            self.action()
            # 2.5 Call drawing function
            self.paint()
            # 2.6 Delay to adjust refresh rate
            pygame.time.delay(self.speed)
            # 2.7 Refresh screen
            pygame.display.update()

    '''Region 3: Business Execution Area'''
    def action(self):
        # 3.1 Loop through all event listeners
        for event in pygame.event.get():
            # 3.2 Check if the window is closing
            if event.type == pygame.QUIT:
                sys.exit(0)

        # 3.4 Adjust speed based on score
        if 0 <= self.score < 100:
            self.speed = 10
        elif 100 <= self.score < 200:
            self.speed = 8
        elif 200 <= self.score < 300:
            self.speed = 5
        elif 300 <= self.score:
            self.speed = 1

        '''3.3 Ball movement'''
        for i in range(5):
            # 3.3.1 Modify coordinates based on flight direction
            if self.ff[i] == 0:
                self.xx[i] += 1
                self.yy[i] += 1
            if self.ff[i] == 1:
                self.xx[i] += 1
                self.yy[i] -= 1
            if self.ff[i] == 2:
                self.xx[i] -= 1
                self.yy[i] -= 1
            if self.ff[i] == 3:
                self.xx[i] -= 1
                self.yy[i] += 1

            # 3.2 Modify flight direction based on coordinates
            # Bottom boundary
            if self.yy[i] > 600 - 15:
                self.colors[i] = self.getColor()  # Change color
                self.score += 5  # Add points
                if self.ff[i] == 0:
                    self.ff[i] = 1
                else:
                    self.ff[i] = 2
            # Right boundary
            if self.xx[i] > 800 - 15:
                self.colors[i] = self.getColor()  # Change color
                self.score += 5  # Add points
                if self.ff[i] == 1:
                    self.ff[i] = 2
                else:
                    self.ff[i] = 3
            # Top boundary
            if self.yy[i] < 15:
                self.colors[i] = self.getColor()  # Change color
                self.score += 5  # Add points
                if self.ff[i] == 2:
                    self.ff[i] = 3
                else:
                    self.ff[i] = 0
            # Left boundary
            if self.xx[i] < 15:
                self.colors[i] = self.getColor()  # Change color
                self.score += 5  # Add points
                if self.ff[i] == 3:
                    self.ff[i] = 0
                else:
                    self.ff[i] = 1

    '''Region 4: Drawing Area'''
    def paint(self):
        # 4.2 Draw score
        pygame.font.init()
        ft = pygame.font.Font("simkai.ttf", 28)
        ftStr = ft.render("score:%d" % self.score,
                          True, (255, 0, 0))
        self.screen.blit(ftStr, (100, 100))

        # 4.1 Draw balls
        for i in range(5):
            pygame.draw.circle(self.screen,
                               self.colors[i],
                               (self.xx[i], self.yy[i]), 15, 0)

if __name__ == '__main__':
    MyBall().Menu()
