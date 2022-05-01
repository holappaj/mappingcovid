import matplotlib.pyplot as plt
import networkx as nx
import quotationNetwork

def getData():
    data = quotationNetwork.openFile("dataFile.json")
    dataDic = quotationNetwork.findQuote(data)
    return dataDic

def drawGraph(dic):
    G = nx.Graph()
    G.add_nodes_from(dic)
    for userName in dic:
        for name in dic[userName]:
            G.add_edge(name, userName)
    pos = nx.spring_layout(G, k=1.5, iterations=200)
    nx.draw(G, pos, with_labels=True, font_weight='bold', font_color='red')
    plt.show()


if __name__ == "__main__":
    dataDic = getData()
    drawGraph(dataDic)
