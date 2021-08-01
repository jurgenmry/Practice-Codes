import urllib.request, urllib.parse, urllib.error
import json

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1064648.json')
data = fhand.read()
#print(len(data))

info =json.loads(data)
#print (len(info))
print (info)
print ("==============================================")
total = 0

info = info["comments"]

for item in info:
    print("Count: ",item["count"])
    total = total + int(item["count"])
    print("Sum: ", total)

print("Final sum: ", total)
