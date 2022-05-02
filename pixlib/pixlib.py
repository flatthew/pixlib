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

class states_root():
    def __init__(self,states) -> None:
        self.visualStates = states
        self.currentState = states['main']

    def addState(self,statename,statearray):
        if self.visualStates.get(statename,-1) != -1:
            raise ValueError('State ' + statename + ' already exists.')
        else:
            self.visualStates[statename] = statearray
    
    def removeState(self,statename):
        if self.visualStates.get(statename,-1) == -1:
            raise ValueError('There is no state called \''+ statename +'\' and therefore it cannot be removed.')
        else:
            self.visualStates.pop(statename)

    def switchState(self,statename):
        if self.visualStates.get(statename,-1) == -1:
            raise ValueError('No such state as ' + statename)
        else:
            self.currentState = statename

    def alterState(self,statename,newStateVal):
        if self.visualStates.get(statename,-1) == -1:
            raise ValueError('No such state as ' + statename)
        elif type(newStateVal) != list or type(newStateVal) != tuple:
            raise ValueError('State in invalid format')
        else:
            self.visualStates[statename] = newStateVal

    def draw(self):
        for a in range(len(self.visualStates[self.currentState])):
            for b in range(len(self.visualStates[self.currentState][a])):
                linepos = 0
                if self.visualStates[self.currentState][a][b][1] == None:
                    linepos = linepos+self.visualStates[self.currentState][a][b][0]
                else:
                    for c in range(self.visualStates[self.currentState][a][b][0]):
                        self.pixels[self.x+linepos][self.y+a].updatePixel(self.window,self.visualStates[self.currentState][a][b][1])

class pix_canvas(states_root):
    def __init__(self,windowWidth,windowHeight,pixelsize,states):
        self.windowDim = [windowWidth,windowHeight]
        self.pixarrayDim = [windowWidth//pixelsize,windowHeight//pixelsize]
        self.pixelsize = pixelsize
        self.pixels = self.__initPixelarray__()
        self.window = pg.display.set_mode((windowWidth, windowHeight))
        self.pixelsize = pixelsize
        super().__init__(states)
        self.currentState = ''
        self.x = 0
        self.y = 0

    def __initPixelarray__(self):
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

class pix_sprite(states_root):
    def __init__(self,aposition,aheight,awidth,states):
        self.x, self.y = aposition
        self.height = aheight
        self.width = awidth
        super().__init__(states)
        self.currentState = ''

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

def LEGACY_UpdatePixel(canvas,pixel,acolour):
    pixel.image.fill(color=acolour)
    if len(acolour) == 4:
        pixel.r,pixel.g,pixel.b,pixel.a = acolour
    else:
        pixel.r,pixel.g,pixel.b = acolour
    canvas.blit(pixel.image,pixel.Rect)