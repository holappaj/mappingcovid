import json
import matplotlib.pyplot as plt

file = open('dataFile.json')
data = json.load(file)

ar = []
for i in data:
    text = data[i]['Text']
    pituus = len(text)
    ar.append(pituus)
    
plt.hist(ar, 13, range=(0, 2600))
plt.show()
