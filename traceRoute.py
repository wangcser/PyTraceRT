from scapy.layers.inet import traceroute
from log import log
import pprint


# refer: https://github.com/secdev/scapy/blob/master/scapy/layers/inet.py
# refer: https://0xbharath.github.io/art-of-packet-crafting-with-scapy/network_recon/traceroute/index.html
# we can use tcp-syn, udp, icmp to implement traceroute methods.


def trace_route(target, verbose=0, show=True, store=True):

    ans, uans = traceroute(target=target,
                           dport=80,
                           minttl=1,
                           maxttl=30,
                           sport=80,
                           timeout=5,
                           verbose=verbose)

    route_dict = ans.get_trace()

    dst = list(route_dict.keys())[0]
    src = route_dict[dst][1][0]

    log.info("trace route from " + src + " to " + dst)

    if show:
        log.info("route info: ")
        log.info(route_dict[dst])
        # pretty display
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(route_dict[dst])

    if store:
        file_name = src + "-" + dst
        with open("RawTopoData/" + file_name + ".txt", 'w') as f:
            for iter in route_dict[dst]:
                f.write(route_dict[dst][iter][0] + "\n")

        log.info(file_name + " stored.")


if __name__ == "__main__":

    ip_list = [
        "www.uestc.edu.cn",
        "www.baidu.com",
        "www.tencent.com",
        "www.cctv.com",
        "www.google.com.hk"
    ]

    for ip in ip_list:
        trace_route(target=ip)
