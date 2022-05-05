import json
import matplotlib.pyplot as plt
import networkx as nx

def create_graph(data):
    G = nx.Graph()
    G.add_nodes_from(data)
    for userName in data:
        for name in data[userName]:
            G.add_edge(name, userName)
    return G


def get_avg(dic, nodes):
    avg_value = 0
    for node in dic:
        node_value = dic[node]
        avg_value = avg_value + node_value
    return avg_value / nodes


def boxplot(data):
    fig = plt.figure(figsize =(7, 7))
    ax = fig.add_subplot()
    ax.set_xticklabels(['degree centrality', 'closeness centrality'])

    plt.boxplot(data)
    plt.show()


if __name__ == "__main__":
    file = open('quoteData.json')
    data = json.load(file)

    G = create_graph(data)

    nodes = len(list(G.nodes()))
    edges = len(list(G.edges()))
    #diameter = nx.diameter(G)

    connected_components = [comp for comp in sorted(nx.connected_components(G), key=len, reverse=True)]
    nmb_connected_components = len(connected_components)
    longest_component = G.subgraph(connected_components[0]).copy()
    diameter_of_comp = nx.diameter(longest_component)

    avg_cc = nx.average_clustering(G)
    degree_data = nx.degree_centrality(G)
    closeness_data = nx.closeness_centrality(G)
    avg_degree = get_avg(degree_data, nodes)
    avg_closeness = get_avg(closeness_data, nodes)

    #nx.draw_networkx(G)
    #plt.show()

    print(nodes, edges, diameter_of_comp, nmb_connected_components, avg_cc, avg_degree, avg_closeness)
    #nodes: 126
    #edges: 186
    #graph is not connected -> diameter is infinity
    #diameter of longest component: 8
    #connected components: 11
    #average clustering coefficient: 0.08453372905753857
    #average degree centrality: 0.023619047619047633
    #average degree closeness centrality: 0.20470759143266876


    #plotting
    degree_values = [degree_data[node] for node in degree_data]
    closeness_values = [closeness_data[node] for node in closeness_data]

    fig = plt.figure()
    gs = fig.add_gridspec(2, hspace=0.5)
    axs = gs.subplots()
    axs[0].hist(degree_values, 20)
    axs[0].set_title('degree centrality')
    axs[1].hist(closeness_values, 20)
    axs[1].set_title('closeness centrality')
    plt.show()

    boxplot([degree_values, closeness_values])
