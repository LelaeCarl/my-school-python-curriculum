import sys
import pygame.display


class MyGuess():
    '''Region 1: Initialization Area'''
    def __init__(self):
        # 1.1 Set window object
        self.screen = pygame.display.set_mode((1000, 800))
        # 1.2 Answer list
        self.answerList = []
        # 1.3 Title list
        self.titleList = []
        # 1.4 Poster list
        self.iconList = []
        # 1.5 Options list
        self.optionList = []
        # 1.6 Call data parsing function
        self.getData()
        # 1.7 Set question number
        self.num = 0
        # 1.8 Set user-selected answers
        self.userAnswer = []

    '''1.6 Function to parse data and save it'''
    def getData(self):
        # 1.6.1 Read all data from the file
        file = open("guess.txt", "r", encoding="utf-8")
        contentList = file.readlines()
        file.close()
        # 1.6.2 Loop through all the lines read
        # answer:box of treasure#icon:movie_ygbh#title:Comedy blockbuster with spoof style#options:line,talk,fly,person,laugh,tian,yellow,work,big,super,legend,extra,treasure,red,team,sky,wall,box
        for line in contentList:
            # 1.6.3 Split the line into four parts using '#'
            # Replace newline characters
            line = line.replace("\n", "")
            lineList = line.split("#")
            # 1.6.4 Loop through the four parts
            for data in lineList:
                # 1.6.5 Split data using ':'
                dt = data.split(":")
                # 1.6.6 Check if it's an answer
                if dt[0] == "answer":
                    self.answerList.append(dt[1])
                elif dt[0] == "icon":
                    self.iconList.append(dt[1])
                elif dt[0] == 'title':
                    self.titleList.append(dt[1])
                elif dt[0] == "options":
                    # Split options three times
                    options = dt[1].split(",")
                    self.optionList.append(options)

    '''Region 2: Main Structure'''
    def Menu(self):
        # 2.1 Set window title
        pygame.display.set_caption("Super Guessing Game")
        # 2.2 Infinite loop
        while True:
            # 2.3 Fill the screen with color
            self.screen.fill((255, 255, 255))
            # 2.4 Call the business execution function
            self.action()
            # 2.5 Call the drawing function
            self.paint()
            # 2.6 Refresh the screen
            pygame.display.update()

    '''Region 3: Business Execution Function'''
    def action(self):
        # 3.1 Loop through all event listeners
        for event in pygame.event.get():
            # 3.2 Check if the window is closed
            if event.type == pygame.QUIT:
                sys.exit(0)
            # 3.3 Check mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 3.3.1 Get mouse coordinates
                mouseX, mouseY = pygame.mouse.get_pos()
                # 3.3.2 Check if left mouse button is clicked
                leftFlag = pygame.mouse.get_pressed()[0]
                '''3.3.3 Option box click check'''
                # Get current options content
                options = self.optionList[self.num]
                # The number of answer boxes cannot exceed the length of the correct answer
                awLen = len(self.answerList[self.num])
                # Calculate the starting x-coordinate of the first option box
                opX = (1000 - 50 * 10 - 20 * 9) / 2
                if opX < mouseX < 1000 - opX and \
                        550 < mouseY < 670 and leftFlag and len(self.userAnswer) < awLen:
                    # Calculate the selected column index
                    opRow = int((mouseX - opX) // 70)
                    # Check if it's in the second row (Y >= 620)
                    if 620 <= mouseY < 670:
                        opRow += 10
                    # Add the option to the user's answer
                    self.userAnswer.append(options[opRow])
                '''3.3.4 Answer box click event'''
                awLen = len(self.answerList[self.num])
                answerX = (1000 - 50 * awLen - 20 * (awLen - 1)) / 2
                if answerX < mouseX < 1000 - answerX and \
                        480 <= mouseY < 480 + 50 and leftFlag:
                    # Calculate the selected column index
                    col = int((mouseX - answerX) // 70)
                    # Remove selected option from user answer
                    if 0 <= col < len(self.userAnswer):
                        del self.userAnswer[col]
        '''3.4 Check if the answer is correct'''
        if len(self.answerList[self.num]) == len(self.userAnswer):
            # 3.4.1 Get the correct answer as a string
            answer = self.answerList[self.num]
            # 3.4.2 Get the user's answer as a string
            userAw = "".join(self.userAnswer)
            # 3.4.3 Compare answers
            if answer == userAw:
                # If correct, move to the next question
                self.num += 1 if self.num < 9 else 0
                self.userAnswer.clear()  # Clear user answers

    '''Region 4: Drawing Function'''
    def paint(self):
        # 4.1 Draw the question number
        pygame.font.init()
        ft = pygame.font.Font("simkai.ttf", 28)
        ftNum = ft.render(f"Question {self.num + 1}", True, (255, 0, 0))
        numX = (1000 - 30 * 3) / 2
        self.screen.blit(ftNum, (numX, 20))

        # 4.2 Draw the title
        ftTitle = ft.render(f"{self.titleList[self.num]}", True, (255, 0, 0))
        titleX = (1000 - 30 * len(self.titleList[self.num])) / 2
        self.screen.blit(ftTitle, (titleX, 70))

        # 4.3 Draw the poster
        # Image\movie_ygbh.png
        iconPath = f"Image/{self.iconList[self.num]}.png"
        icon = pygame.image.load(iconPath)
        img = pygame.transform.scale(icon, (320, 350))
        iconX = (1000 - 320) / 2
        self.screen.blit(img, (iconX, 120))

        # 4.4 Draw the answer boxes
        for i in range(len(self.answerList[self.num])):
            # Get the answer
            answer = self.answerList[self.num]
            # Calculate the x-coordinate of the first answer box
            answerX = (1000 - 50 * len(answer) - 20 * (len(answer) - 1)) / 2
            # Calculate the x-coordinate of each answer box
            aX = answerX + i * (50 + 20)
            # Draw the answer box
            pygame.draw.rect(self.screen, (255, 255, 0), (aX, 480, 50, 50), 0)

        # 4.5 Draw the option boxes
        for i in range(20):
            # Calculate the starting x-coordinate
            opX = (1000 - 50 * 10 - 20 * 9) / 2
            # Calculate the x-coordinate for each option box
            if i < 10:
                optionX = opX + i * 70
                optionY = 550
            else:
                optionX = opX + (i - 10) * 70
                optionY = 620
            pygame.draw.rect(self.screen, (255, 0, 0), (optionX, optionY, 50, 50), 0)
            '''Draw text in option boxes'''
            op = self.optionList[self.num][i]
            ftOption = ft.render(op, True, (255, 255, 255))
            self.screen.blit(ftOption, (optionX + 7, optionY + 7))

        # 4.6 Draw the answer content
        for i in range(len(self.userAnswer)):
            # 1) Get the length of the answer
            awLen = len(self.answerList[self.num])
            # 2) Calculate the x-coordinate of the first answer box
            answerX = (1000 - 50 * awLen - 20 * (awLen - 1)) / 2
            # 3) Calculate the x-coordinate for each answer text
            optionX = answerX + i * 70
            # 4) Set the content
            ftAnaswer = ft.render(f"{self.userAnswer[i]}", True, (255, 0, 0))
            # 5) Draw the answer text
            self.screen.blit(ftAnaswer, (optionX + 7, 480 + 7))


if __name__ == '__main__':
    MyGuess().Menu()
