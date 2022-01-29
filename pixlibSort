def drawArray(screen,array,pixels,operation,currentpoint):
    for i in range(len(array)):
        if i == currentpoint:
            if operation == 'compare':
                for x in range(array[i]):
                    pixels[i][x].updatePixel(screen,(0,255,0))
            elif operation == 'swap':
                for x in range(array[i]):
                    pixels[i][x].updatePixel(screen,(255,0,0))
        else:
            for x in range(array[i]):
                    pixels[i][x].updatePixel(screen,(0,0,255))