import json
import networkx as nx

def create_graph(data):
    G = nx.Graph()
    G.add_nodes_from(data)
    for userName in data:
        for name in data[userName]:
            G.add_edge(name, userName)
    return G

def create_GN_dic(graph, iterations):
    start_comm = list(graph.nodes())
    comm_dic = {0: [start_comm]}
    communities = nx.community.girvan_newman(graph)

    for i in range(iterations):
        comm_list = []
        for c in next(communities):
            comm_list.append(list(c))
        comm_dic[i+1] = comm_list
    return comm_dic

if __name__ == "__main__":
    file = open('quoteData.json')
    data = json.load(file)
    G = create_graph(data)

    #graph of the longest connected component
    connected_components = [comp for comp in sorted(nx.connected_components(G), key=len, reverse=True)]
    G1 = G.subgraph(connected_components[0]).copy()

    iterations = 25 #how many iterations of the algorithm will be saved
    comm_dic = create_GN_dic(G1, iterations)

    with open('communitiesData.json', 'w') as file:
        json.dump(comm_dic, file, indent=4)
