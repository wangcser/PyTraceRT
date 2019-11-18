import matplotlib.pyplot as plt
import networkx as nx
from log import log

import matplotlib as mpl

mpl.use('Agg')

log.info(mpl.get_backend())


def draw_topo(vertex, matrix, fig_path="./result/result.png"):
    G = nx.Graph()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i, j] == 1:
                G.add_edge(vertex[i], vertex[j])

    pos = nx.spring_layout(G)

    nx.draw(G, pos=pos,
            node_size=10, node_color='r',
            edge_color='grey', font_size=4, with_labels=True)

    # print(G.number_of_nodes())
    # print(G.number_of_edges())

    # 这里存在一个 graph drawing 的问题，如何去除重复，因此可能需要图形的数据信息

    plt.savefig(fig_path, dpi=500)
    log.info("result saved as: " + fig_path)
    log.info("log-file saved as: tr_Y-M-D_H_M_S.log")

    log.info("result raw data saved as: result.gml")
    nx.write_gml(G, "./result/result.gml")
