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
        
        if self.rect.y > 450:
            '''move_up = True
            move_down = False'''
            self.rect.y *= -1
        if self.rect.y < 50:
            '''move_up = False
            move_down = True'''
            self.rect.y *= -1
        '''if move_right == True:
            self.rect.x += self.speed
        if move_left == True:
            self.rect.x -= self.speed
        if move_up == True:
            self.rect.y -= self.speed
        if move_down == True:
            self.rect.y += self.speed'''
game = True

finish = False
run = True
clock = time.Clock()
FPS = 60
igrok1 = Playerone('rocket.png', 0, 200, 5, 50, 75)
igrok2 = Playertwo('rocket.png', 650, 200, 5, 50, 75)
winone = font.render('PLAYER ONE WIN', True, (124,252,0))
wintwo = font.render('PLAYER TWO WIN', True, (124,252,0))
myach = Ball('asteroid.png', 300, 200, 5, 50, 50)
speed = 5
while game:
    if run != False:
        for e in event.get():
            if e.type == QUIT:
                game = False
        if finish != True:
            '''move_up = False
            move_down = True
            move_right = True
            move_left = False'''
            myach.rect.x += speed
            myach.rect.y += speed
            window.blit(background, (0, 0))
            igrok1.reset()
            igrok1.update()
            igrok2.reset()
            igrok2.update()
            if myach.rect.y > 550:
                speed *= -1
            if myach.rect.y < 50:
                speed *= -1
            myach.reset()
    display.update()
    clock.tick(FPS)