import pygame
import sys
from random import*
from pygame.locals import *
pygame.init()

font = pygame.font.SysFont('Comic Sans MS', 35)
pygame.mixer.music.load('music/Adam Bushfield — Doctor Who s1-3 Theme 8-bit (www.lightaudio.ru).mp3')
pygame.mixer.music.play()

speed = 20
FPS = 30
WIN_WIDTH = 1080
WIN_HEIGHT = 720
ye = 100
xe = 100
points = 0
music = 1
t = 0

com=pygame.image.load('image/com.png')
com=pygame.transform.scale(com,(WIN_WIDTH,WIN_HEIGHT))

BadWolf=pygame.image.load('image/BadWolf.png')
BadWolf=pygame.transform.scale(BadWolf,(300,70))

Fnaf=pygame.image.load('image/Fnaf.png')
Fnaf=pygame.transform.scale(Fnaf,(300,70))

corabl = [pygame.image.load("image/corablgif/corabl1.png"),
                pygame.image.load("image/corablgif/corabl2.png"),
                pygame.image.load("image/corablgif/corabl3.png"),
                pygame.image.load("image/corablgif/corabl4.png"),
                pygame.image.load("image/corablgif/corabl5.png"),
                pygame.image.load("image/corablgif/corabl6.png"),
                pygame.image.load("image/corablgif/corabl7.png"),
                pygame.image.load("image/corablgif/corabl8.png"),
                pygame.image.load("image/corablgif/corabl9.png"),
                pygame.image.load("image/corablgif/corabl10.png"),
                pygame.image.load("image/corablgif/corabl11.png"),
                pygame.image.load("image/corablgif/corabl12.png"),
                pygame.image.load("image/corablgif/corabl13.png"),
                pygame.image.load("image/corablgif/corabl14.png"),
                pygame.image.load("image/corablgif/corabl15.png"),
                pygame.image.load("image/corablgif/corabl16.png")]

Star=pygame.image.load('image/Star.png')
Star=pygame.transform.scale(Star,(70,70))

blaster=pygame.image.load('image/blaster.png')
blaster=pygame.transform.scale(blaster,(40,40))

fon=pygame.image.load('image/fon.png')
fon=pygame.transform.scale(fon,(WIN_WIDTH,WIN_HEIGHT))


clock = pygame.time.Clock()
sc = pygame.display.set_mode(
(WIN_WIDTH, WIN_HEIGHT))

clock = pygame.time.Clock()

x = WIN_WIDTH // 2

y = WIN_HEIGHT // 2

xb=x+50

yb=y

moving="stop"

Esc = 'stop '

attack="stop"
speed_blaster=0

start_ticks=pygame.time.get_ticks()

value = 0
menu="yes"
while 1:
    seconds = int((pygame.time.get_ticks() - start_ticks) / 400)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_a:
                moving="left"
            if i.key==pygame.K_d:
                moving="right"
            if i.key==pygame.K_w:
                moving="up"
            if i.key==pygame.K_s:
                moving="down"
            if i.key==pygame.K_SPACE:
                attack="attack"
            if i.key==pygame.K_ESCAPE:
                Esc="END"

            if i.key == pygame.K_e:
                menu = "no"
        if i.type == pygame.KEYUP:
            if i.key==pygame.K_a or i.key==pygame.K_d or i.key==pygame.K_s or i.key==pygame.K_w or i.key==pygame.K_SPACE or i.key==pygame.K_ESCAPE:
                moving="stop"
    if menu=="yes":
        sc.blit(com,(0,0))
    else:
        yb+=speed_blaster

        if attack=="attack":
            speed_blaster=-15
        else:
            yb = y+40
            xb = x+25

        seconds -= t
        if abs (xe - xb) < 50 and abs (ye - yb) < 50:
            xe = randint (100,1000)
            ye = randint (100, 500)
            t += 4
            points += 1

        value += 1

        if value >= len(corabl) - 1:
                value = 0
        image = corabl[value]

        f = 150
        if value == 0:
            p = 200
        else:
            p = 265

        if Esc=="END":
            break

        if moving=="left":
            x=x-speed

        if moving=="right":
            x=x+speed

        if moving == "up":
            y = y - speed

        if moving == "down":
            y = y + speed

        if y<0:
            y=0
        if x<0:
            x=0
        if x+100>WIN_WIDTH:
            x=WIN_WIDTH-100
        if y+100>WIN_HEIGHT:
            x=WIN_HEIGHT-100
        if yb<0:
            yb=y
            attack="stop"
            speed_blaster = 0
        if seconds >= 100: #конец игры
            sc.blit(Fnaf,(100,100))
            break

        text = font.render("XP   " + str(points), 0, (255,250,250))
        text2 = font.render("BBC timer " + str(seconds), 0, (255,250,250))

        sc.blit(fon, (0, 0))
        sc.blit(BadWolf,(40, 25))
        sc.blit(blaster, (xb, yb))
        sc.blit(Star, (xe, ye))
        sc.blit(text, (900, 38))
        sc.blit(text2, (550, 38))
        sc.blit(image,(x, y))
    pygame.display.update()

    clock.tick(FPS)