from pygame import *
from random import *
font.init()
font = font.SysFont('Arial', 40)
window = display.set_mode((700, 500))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
class GameSprite(sprite.Sprite):
    def __init__(self, picture, pos_1, pos_2, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(picture), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos_1
        self.rect.y = pos_2
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Playerone(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_W] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_S] and self.rect.y < 425:
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
        if sprite.spritecollide(self, playerone, False) == True:
            move_right = True
            move_left = False
        if sprite.spritecollide(self, playertwo, False) == True:
            move_right = False
            move_left = True
        if self.rect.y >= 450:
            move_up = True
            move_down = False
        if self.rect.y <= 0:
            move_up = False
            move_down = True
        if move_right == True:
            self.rect.x += self.speed
        if move_left == True:
            self.rect.x -= self.speed
        if move_up == True:
            self.rect.y -= self.speed
        if move_down == True:
            self.rect.y += self.speed
game = True
finish = False
run = True
clock = time.Clock()
FPS = 60
playerone = Playerone('rocket.png', 50, 200, 15, 50, 75)
playertwo = Playertwo('rocket.png', 650, 200, 15, 50, 75)
winone = font.render('PLAYER ONE WIN', True, (124,252,0))
wintwo = font.render('PLAYER TWO WIN', True, (124,252,0))
ball = Ball('asteroid.png', 300, 200, 15, 50, 50)
