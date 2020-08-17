def border(img,borderwidth,bordercolor):
  width= getWidth(img) - borderwidth
  height= getHeight(img) - borderwidth
  if borderwidth < 50:
    for p in getPixels(img):
     x=getX(p)
     y=getY(p)
     if y < borderwidth: 
       setColor(p,bordercolor)
     if y > height :
       setColor(p,bordercolor)
     if x < borderwidth:
       setColor(p,bordercolor)
     if x > width:
       setColor(p,bordercolor)
     
def lighter(img):
  half = getWidth(img)/2
  for p in getPixels(img):
    x=getX(p)
    if x < half:
      color = getColor(p)
      man = makeLighter(color)
      setColor(p,man)
    else:
      r=getRed(p)
      g=getGreen(p)
      b=getBlue(p)
      mom=(r+g+b)/3
      dad = makeColor(mom,mom,mom)
      setColor(p,dad)

def horizontal(img):
  third = getHeight(img)/3
  for p in getPixels(img):
    y = getY(p)
    if y < third:
      color = getColor(p)
      hello = makeLighter(color)
      setColor(p, hello)
    elif y < 2*third:
      r = getRed(p)
      g = getGreen(p)*0.7
      b = getBlue(p)*0.7
      color1 = makeColor(r,g,b)
      setColor(p,color1)
    else:
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      neg=makeColor(255-r,255-g,255-b)
      setColor(p,neg)