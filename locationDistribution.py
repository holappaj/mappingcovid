import json
from textwrap import indent
import matplotlib.pyplot as plt

dic = {}
dic2 = {}
dic3 = {}
dic4 = {}

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

def saveFile(dictionary, filename):
    with open(filename, 'w') as saveFile:
        json.dump(dictionary, saveFile, indent=4)

def createDistValueNew(file):
    for i in file:
        item = file[i]
        try:
            dic2[item] = dic2[item] + 1
        except KeyError:
            dic2[item] = 1
    return dic2

def createDistValueOld(file):
    for i in file:
        item = file[i]
        try:
            dic3[item] = dic3[item] + 1
        except KeyError:
            dic3[item] = 1
    return dic3

def drawGraph1(data):
    fig = plt.figure(figsize=(10,5))
    for i in data:
        x = i
        y = data[i]
        plt.scatter(x, y, c='red')
    plt.show()
    fig.savefig('locationDistPicClean.jpg', bbox_inches='tight', dpi=300)

def drawGraph2(data):
    fig = plt.figure(figsize=(10,5))
    for i in data:
        x = i
        y = data[i]
        plt.scatter(x, y, c='red')
    plt.show()
    fig.savefig('locationDistPicOrig.jpg', bbox_inches='tight', dpi=300)    
    

def repName(dataFile): 
    for i in dataFile:
        if (dataFile[i]["Rep"]) and ("Reputation: " in dataFile[i]["Rep"]):
            string = dataFile[i]["Rep"]
            string = string.split("Reputation: ")
            string = string[1]
            for chr in string:
                if chr == "\n":
                    temp = string.index(chr)
            loc = string[0 : temp]
            name = dataFile[i]["Name"]
            dic4[name] = loc
            print(loc)
    return dic4



if __name__ == "__main__":
    openedData = openFile("dataFile.json")
    createDistribution(openedData)
    saveFile(dic, 'locationData.json')
    
    oldData = openFile('locationData.json')
    newData = openFile("cleanedLocationData.json")
    
    createDistValueNew(newData)
    saveFile(dic2, 'locationNumbers.json')
    drawGraph1(dic2)
    
    createDistValueOld(oldData)
    drawGraph2(dic3)

    repName(openedData)
    saveFile(dic4, 'nameRep.json')
