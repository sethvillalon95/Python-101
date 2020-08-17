def makeCircle(x,y):
  canvas = makeEmptyPicture(400,400)
  addOvalFilled(canvas, x, y, 50, 50, red)
  return canvas

def bounce():
  x = 1
  y = 1 
  i = 1
  dx = 10
  dy = -10
  while i < 200:
    frame = makeCircle(x,y)
    if x < 0 or x > 350:
      dx = -dx
    if y < 0 or y >350:
      dy = -dy
    x += dx
    y += dy
    if i < 10:
      writePictureTo(frame, "C:/Users/Seth Villalon/Desktop/ball/frame00"+str(i)+".png")
    elif i < 100:
     writePictureTo(frame, "C:/Users/Seth Villalon/Desktop/ball/frame0"+str(i)+".png")
    else:
      writePictureTo(frame, "C:/Users/Seth Villalon/Desktop/ball/frame"+str(i)+".png")
    i +=1
    