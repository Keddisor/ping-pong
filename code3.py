from pygame import *
from random import *
font.init()
font = font.SysFont('Arial', 40)
window = display.set_mode((700, 500))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
class GameSprite(sprite.Sprite):
    def __init__(self, picture, pos_1, pos_2, speed, width, height, down, up, left, right):
        super().__init__()
        self.image = transform.scale(image.load(picture), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos_1
        self.rect.y = pos_2
        self.down = down
        self.up = up
        self.left = left
        self.right = right
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Playerone(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 425:
            self.rect.y += self.speed
class Playertwo(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 425:
            self.rect.y += self.speed
class Ball(GameSprite):
    def update(self):
        if self.right == True:
            self.rect.x += self.speed
        if self.left == True:
            self.rect.x -= self.speed
        if self.up == True:
            self.rect.y -= self.speed
        if self.down == True:
            self.rect.y += self.speed
game = True
finish = False
run = True
clock = time.Clock()
FPS = 60
playerone = Playerone('rocket.png', 0, 200, 15, 50, 75, False, False, False, False)
playertwo = Playertwo('rocket.png', 650, 200, 15, 50, 75, False, False, False, False)
winone = font.render('PLAYER ONE WIN', True, (124,252,0))
wintwo = font.render('PLAYER TWO WIN', True, (124,252,0))
ball = Ball('asteroid.png', 300, 200, 5, 50, 50, True, False, False, True)
while game:
    if run != False:
        for e in event.get():
            if e.type == QUIT:
                game = False
        if finish != True:
            window.blit(background, (0, 0))
            playerone.reset()
            playerone.update()
            playertwo.reset()
            playertwo.update()
            ball.update()
            ball.reset()
            if ball.rect.y >= 450:
                ball.up = True
                ball.down = False
            if ball.rect.y <= 0:
                ball.up = False
                ball.down = True
            if sprite.spritecollide(ball, playerone, False):
                ball.right = True
                ball.left = False
            if sprite.spritecollide(ball, playertwo, False):
                ball.left = True
                ball.right = False
        display.update()
        clock.tick(FPS)