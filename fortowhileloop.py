def sunset(img):
  for p in getPixels(img):
    value = getBlue(p)
    setBlue(p,value*0.7)
    value = getGreen(p)
    setGreen(p,value*0.7)

def sunset2(img):
  index = 0
  pixies = getPixels(img)
  while index < len(pixies):
    p = pixies[index]
    value = getBlue(p)
    setBlue(p,value*0.7)
    value = getGreen(p)
    setGreen(p,value*0.7)
    index += 1

def rotate2(img):
  canvas = makeEmptyPicture(1000,1000)
  w = getWidth(img)
  h = getHeight(img)
  x = 0
  y = 0
  while x < w:
    y = 0
    while y < h:
      color = getColor(getPixel(img,x,y))
      setColor(getPixel(canvas,y,w-x-1),color)
      y += 1
    x +=1
  return canvas
 
def rotate(img):
  canvas = makeEmptyPicture(1000,1000)
  targetX = 0
  w = getWidth(img)
  h = getHeight(img)
  for sourceX in range(0,w):
    targetY = 0
    for sourceY in range(0,h):
      color = getColor(getPixel(img,sourceX,sourceY))
      setColor(getPixel(canvas,targetY,w-targetX-1),color)
      targetY += 1
    targetX +=1
  show(canvas)
  return canvas