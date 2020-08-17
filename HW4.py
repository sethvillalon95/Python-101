def blue(img):     
  for p in getPixels(img):
    r = getRed(p)*0.5
    g = getGreen(p)*0.5
    b = getBlue(p)*2.0
    color = makeColor(r,g,b)
    setColor(p,color)
    
def negative(img):
  for p in getPixels(img):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    x = makeColor(255-r, 255-g, 255-b)
    setColor(p,x)

  
def grayScale(img):
  for p in getPixels(img):
     y = (getRed(p)+getGreen(p)+getBlue(p))/3
     setColor(p,makeColor(y,y,y))
     
def negateFinal(img):
  grayScale(img)
  negative(img)
     
def negate(img):
 for p in getPixels(img):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    y = (getRed(p)+getGreen(p)+getBlue(p))/3
    setColor(p,makeColor(y,y,y))
    x = makeColor(255-r, 255-g, 255-b)
    setColor(p,x)
    
def topBlack(img):
  pixels = getPixels(img)
  top = len(pixels)/2
  for index in range(0,top):
     pixel = pixels[index]
     setColor(pixel,black)
      
    
def mirrorHalf2(img):
  pixels = getPixels(img)
  target = len(pixels)- 1
  for index in range(0, len(pixels)/2):
    pixel1 = pixels[index]
    pixel2 = pixels[target]
    color1 = getColor(pixel2)
    setColor(pixel1,color1)
    target = target-1
     
