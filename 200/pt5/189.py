import pygame

BLACK = (0, 0, 0)
padWidth = 480
padHeight = 640
fighterWidth = 36
fighterHeight = 38

def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x, y))

def runGame():
    global gamepad, clock,fighter

    x = padWidth * 0.45
    y = padHeight * 0.9
    xChange = 0

    ongame = False
    while not ongame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ongame = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange -= 5

                elif event.key == pygame.K_RIGHT:
                    xChange += 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xChange = 0

        gamepad.fill(BLACK)

        x += xChange
        if x < 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth

        drawObject(fighter, x, y)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def initGame():
    global gamepad, clock, fighter

    pygame.init()
    gamepad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('MyGalaga')
    fighter = pygame.image.load('fighter.png')
    clock = pygame.time.Clock()

initGame()
runGame()