from calTopo import cal_adj_mat
from drawTopo import draw_topo
from log import log


# this test case use to test graph module.
# given route message, figure out the code can draw the graph correctly.

if __name__ == "__main__":

    vertex, matrix = cal_adj_mat("TestTopoData/")

    draw_topo(vertex, matrix, "TestResult/TestResult.png")
