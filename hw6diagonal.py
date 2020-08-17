def diagonalLeft(img):
  w = getWidth(img)
  h = getHeight(img)
  for y in range(0,h):
    for x in range(0,y):
      src = getPixel(img, x, y)
      dest = getPixel(img, y,x)
      color = getColor(src)
      setColor(dest, color)
      
def diagonalRight(img):
  w = getWidth(img)
  h = getHeight(img)
  for y in range(0,h):
    for x in range(0,w):
      src = getPixel(img, h-1-y, x)
      dest = getPixel(img,w-1-x,y)
      color = getColor(src)
      setColor(dest, color)