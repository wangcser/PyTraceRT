import matplotlib.pyplot as plt
import networkx as nx


def draw_topo(vertex, matrix):
    G = nx.Graph()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i, j] == 1:
                G.add_edge(vertex[i], vertex[j])

    nx.draw(G,
            node_size=20, node_color='r',
            edge_color='grey', font_size=10, with_labels=True)

    # print(G.number_of_nodes())
    # print(G.number_of_edges())

    plt.axis('equal')
    plt.show()
