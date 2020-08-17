import sys 

char = sys.argv[1]
n = int(sys.argv[2])
space = " " * (n-2)

print char* n

for i in range(n-2):
 print char + space + char

print char * n

