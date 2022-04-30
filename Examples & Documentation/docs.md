# Pixlib Documentation

**Please Note** this library is almost entirely **a joke**. It is inefficient, slow, and terribly written. That will not change, because it is a joke. If you are considering trying to make a serious project with this, I would highly recommend you don't. It is not that kind of thing.

## Objects
### pixlib object

**This is the base object you create to use the library.**

To initialise, the width and height of the windows and the size in pixels of each pixel object - allowing for smaller or larger pixel resolutions. (Example Below)

```
windowWidth = 720
windowHeight = 720
pixelSize = 2
pix = pixlib.pixlib(windowWidth,windowHeight,pixelSize)
```
Note that if the pixel size is not divisible into the resolution, the full window may not be covered.

### pix_sprite



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
