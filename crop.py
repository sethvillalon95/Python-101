def crop1(img, top, bottom, left, right):
  canvas = makeEmptyPicture(1000,1000)
  w = getWidth(img)
  h = getHeight(img)
  y2= 200
  for y1 in range(top, bottom):
    x2 = 400 
    for x1 in range(left, right):
      src = getPixel(img, x1, y1)
      dest = getPixel(canvas, x2, y2)
      color = getColor(src)
      setColor(dest,color)
      x2 = x2 + 1
    y2 = y2 + 1
  return canvas
  
def crop2(img, top, bottom, left, right):
  canvas = makeEmptyPicture(1000,1000)
  w = getWidth(img)
  h = getHeight(img)
  y2= 200
  for y1 in range(top, bottom):
    x2 = 400 
    for x1 in range(left, right):
      src = getPixel(img, x1, y1)
      dest = getPixel(canvas, x2, y2)
      color = getColor(src)
      setColor(dest,color)
      x2 = x2 + 1
    y2 = y2 + 1
  y2= 100
  for y1 in range(top, bottom):
    x2 = 400 
    for x1 in range(left, right):
      src = getPixel(img, x1, y1)
      dest = getPixel(canvas, x2, y2)
      color = getColor(src)
      setColor(dest,color)
      x2 = x2 + 1
    y2 = y2 + 1
  return canvas