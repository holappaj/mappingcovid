import json
from pandas import DataFrame

def saveFile(dictionary, filename):
    with open(filename, 'w') as saveFile:
        json.dump(dictionary, saveFile, indent=4)

if __name__ == "__main__":
    file = open('communitiesData.json')
    data = json.load(file)
    
    num_iterations = 13

    meta_len_list = []
    for iteration in range(num_iterations+1):
        communities = data[str(iteration)]
        len_list = []
        for c in communities:
            len_list.append(len(c))
        meta_len_list.append(sorted(len_list, reverse=1))

    #creates list for the dataframe
    iteration_list = []
    for i in range(num_iterations + 1):
        iteration_list.append(i)

    d = {'iterations': iteration_list, 'community sizes': meta_len_list}
    df = DataFrame(data=d)

    #NOTE: ONLY THE LONGEST CONNECTED COMPONENT USED
    print(df)
    #        iterations                                community sizes
    #0            0                                              [105]
    #1            1                                           [95, 10]
    #2            2                                       [77, 18, 10]
    #3            3                                    [73, 18, 10, 4]
    #4            4                                 [70, 18, 10, 4, 3]
    #5            5                              [67, 18, 10, 4, 3, 3]
    #6            6                          [51, 18, 16, 10, 4, 3, 3]
    #7            7                       [47, 18, 16, 10, 4, 4, 3, 3]
    #8            8                    [45, 18, 16, 10, 4, 4, 3, 3, 2]
    #9            9                 [40, 18, 16, 10, 5, 4, 4, 3, 3, 2]
    #10          10             [29, 18, 16, 11, 10, 5, 4, 4, 3, 3, 2]
    #11          11          [29, 16, 13, 11, 10, 5, 5, 4, 4, 3, 3, 2]
    #12          12       [23, 16, 13, 11, 10, 6, 5, 5, 4, 4, 3, 3, 2]
    #13          13   [16, 13, 12, 11, 11, 10, 6, 5, 5, 4, 4, 3, 3, 2]

    repData = open('nameRep.json')
    repData = json.load(repData)
    overallList = []
    averageList = []

    for i in data[str(13)]:
        score = 0
        divider = 0
        for name in i:
            divider += 1
            try:
                score += int(repData[name])
            except:
                score +=0
#        try:
#            dic5[score] = dic5[score] + 1
#        except KeyError:
#            dic5[score] = 1
        point = (score / divider)
        overallList.append(score)
        averageList.append(point)
    print(averageList)
#    print(dic5)
    print(overallList)
#    saveFile(dic5, 'reputationClusters.json')
