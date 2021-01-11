import pygame
import random

BLACK = (0, 0, 0)
padWidth = 480
padHeight = 640
fightWidth = 36
fightHeight = 38
enemyWidth = 26
enemyHeight = 20

def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj,(x, y))

def runGame():
    global gamepad, clock, fighter, enemy, bullet

    bulletXY = []
    x = padWidth * 0.45
    y = padHeight * 0.9
    xChange = 0
    enemyX = random.randrange(0, padWidth - enemyWidth)
    enemyY = 0
    enemySpeed = 3

    doneFlag = False
    while not doneFlag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                doneFlag = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange -= 5

                elif event.key == pygame.K_RIGHT:
                    xChange += 5

                elif event.key == pygame.K_LCTRL:
                    if len(bulletXY) < 2:
                        bulletX = x + fightWidth/2
                        bulletY = y - fightHeight
                        bulletXY.append([bulletX, bulletY])

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xChange = 0

        gamepad.fill(BLACK)

        x += xChange
        if x < 0:
            x = 0
        elif x > padWidth - fightWidth:
            x = padWidth - fightWidth

        drawObject(fighter, x, y)

        if len(bulletXY) != 0:
            for i, bxy in enumerate(bulletXY):
                bxy[1] -= 10
                bulletXY[i][1] = bxy[1]

            if bxy[1] <= 0:
                try:
                    bulletXY.remove(bxy)
                except:
                    pass

        if len(bulletXY) != 0:
            for bx, by in bulletXY:
                drawObject(bullet, bx, by)

        enemyY += enemySpeed
        if enemyY > padHeight:
            enemyY = 0
            enemyX = random.randrange(0, padWidth - enemyWidth)

        drawObject(enemy, enemyX, enemyY)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def initGame():
    global gamepad, clock, fighter, enemy, bullet

    pygame.init()
    gamepad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('MyGalaga')
    fighter = pygame.image.load('fighter.png')
    enemy = pygame.image.load('enemy.png')
    bullet = pygame.image.load('bullet.png')
    clock = pygame.time.Clock()

initGame()
runGame()