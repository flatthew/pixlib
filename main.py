import pygame as pg
import random
import pixlib as pl
import pixlibAlphabet as plalpha

windowWidth = 500
windowHeight = 500

white = 255,255,255,255
terminalGreen = 0,255,0,255
black = 0,0,0,255

def generateRandomArray():
    array = []
    for i in range(1,101):
        array.append[i]
    array = random.shuffle(array)
    return array

def bubbleSort(array):
    for x in range(0,(len(array)-1)): #goes through for the maximum number of passes
        for i in range(0, len(array)-1): #main loop for the pass
            if array[i] > array[i+1]: #checks if an item needs to be swapped
                array[i],array[i+1] = array[i+1],array[i] #carries out swap
            else:
                pass
    return array

def main(size):
    pg.init()
    pixlib = pl.pixlib(windowWidth,windowHeight,size)
    go = True

    while go ==True:
        ##ALL LOGIC HERE
        for event in pg.event.get():
            #events
            if event.type == pg.QUIT: #if window is x'd out
                go = False
            #keystrokes
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE: #if Esc Pressed
                    go = False
        
        #if sortarray

        #DRAW ALL YOUR OBJECTS HERE (THE LAST DRAWN WILL BE AT THE 'FRONT')
        pl.drawBasicBG(pixlib.window,pixlib.pixels,windowWidth,windowHeight,size,black)
        plalpha.debugDRAWALL(pixlib.window,pixlib.pixels,)
        
        

        pg.display.flip()

main(5)