import sys
import pygame.display

class MyBall():
    '''Region 1: Initialization Area'''
    def __init__(self):
        # 1.1 Create window object
        self.screen = pygame.display.set_mode((800, 600))
        # 1.2 Set the ball's coordinates
        self.x = 100
        self.y = 100
        # 1.3 Set the ball's flight direction
        self.f = 0

    '''Region 2: Main Structure Area'''
    def Menu(self):
        # 2.1 Set the window title
        pygame.display.set_caption("Bouncing Ball")
        # 2.2 Infinite loop
        while True:
            # 2.3 Set background color
            self.screen.fill((255, 255, 255))
            # 2.4 Call business execution function
            self.action()
            # 2.5 Call drawing function
            self.paint()
            # 2.6 Delay to adjust the refresh rate
            pygame.time.delay(5)
            # 2.7 Refresh the screen
            pygame.display.update()

    '''Region 3: Business Execution Area'''
    def action(self):
        # 3.1 Loop through all event listeners
        for event in pygame.event.get():
            # 3.2 Check if the window is closing
            if event.type == pygame.QUIT:
                sys.exit(0)
        '''3.3 Ball Movement'''
        # 3.3.1 Change coordinates based on flight direction
        if self.f == 0:
            self.x += 1
            self.y += 1
        if self.f == 1:
            self.x += 1
            self.y -= 1
        if self.f == 2:
            self.x -= 1
            self.y -= 1
        if self.f == 3:
            self.x -= 1
            self.y += 1
        # 3.2 Modify flight direction based on coordinates
        # Bottom boundary
        if self.y > 600 - 15:
            if self.f == 0:
                self.f = 1
            else:
                self.f = 2
        # Right boundary
        if self.x > 800 - 15:
            if self.f == 1:
                self.f = 2
            else:
                self.f = 3
        # Top boundary
        if self.y < 15:
            if self.f == 2:
                self.f = 3
            else:
                self.f = 0
        # Left boundary
        if self.x < 15:
            if self.f == 3:
                self.f = 0
            else:
                self.f = 1

    '''Region 4: Drawing Area'''
    def paint(self):
        # 4.1 Draw the ball
        pygame.draw.circle(self.screen,
                           (0, 0, 0),
                           (self.x, self.y), 15, 0)

if __name__ == '__main__':
    MyBall().Menu()
