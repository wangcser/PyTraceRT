import warnings

warnings.filterwarnings("ignore")   # ignore matplotlib warnings

from traceRoute import trace_route
from calTopo import cal_adj_mat
from drawTopo import draw_topo
from log import log
import os


if __name__ == "__main__":

    # pre work: add log config
    log.info("Topo Discovery task started.")

    val = input("Please choose a program function:\n"
                "   collect and calculate: input 1\n"
                "   collect route message: input 2\n"
                "   calculate topo graph : input 3\n")

    if val == '1' or val == '2':
        # 1. use traceroute module collect route data
        log.info("start collect route msg.")

        # read ip list in file
        log.info("read ip in path \"./ip_list/inet_ip_list.txt\".")
        ip_list = []
        with open("./ip_list/inet_ip_list.txt", "r") as f:
            for line in f.readlines():
                ip_list.append(line.strip('\n'))
        log.info("read ip list finished, got " + str(len(ip_list)) + " ips.")

        # trace route in ip list
        for ip in ip_list:
            try:
                trace_route(target=ip)
            except ConnectionError:
                log.warning(ip + " traceroute failed.")

        log.info("all routes collected.")

    if val == '1' or val == '3':
        # 2. cal topo msg use adj-matrix
        log.info("start cal topo.")
        try:
            vertex, matrix = cal_adj_mat()
        except IOError:
            log.warning("please check out input data!")

        # 3. draw topo
        log.info("start draw topo graph.")
        try:
            draw_topo(vertex, matrix)
        except EnvironmentError:
            log.warning("please check out draw-related modules!")

    log.info("task finished.")

    os.system("pause")


