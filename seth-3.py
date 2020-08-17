import sys

if len(sys.argv) == 1:
	print "Enter a file"
	
else:
	filename = sys.argv[1]
	file = open(filename)
	lines = 0
	chars = 0
	vowels = 0
	consonants = 0
	lowers = 0
	uppers = 0
	
	for line in file:
		lines += 1
		for char in line:
			chars += 1
			if char.lower() in "aeiou":
				vowels +=1
			if char.lower() in "bcdfghjklmnpqrstvwxyz":
				consonants +=1
			if char in "abcdefghijklmnopqrstuvwxyz":
				lowers +=1	
			if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
				uppers +=1
					
print "There are",lines,"lines."
print "There are",chars, "characters."
print "There are", vowels,"vowels."
print "There are", consonants,"consonants."
print "There are", lowers,"lower-case letters."
print "There are", uppers,"upper-case letters."
