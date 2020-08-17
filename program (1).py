def decreaseBlue(img):
  for p in getPixels(img):
    value=getBlue(p)
    setBlue(p,value*0.5)
    
def decreaseGreen(img):
  for p in getPixels(img):
    value=getGreen(p)
    setGreen(p,value*0.5)
    
def swapColor(img):
  for p in getPixels(img):
    red = getRed(p)
    green = getGreen(p)
    blue = getBlue(p)
    color = makeColor(blue,green,red)
    setColor(p,color)

def makeBlack(img):
  for p in getPixels(img):
    newColor = makeColor(0,0,0)
    setColor(p,newColor)
  
def makeWhite(img):
  for p in getPixels(img):
    newColor = makeColor(255,255,255)
    setColor(p,newColor)