import json
from textwrap import indent

dic = {}

file = open("dataFile.json")
dataFile = json.load(file)
 
for i in dataFile:
    if dataFile[i]["Rep"].startswith("\nLocation: "):
        string = dataFile[i]["Rep"]
        string = string[11:]
        for chr in string:
            if chr == "\n":
                temp = string.index(chr)
        loc = string[0 : temp]
        try:
            dic[loc] = dic[loc] + 1
        except KeyError:
            dic[loc] = 1
        

print(dic)
with open('locationData.json', 'w') as saveFile:
    json.dump(dic, saveFile, indent=4)