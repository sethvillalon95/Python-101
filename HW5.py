def eight(img):
  for p in getPixels(img):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    if r<100:
      setRed(p,0)
    if r>100:
      setRed(p,255)
    if g<100:
      setGreen(p,0)
    if g>100:
      setGreen(p,255)
    if b<100:
      setBlue(p,0)
    if b>100:
      setBlue(p,255)
    
def pinkify(img):
  for p in getPixels(img):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    if r>100 and g>100 and b>100:
      setColor(p,pink)
    