'''
08 - MyStar
1. Main Function Logic
2. Font Setup
   2.1 Path for fonts: C:\Windows\Fonts (Chinese font files)
   2.2 Store fonts in day05 directory
3. Generate 100 Stars
   3.1 Randomly set xx and yy coordinates between 0-800
   3.2 Randomly generate 100 stars
4. Animation
   4.1 Gradual movement animation
5. Dynamic Features
   5.1 Gradual movement (3.3: Modify star positions)
   5.2 Dynamic random colors
6. Image Rendering
   6.1 Load image resources (4.5)
7. Requirements
   7.1 Use day05 fonts for Chinese
   7.2 Display an image (assign it to self.img)
   7.3 Display stars dynamically
'''

import sys
import random
import pygame

class MyStar():
    '''Initialize Area'''
    def __init__(self):
        # 1. Set up main window (800x600)
        self.screen = pygame.display.set_mode((800, 600))
        # 2. Generate star coordinates
        self.xx = [random.randint(0, 800) for i in range(100)]
        self.yy = [random.randint(0, 600) for i in range(100)]
        # 3. Load resources
        self.img = pygame.image.load("IMG_7711.JPG")

    '''Menu Area'''
    def Menu(self):
        # 1. Set window title
        pygame.display.set_caption("Fire Star!")
        # 2. Main loop
        while True:
            # 2.3 Fill background color
            self.screen.fill((0, 0, 0))
            # 2.4 Invoke response logic
            self.action()
            # 2.5 Invoke rendering logic
            self.paint()
            # Pause for 10 ms
            pygame.time.delay(10)
            # 2.6 Refresh window
            pygame.display.update()

    '''Perform Action'''
    def action(self):
        # 3.1 Detect system events
        for event in pygame.event.get():
            # 3.2 If the close button is clicked
            if event.type == pygame.QUIT:
                sys.exit(0)  # 0 indicates normal exit
        # 3.3 Gradually move stars
        for i in range(0, 100):
            self.xx[i] += 1
            self.yy[i] += 1
            if self.xx[i] > 800:
                self.xx[i] = 0
            if self.yy[i] > 600:
                self.yy[i] = 0

    '''Render Image'''
    def paint(self):
        # 4.5 Draw stars
        # self.screen draws circles on top (255,255,255) = white color
        # pygame.draw.circle(surface, color, (x, y), radius, width)
        for i in range(0, 100):
            pygame.draw.circle(self.screen,
                               (0, 0, 0),
                               (self.xx[i], self.yy[i]), 5)
        # 4.6 Display image resources (scale to 100x100)
        ig = pygame.transform.scale(self.img, (100, 100))
        self.screen.blit(ig, (200, 200))
        # 4.1 Display text
        pygame.font.init()
        # 4.2 Set text font style
        ft = pygame.font.Font("simkai.ttf", 28)
        for i in range(100):
            # 4.3 Randomly generate RGB colors
            R = random.randint(0, 255)
            G = random.randint(0, 255)
            B = random.randint(0, 255)
            ftStr = ft.render("*", True, (R, G, B))
            # Display text on screen at (xx, yy) coordinates
            self.screen.blit(ftStr, (self.xx[i], self.yy[i]))

if __name__ == "__main__":
    # Create instance of MyStar and run menu
    star_game = MyStar()
    star_game.Menu()
