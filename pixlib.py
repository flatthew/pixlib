import pygame as pg

class pixel(pg.sprite.Sprite):
    def __init__(self, x,y, size, acolour = (0,0,0),opacity = 255):
        self.image = pg.Surface((size, size),pg.SRCALPHA)
        self.r = acolour[0]
        self.g = acolour[1]
        self.b = acolour[2]
        self.a = opacity
        self.color = (self.r,self.g,self.b,self.a)
        self.Rect = self.image.get_rect()
        self.Rect.move_ip(x,y)

    def updatePixel(self,canvas,acolour):
        self.image.fill(acolour)
        if len(acolour) == 4:
            self.r,self.g,self.b,self.a = acolour
        elif len(acolour) == 3:
            self.r,self.g,self.b = acolour
        canvas.blit(self.image,self.Rect)

class pixlib():
    def __init__(self,windowWidth,windowHeight,pixelsize):
        self.windowDim = [windowWidth,windowHeight]
        self.pixarrayDim = [windowWidth/pixelsize,windowHeight/pixelsize]
        self.pixels = self.initPixelarray
        self.window = pg.display.set_mode((windowWidth, windowHeight))
        self.pixelsize = pixelsize
        self.visualstates = {}

    def initPixelarray(self):
        pixels = []
        for i in range(0,self.windowDim[0],self.pixelsize):
            column = []
            for x in range(0,self.windowDim[1],self.pixelsize):
                column.append(pixel(i,x,self.pixelsize,(0,0,0,255)))
            pixels.append(column)
        return pixels

    def drawBasicBG(self,colour):
        for i in range(0,self.pixarrayDim[0]):
            for x in range(0,self.pixarrayDim[1]):
                self.pixels[i][x].updatePixel(self.window,colour)

    def addState(self,statename,statearray):
        if self.visualStates.get(statename,-1) != -1:
            raise ValueError('A State by this name already exists.')
        else:
            self.visualStates[statename] = statearray
    
    def removeState(self,statename):
        if self.visualStates.get(statename,-1) == -1:
            raise ValueError('There is no state by this name, and therefore it cannot be removed.')
        else:
            self.visualStates.pop(statename)

    def draw(self,screen,pixels):
        for a in range(len(self.visualStates[self.currentState])):
            for b in range(len(self.visualStates[self.currentState][a])):
                linepos = 0
                if self.visualStates[self.currentState][a][b][1] == None:
                    linepos = linepos+self.visualStates[self.currentState][a][b][0]
                else:
                    for c in range(self.visualStates[self.currentState][a][b][0]):
                        pixels[self.x+linepos][self.y+a].updatePixel(screen,self.visualStates[self.currentState][a][b][1])

def legacyUpdatePixel(canvas,pixel,acolour):
    pixel.image.fill(color=acolour)
    if len(acolour) == 4:
        pixel.r,pixel.g,pixel.b,pixel.a = acolour
    else:
        pixel.r,pixel.g,pixel.b = acolour
    canvas.blit(pixel.image,pixel.Rect)

def drawBasicBG(screen,pixels,windowWidth,windowHeight,size,colour):
    for i in range(0,windowWidth//size):
        for x in range(0,windowHeight//size):
            pixels[i][x].updatePixel(screen,colour)

class pixlibObject():
    def __init__(self,aposition,aheight,awidth,**kwargs):
        self.x, self.y = aposition
        self.height = aheight
        self.width = awidth
        self.visualStates = kwargs

    def addState(self,statename,statearray):
        if self.visualStates.get(statename,-1) != -1:
            raise ValueError('A State by this name already exists.')
        else:
            self.visualStates[statename] = statearray
    
    def removeState(self,statename):
        if self.visualStates.get(statename,-1) == -1:
            raise ValueError('There is no state by this name, and therefore it cannot be removed.')
        else:
            self.visualStates.pop(statename)

    def updatePos(self,screen,pixels,aposition):
        self.x, self.y = aposition
        self.draw(screen,pixels)

    def draw(self,screen,pixels):
        for a in range(len(self.visualStates[self.currentState])):
            for b in range(len(self.visualStates[self.currentState][a])):
                linepos = 0
                if self.visualStates[self.currentState][a][b][1] == None:
                    linepos = linepos+self.visualStates[self.currentState][a][b][0]
                else:
                    for c in range(self.visualStates[self.currentState][a][b][0]):
                        pixels[self.x+linepos][self.y+a].updatePixel(screen,self.visualStates[self.currentState][a][b][1])

