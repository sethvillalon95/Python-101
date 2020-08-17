def circle(x,y):
  canvas = makeEmptyPicture(200,200)
  addOvalFilled(canvas,x,y,100,100,yellow)
  addOval(canvas,x,y,100,100)
  addRectFilled(canvas,80,90,10,10,black)
  addRectFilled(canvas,115,90,10,10,black)
  addOvalFilled(canvas,72,122,60,10,black)
  return canvas
  
def circle1(x,y):
  canvas = makeEmptyPicture(500,500)
  addOvalFilled(canvas,x,y,100,100,yellow)
  addOval(canvas,x,y,100,100)
  x1 = x + 30
  y1 = y + 40
  x2 = x + 65
  y2 = y + 40
  x3 = x + 22 
  y3 = y + 72
  addRectFilled(canvas,x1,y1,10,10,black)
  addRectFilled(canvas,x2,y2,10,10,black)
  addOvalFilled(canvas,x3,y3,60,10,black)
  return canvas
   
 
def circle2(canvas,x,y):
  addOvalFilled(canvas,x,y,100,100,yellow)
  addOval(canvas,x,y,100,100)
  x1 = x + 30
  y1 = y + 40
  x2 = x + 65
  y2 = y + 40
  x3 = x + 22 
  y3 = y + 72
  addRectFilled(canvas,x1,y1,10,10,black)
  addRectFilled(canvas,x2,y2,10,10,black)
  addOvalFilled(canvas,x3,y3,60,10,black)
  
  
def crowd():
  canvas = makeEmptyPicture(1000,1000)
  for y in range(0,300,150):
    for x in range(0,300,150):
      circle2(canvas,x,y) 
  return canvas
