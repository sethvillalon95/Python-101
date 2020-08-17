def copy(img, canvas, dx, dy):
  w = getWidth(img)
  h = getHeight(img)
  y2 = dy
  for y1 in range(0,h):
    x2 = dx
    for x1 in range(0,w):
      src = getPixel(img, x1, y1)
      dest = getPixel(canvas, x2, y2)
      color = getColor(src)
      setColor(dest, color)
      x2 = x2 + 1
    y2 = y2 + 1

def makeComic():
  bg = makeEmptyPicture(400, 400)
  copy(toad, bg, 100, 50)
  myFont = makeStyle(sansSerif, bold+italic, 12)
  addTextWithStyle(bg, 100,220 , "When frogs park illegaly, They get TOAD", myFont, red)
  return bg

def save(picture):
  file = "C:\Users\Seth Villalon\Desktop\CIS 101\homeworktoad.jpg "
  writePictureTo(picture, file)
  
  
def makeComic2():
  bg = makeEmptyPicture(2000, 500)
  copy(pic1, bg, 50, 50)
  copy(pic2, bg, 500, 50)
  copy(pic3, bg, 950, 50)
  myFont = makeStyle(sansSerif, bold, 20)
  addTextWithStyle(bg, 70, 300, "\"SPONGEBOOB! Help me with a bug\"",myFont,white)
  addTextWithStyle(bg, 600, 300, "\"A what?\"",myFont,white)
  addTextWithStyle(bg, 1049, 300, "\"A BUUUUGGGG?!!!!!\"",myFont,black)
  myFont = makeStyle(sansSerif, bold+italic, 60)
  addTextWithStyle(bg, 150, 470, "Programming Assignment Under the Sea", myFont, red)
  return bg