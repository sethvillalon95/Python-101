def mirrorLeft(img):
  w = getWidth(img)
  h = getHeight(img)
  for y in range(0,h):
    for x in range(0,20):
      target = 40-1-x
      src = getPixel(img, x, y)
      dest = getPixel(img, target,y)
      color = getColor(src)
      setColor(dest, color)

def horizontal(img):
 w = getWidth(img)
 h = getHeight(img)/3
 for x in range(0,w):
   for y in range(0,h):
     px=getPixel(img,x,y)
     r=getRed(px)
     r=getRed(px)*0.5
     setRed(px,r)
   for y in range(2*h,3*h):
     px=getPixel(img,x,y)
     b=getRed(px)
     b=getRed(px)*0.5
     setBlue(px,b)

def horizontal2(img):
 w = getWidth(img)
 h = getHeight(img)/3
 for x in range(0,w):
   for y in range(0,h):
     px=getPixel(img,x,y)
     color = getColor(px)
     lol = makeLighter(color)
     setColor(px,lol)
   for y in range(h,2*h):
     px=getPixel(img,x,y)
     r=getRed(px)
     g=getGreen(px)*0.7
     b=getBlue(px)*0.7
     newcolor=makeColor(r,g,b)
     setColor(px,newcolor)
   for y in range(2*h,3*h):
     px = getPixel(img,x,y)
     r = getRed(px)
     g = getGreen(px)
     b = getBlue(px)
     negColor = makeColor(255-r,255-g,255-b)
     setColor(px,negColor)
  