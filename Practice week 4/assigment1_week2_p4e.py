import re
numlist = list()
fhand = open ('regex_sum_42.txt')
for line in fhand :
    line = line.rstrip()
    y = re.findall('[0-9]+' , line)
    if len (y) < 1 : continue
    #print (y)  (debugging)
    for i in y:
        num = float(i)
        numlist.append(num)

#print(numlist) This is a fail trail
    #if len (y)!= 1: continue
    #print (y)
    #num = float(y[0])
    #numlist.append(num)

print (sum(numlist[:]))
