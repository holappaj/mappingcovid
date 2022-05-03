import json
from textwrap import indent
import matplotlib.pyplot as plt

dic = {}
dic2 = {}

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

def createDistValue(file):
    for i in file:
        item = file[i]
        try:
            dic2[item] = dic2[item] + 1
        except KeyError:
            dic2[item] = 1
    return dic2

def drawGraph(data):
    for i in data:
        x = i
        y = data[i]
        plt.scatter(x, y, c='red')
    plt.show()

if __name__ == "__main__":
    openedData = openFile("dataFile.json")
    createDistribution(openedData)
    saveFile(dic, 'locationData.json')
    newData = openFile("locationData.json")
    createDistValue(newData)
    saveFile(dic2, 'locationNumbers.json')
    drawGraph(dic2)
