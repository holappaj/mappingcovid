import json

def writeFile(file, data):
    with open(file, 'w') as saveFile:
        json.dump(data, saveFile, indent=4)

def openFile(file):
    data = open(file)
    data = json.load(data)
    return data

def findQuote(data):
    quoteDic = {}
    for post in data:
        userName = data[post]['Name']
        text = data[post]["Text"]
        if text.startswith('\nQuote'):
            quote = text.split("\n")[6]
            index = quote.index('by')
            quoteName = quote[index+3:]
            #print(quoteName)
            if userName not in quoteDic:
                quoteDic[userName] = [quoteName]
            else:
                if quoteName not in quoteDic[userName]:
                    quoteDic[userName].append(quoteName)
    return quoteDic
        

if __name__ == "__main__":
    data = openFile("dataFile.json")
    data = findQuote(data)
    writeFile('quoteData.json', data)