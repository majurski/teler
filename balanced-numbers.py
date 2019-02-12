#A = "" 
#stopword = "" 
#while True: 
#   line = input() 
#   if line.strip() == stopword: 
#      break 
#   A += "%s\n" % 
	

import fileinput 
for line in fileinput.input(): 
   colect = []
   colect.append(line)

if int(line[0]) + int(line[2]) == int(line[1]):
    print(sum(colect))
else:
    pass