import re
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1064645.html')

counts = list()
for line in fhand:
    line2 = line.decode().strip()
    #print(line2)
    x = re.findall('^\<tr\>.*>([0-9]+)', line2)
    if len(x)!= 1 : continue
    for i in x:
        counts.append(int(i))

print(sum(counts))
