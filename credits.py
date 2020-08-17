while True:
  name = raw_input("Hi, please tell me your name: ")
  print "Nice to meet you, " + name
  creString = raw_input("How many credits are have you taken? ")
  cre = int(creString)
  if cre < 0:
    break 
  if cre < 30:
    print "Freshman"
  elif cre< 60:
    print "Sophomore"
  elif cre < 90:
    print "Junior"
  else:
    print "Senior"

print "SEE YOU!"