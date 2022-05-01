# pixlib
This is a really dumb side project I made using python and pygame. 
In essence, it works by creating a massive array of pixel objects, which cover an entire pygame window, and then everything that is displayed is made on top of this. It was created mostly as something to do while procrastinating or busy. Please, for the love of god, do not try to use this seriously.

All of the documentation that exists for this can be found below. It's not going to be heavily documented, it is a silly side project.

## What this is for
- Memes
- Jokes
- Generally doing stupid things
## What this is most definitely not for
- Anything at all serious, this thing is horrifically inefficient, and probably incredibly wasteful in terms of both memory and CPU usage. 

# Documentation

**Please Note** this library is almost entirely **a joke**. It is inefficient, slow, and terribly written. That will not change, because it is a joke. If you are considering trying to make a serious project with this, I would highly recommend you don't. It is not that kind of thing.

## Objects
### pixlib object

**This is the base object you create after creating the window to initialise the library.**

To initialise, the width and height of the windows and the size in pixels of each pixel object - allowing for smaller or larger pixel resolutions. (Example Below)

```
windowWidth = 720
windowHeight = 720
pixelSize = 2
pix = pixlib.pixlib(windowWidth,windowHeight,pixelSize)
```
Note that if the pixel size is not divisible into the resolution, the full window may not be covered.

### pix_sprite

**This object is used to create sprites that are able to move across the pixel grid automatically.**

## Asset Encoding
Assets are encoded using a form of Run Length Encoding. It comprises several lists. 

```
A = [
    [[1,None],[2,red],[1,None]],
    [[1,orange],[2,None],[1,orange]],
    [[1,yellow],[2,None],[1,yellow]],
    [[4,green]],
    [[1,blue],[2,None],[1,blue]],
    [[1,indigo],[2,None],[1,indigo]],
    [[1,violet],[2,None],[1,violet]]
]
```
(Pictured above, a rainbow coloured capital A, using variable names where a typical RGB tuple could otherwise be used.)
