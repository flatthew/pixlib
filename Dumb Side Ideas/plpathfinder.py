import pixlib as pl
import pygame as pg
import pixlib as pl
import pixlibAlphabet as plalpha

windowWidth = 500
windowHeight = 500

white = 255,255,255,255
terminalGreen = 0,255,0,255
black = 0,0,0,255

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

        #DRAW ALL YOUR OBJECTS HERE (THE LAST DRAWN WILL BE AT THE 'FRONT')
        pixlib.drawBasicBG(black)
        
        pg.display.flip()

main(3)