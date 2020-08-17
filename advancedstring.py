def large(string):
  words = string.split(" ")
  buffer = " "
  i = 0
  for i in range(0, len(words), 2):
    buffer += words[i]+" "
    buffer += words[i + 1].upper()+ " "
  print buffer

def printWords(string):
	words = string.split(" ")
	for w in words:
	  print w

 
def printChars(string):
 for char in string:
   x = ord(char)
   print x

def average(string):
  m = string.count("M")
  f = string.count("F")
  total = (m+f)*1.0
  avgm = (m/total)*100
  avgf = (f/total)*100
  print avgm , "males" 
  print avgf , "females"
  
