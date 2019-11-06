from traceRoute import trace_route
from calTopo import cal_adj_mat
from drawTopo import draw_topo
from log import log
import os


if __name__ == "__main__":

    # pre work: add log config
    log.info("topo discovery started.")

    log.warning("make sure you have fill the ip list msg in folder ip_list.")

    # 1. use traceroute collect route data
    log.info("start collect route msg.")

    # read ip list in file
    ip_list = []
    with open("./ip_list/inet_ip_list.txt", "r") as f:
        for line in f.readlines():
            ip_list.append(line.strip('\n'))
    log.info("read ip list in file finished, we got " + str(len(ip_list)) + " ips.")

    # trace route in ip list
    for ip in ip_list:
        try:
            trace_route(target=ip)
        except:
            log.info(ip + "failed.")

    log.info("all routes msg collected.")

    # 2. cal topo msg use adj-matrix
    log.info("start cal topo msg.")
    vertex, matrix = cal_adj_mat()

    # 3. draw topo
    log.info("start draw topo graph.")
    draw_topo(vertex, matrix)

    os.system("pause")

