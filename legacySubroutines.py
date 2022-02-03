def legacyUpdatePixel(canvas,pixel,acolour):
    pixel.image.fill(color=acolour)
    if len(acolour) == 4:
        pixel.r,pixel.g,pixel.b,pixel.a = acolour
    else:
        pixel.r,pixel.g,pixel.b = acolour
    canvas.blit(pixel.image,pixel.Rect)