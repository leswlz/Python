import pygame

pygame.init()
win = pygame.display.set_mode((480, 480))

pygame.display.set_caption("Game")

walkRight = [pygame.image.load('right_1.gif'), pygame.image.load('right_2.gif'),
pygame.image.load('right_3.gif'), pygame.image.load('right_4.gif'),
pygame.image.load('right_5.gif'), pygame.image.load('right_6.gif'),
pygame.image.load('right_7.gif'), pygame.image.load('right_8.gif')]

waltLeft = [pygame.image.load('left_1.gif'), pygame.image.load('left_2.gif'),
pygame.image.load('left_3.gif'), pygame.image.load('left_4.gif'),
pygame.image.load('left_5.gif'), pygame.image.load('left_6.gif'),
pygame.image.load('left_7.gif'), pygame.image.load('left_8.gif')]

playerStand = pygame.image.load('idle.gif')
bg = pygame.image.load('bg.png')

clock = pygame.time.Clock()

x = 50
y = 385
widht = 51
height = 63
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0
lastMove = "right"

class shot():
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.velocity = 8 * direction

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

def drawWindow():
    global animCount
    win.blit(bg, (0,0))

    if animCount + 1 >= 40:
        animCount = 0

    if left:
        win.blit(waltLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))

    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()

run = True
bullets = []
while run:
    clock.tick(48)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_v]:
        if lastMove == "right":
            direction = 1
        else:
            direction = -1

        if len(bullets) < 11:
            bullets.append(shot(round(x + widht // 2), round(y + height // 2),
            5, (255, 0, 0), direction))

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_RIGHT] and x < 500 - widht - 5:
        x += speed
        right = True
        left = False
        lastMove = "right"
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    drawWindow()

pygame.quit()
