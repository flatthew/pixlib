import pygame as pg
import random
from pixlib import *
from pixlibAlphabet import drawChar
windowWidth = 500
windowHeight = 500

white = 255,255,255,255
green = 0,255,0,255
black = 0,0,0,255

class paddle():
    def __init__(self,apos,awidth,alength,acolour):
        self.pos = apos
        self.width = awidth
        self.length = alength
        self.colour = acolour
        self.score = 0

    def drawPaddle(self,screen,pixels,pixelsize):
        for i in range(self.pos[0], (self.pos[0] + self.width//pixelsize), 1):
            for x in range(self.pos[1], self.pos[1] + self.length//pixelsize, 1):
                print('i'+str(i)+'x'+str(x))
                print(len(pixels))
                legacyUpdatePixel(screen,pixels[i][x],white)

    def updatePaddle(self,dir,windowHeight,pixelsize):
            if self.pos[1] == (windowHeight//pixelsize) - (self.length//pixelsize) - 1 and dir == 1:
                pass
            elif self.pos[1] == 11 and dir == -1:
                pass
            else:
                self.pos[1] = self.pos[1] + dir

class ball():
    def __init__(self,apos,awidth,alength,acolour):
        pos = apos
        width = awidth
        length = alength
        colour = acolour

    def bounceCheck(self):
        pass

def drawUI(screen,pixels,windowWidth,windowHeight,size,p1score,p2score):
    for i in range(0,windowHeight//size,1):
        if i%4 == 0:
            pass
        else:
            legacyUpdatePixel(screen,pixels[windowWidth//(size*2)][i],white)
    p1score = str(p1score)
    if len(p1score) > 1:
        p1score.split()
        for i in range(len(p1score)):
            drawChar(p1score[i],screen,pixels,white,(((windowWidth//(size*2)//(size*2))-(len(p1score)*5-1),1)))
    else:
        drawChar(p1score,screen,pixels,white,(((windowWidth//(size*2)//size*2)-3),1))
    
def pong(size):
    pg.init()
    screen = pg.display.set_mode((windowWidth, windowHeight))
    pg.display.set_caption('Pong')
    pixels = initWindow(windowWidth,windowHeight,size,black)
    paddlesize = 10
    paddles = [paddle([1,10],paddlesize,paddlesize*6,white),paddle([windowWidth//(size) - 1 - (paddlesize//size),10],paddlesize,paddlesize*6,white)]
    
    go = True

    while go ==True:
        for event in pg.event.get():
            #events
            if event.type == pg.QUIT: #if window is x'd out
                go = False
            #keystrokes
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE: #if Esc Pressed
                    go = False
        keys = pg.key.get_pressed()  #checking pressed keys
        if keys[pg.K_UP]:
            paddles[1].updatePaddle(-1,windowHeight,size)
        if keys[pg.K_DOWN]:
            paddles[1].updatePaddle(1,windowHeight,size)
        if keys[pg.K_w]:
            paddles[0].updatePaddle(-1,windowHeight,size)
        if keys[pg.K_s]:
            paddles[0].updatePaddle(1,windowHeight,size)
        
        
        drawBG(screen,pixels,windowWidth,windowHeight,size,black)
        drawUI(screen,pixels,windowWidth,windowHeight,size,paddles[0].score,paddles[1].score)
        
        for i in range(0,len(paddles)):
            paddles[i].drawPaddle(screen,pixels,size)
        
        pg.display.flip()

pong(5)