import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1064647.xml')

#for line in fhand:
#   line2 = line.decode().rstrip()
#stuff = ET.fromstring(line2)
#print(stuff)
#lst = stuff.findall('comment/count')
#print (len(lst))

data = fhand.read().decode()
#print(data)
stuff = ET.fromstring(data)
#print (stuff)
lst = stuff.findall('.//count')
#print (lst)
accumulation = 0
for i in lst:
    accumulation = accumulation + int(i.text)
print (str(accumulation))
