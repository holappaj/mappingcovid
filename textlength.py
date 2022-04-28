import json
import numpy as np

file = open('dataFile.json')
data = json.load(file)

ar = []
for i in data:
    text = data[i]['Text']
    pituus = len(text)
    ar.append(pituus)
    
np_ar = np.array(ar)
sec1 = np.sum(np_ar < 200)
sec2 = np.sum(np_ar < 400) - np.sum(np_ar < 200)
sec3 = np.sum(np_ar < 600) - np.sum(np_ar < 400)
sec4 = np.sum(np_ar < 800) - np.sum(np_ar < 600)
sec5 = np.sum(np_ar < 1000) - np.sum(np_ar < 800)
sec6 = np.sum(np_ar > 1000)
print(sec1, sec2, sec3, sec4, sec5, sec6)
