import json
from textwrap import indent

dic = {}

def openFile(fileName):
    file = open(fileName)
    dataFile = json.load(file)
    return dataFile

def createDistribution(dataFile): 
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
    return dic

def saveFile(dictionary):
    with open('locationData.json', 'w') as saveFile:
        json.dump(dictionary, saveFile, indent=4)
    print("made it here")

if __name__ == "__main__":
    openedData = openFile("dataFile.json")
    createDistribution(openedData)
    saveFile(dic)