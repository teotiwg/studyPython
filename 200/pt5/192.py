import pygame
import random
from time import sleep

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255,255,255)
padWidth = 480
padHeight = 640
fightWidth = 36
fightHeight = 38
enemyWidth = 26
enemyHeight = 20

def drawScore(count):
    global gamepad
    font = pygame.font.SysFont(None, 20)
    text = font.render('Enemy Kills: ' + str(count), True, WHITE)
    gamepad.blit(text, (0,0))

def drawPassed(count):
    global gamepad
    font = pygame.font.SysFont(None, 20)
    text = font.render('Enemy Passed: ' + str(count), True, RED)
    gamepad.blit(text, (360, 0))

def dispMessage(text):
    global gamepad
    textfont = pygame.font.Font('freesansbold.ttf', 80)
    text = textfont.render(text, True, RED)
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamepad.blit(text, textpos)
    pygame.display.update()
    sleep(2)
    runGame()

def crash():
    global gamepad
    dispMessage('Crashed!')

def gameover():
    global gamepad
    dispMessage('Game Over')

def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x,y))

def runGame():
    global gamepad, clock, fighter, enemy, bullet

    isShot = False
    shotCount = 0
    enemyPassed = 0

    bulletXY = []

    x = padWidth * 0.45
    y = padHeight * 0.9
    xChange = 0

    enemyX = random.randrange(0, padWidth - enemyWidth)
    enemyY = 0
    enemySpeed = 3

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
        elif x > padWidth -fightWidth:
            x = padWidth - fightWidth

        if y < enemyY + enemyHeight:
            if (enemyX >x and enemyX < x + fightWidth) or (enemyX + enemyWidth > x and enemyX + enemyWidth < x + fightWidth):
                crash()

        drawObject(fighter, x, y)

        if len(bulletXY) != 0:
            for i, bxy in enumerate(bulletXY):
                bxy[1] -= 10
                bulletXY[i][1] = bxy[1]

                if bxy[1] < enemyY:
                    if bxy[0] > enemyX and bxy[0] < enemyX + enemyWidth:
                        bulletXY.remove(bxy)
                        isShot = True
                        shotCount += 1

                if bxy[1] <= 0:
                    try:
                        bulletXY.remove(bxy)
                    except:
                        pass

        if len(bulletXY) != 0:
            for bx, by in bulletXY:
                drawObject(bullet, bx,by)

        drawScore(shotCount)

        enemyY += enemySpeed

        if enemyY > padHeight:
            enemyY = 0
            enemyX = random.randrange(0, padWidth - enemyWidth)
            enemyPassed += 1

        if enemyPassed == 3:
            gameover()

        drawPassed(enemyPassed)

        if isShot:
            enemySpeed += 1
            if enemySpeed >= 10:
                enemySpeed = 10

            enemyX = random.randrange(0, padWidth - enemyWidth)
            enemyY = 0
            isShot = False

        drawObject(enemy, enemyX, enemyY)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def initGame():
    global gamepad, clock, fighter,enemy, bullet

    pygame.init()
    gamepad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('MyGALAGA')
    fighter = pygame.image.load('fighter.png')
    enemy = pygame.image.load('enemy.png')
    bullet = pygame.image.load('bullet.png')
    clock = pygame.time.Clock()

initGame()
runGame()