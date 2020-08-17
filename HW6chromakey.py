def chromakey(fg,bg):
  for px in getPixels(fg):
    r = getRed(px)
    g = getGreen(px)
    b = getBlue(px)
    if g > r and g > b:
      x = getX(px)
      y = getY(px)
      bgpix = getPixel(bg,x,y)
      a = getColor(bgpix)
      setColor(px,a) 
      
def redHair(img):
  hair = makeColor(42,25,15)
  eye = makeColor(43,16,35)
  teeth = makeColor(232,186,173)
  for pixy in getPixels(img):
    x = getX(pixy)
    y = getY(pixy)
    if 79< x < 292 and 74< y <186: 
       color = getColor(pixy)
       diff = distance(hair, color)
       if diff < 80:
         setColor(pixy, orange)
    if 265< x < 283 and 184< y <259: 
       color = getColor(pixy)
       diff = distance(hair, color)
       if diff < 100:
         setColor(pixy, orange)
    if 73< x < 100 and 178< y <266: 
       color = getColor(pixy)
       diff = distance(hair, color)
       if diff < 80:
         setColor(pixy, orange)
    if 117< x < 248 and 216< y <236: 
       color = getColor(pixy)
       diff = distance(eye, color)
       if diff < 50:
         setColor(pixy, red)
    if 149 <x <224 and 309< y <331:
       color = getColor(pixy)
       diff = distance(teeth,color)
       if diff < 100:
         setColor(pixy,magenta)
    
   
   

 