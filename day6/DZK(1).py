import random
import sys
import pygame.display

class DZK():
    '''Region 1: Initialization Area'''
    def __init__(self):
        # 1.1 Window object
        self.screen = pygame.display.set_mode((800, 600))
        # 1.2 Paddle-related parameters
        self.banX = 100
        self.banY = 500
        self.banW = 550
        self.banH = 30
        # 1.3 Ball's coordinates and flight direction
        self.x = 100
        self.y = 100
        self.f = 0
        # 1.4 Set ball color
        self.color = self.getColor()
        # 1.5 Set score
        self.score = 0
        # 1.6 Set speed
        self.speed = 10

    def getColor(self):
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        return R, G, B

    '''Region 2: Main Structure Area'''
    def Menu(self):
        # 2.1 Set window title
        pygame.display.set_caption("Brick Breaker")
        # 2.2 Infinite loop
        while True:
            # 2.3 Fill background color
            self.screen.fill((255, 255, 255))
            # 2.4 Call business function
            self.action()
            # 2.5 Call drawing function
            self.paint()
            # 2.6 Set delay
            pygame.time.delay(self.speed)
            # 2.7 Refresh screen
            pygame.display.update()

    '''Region 3: Business Execution Function'''
    def action(self):
        # 3.1 Loop through all event listeners
        for event in pygame.event.get():
            # 3.2 Check if window is closing
            if event.type == pygame.QUIT:
                sys.exit(0)
            '''3.3 Mouse event listener'''
            if event.type == pygame.MOUSEMOTION:
                # 3.3.1 Get mouse coordinates
                mx, my = pygame.mouse.get_pos()
                # 3.3.2 Modify banX based on mouse's x-coordinate
                if self.banW / 2 < mx < 800 - self.banW / 2:  # Inside window
                    self.banX = mx - self.banW / 2
                elif mx < self.banW / 2:  # Exceeds left boundary
                    self.banX = 0
                elif self.banX + self.banW / 2 < mx:  # Exceeds right boundary
                    self.banX = 800 - self.banW
        '''3.4 Ball movement'''
        # 3.4.1 Change coordinates based on flight direction
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
        # 3.4.2 Modify flight direction based on coordinates
        '''Ball and paddle collision detection'''
        if self.banX <= self.x - 15 and \
                self.x + 15 <= self.banX + self.banW and \
                self.y >= self.banY - 15:
            self.score += 5  # Add points
            self.banW -= 5 if self.banW > 50 else 0  # Adjust paddle size
            if self.f == 0:
                self.f = 1
            else:
                self.f = 2
        # Bottom boundary
        if self.y > 600 - 15:
            self.score -= 5  # Deduct points
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

        '''3.5 Modify score'''
        if 0 <= self.score < 100:
            self.speed = 10
        elif 100 <= self.score < 200:
            self.speed = 5
        elif 200 <= self.score < 300:
            self.speed = 3
        elif 300 <= self.score:
            self.speed = 1

    '''Region 4: Drawing Area'''
    def paint(self):
        # 4.1 Draw paddle (x, y, w, h) where x, y are the top-left corner coordinates of the rectangle
        pygame.draw.rect(self.screen,
                         (255, 0, 0),
                         (self.banX, self.banY,
                          self.banW, self.banH), 0)
        # 4.2 Draw ball
        pygame.draw.circle(self.screen,
                           self.color,
                           (self.x, self.y), 15, 0)
        # 4.3 Display score
        pygame.font.init()
        ft = pygame.font.Font("simkai.ttf", 28)
        ftStr = ft.render("score:%d" % self.score,
                          True, (255, 0, 0))
        self.screen.blit(ftStr, (100, 100))


if __name__ == '__main__':
    DZK().Menu()
