import random
import sys

import pygame.display


class MyWord():
    '''Region 1: Initialization Area'''
    def __init__(self):
        # 1.1 Set window object
        self.screen = pygame.display.set_mode((800, 600))
        # 1.2 Set coordinates and letter list
        self.xx = [random.randint(0, 800) for i in range(10)]
        self.yy = [-random.randint(0, 600) for i in range(10)]
        # ASCII values for characters: A = 65, Z = 90, a = 97
        self.words = [random.randint(0, 25) + 65 for i in range(10)]


    '''Region 2: Main Structure Area'''
    def Menu(self):
        # 2.1 Set window title
        pygame.display.set_caption("Typing Game")
        # 2.2 Infinite loop
        while True:
            # 2.3 Fill background color
            self.screen.fill((255, 255, 255))
            # 2.4 Call business execution function
            self.action()
            # 2.5 Call drawing function
            self.paint()
            # 2.6 Set delay
            pygame.time.delay(10)
            # 2.7 Refresh the screen
            pygame.display.update()

    '''Region 3: Business Execution Function'''
    def action(self):
        # 3.1 Loop through all event listeners
        for event in pygame.event.get():
            # 3.2 Check if window is closed
            if event.type == pygame.QUIT:
                sys.exit(0)
            # 3.4 Check keyboard events
            if event.type == pygame.KEYDOWN:
                # 3.4.1 Loop through each letter
                for i in range(10):
                    # 3.4.2 Check if the pressed key matches the letter
                    if event.key == self.words[i] + 32 \
                            and self.yy[i] > 0:
                        # 3.4.3 Replace the current letter
                        self.words[i] = random.randint(0, 25) + 65
                        self.xx[i] = random.randint(0, 800 - 30)
                        self.yy[i] = -random.randint(0, 600)
                        break

        '''3.3 Modify y-coordinate value'''
        for i in range(10):
            self.yy[i] += 1
            if self.yy[i] > 600:
                self.yy[i] = 0

    '''Region 4: Drawing Function'''
    def paint(self):
        # 4.1 Draw letters
        pygame.font.init()
        ft = pygame.font.Font("simkai.ttf", 28)
        for i in range(10):
            ftStr = ft.render("%c" % chr(self.words[i]),
                              True, (255, 0, 0))
            self.screen.blit(ftStr, (self.xx[i], self.yy[i]))


if __name__ == '__main__':
    MyWord().Menu()
