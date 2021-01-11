import pygame

BLACK = (0, 0, 0)
padWidth = 480
padHeight = 640

def runGame():
    global gamepad, clock

    doneFlag = False
    while not doneFlag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                doneFlag = True

        gamepad.fill(BLACK)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def initGame():
    global gamepad, clock

    pygame.init()
    gamepad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('MyGalaga')
    clock = pygame.time.Clock()

initGame()
runGame()