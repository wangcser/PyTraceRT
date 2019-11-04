from traceRoute import tr
from calTopo import cal_adj_mat
from drawTopo import draw_topo


if __name__ == "__main__":

    # 1. traceroute data
    ip_list = []
    with open("test_case/camp_ip_list.txt", "r") as f:
        for line in f.readlines():
            ip_list.append(line.strip('\n'))

    for ip in ip_list:
        tr(target=ip)

    # 2. cal adj-matrix
    vertex, matrix = cal_adj_mat()

    # 3. draw topo
    draw_topo(vertex, matrix)