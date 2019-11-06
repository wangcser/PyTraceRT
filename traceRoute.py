from scapy.layers.inet import traceroute, RandShort
from log import log
from scapy.layers.inet import IP, TCP, UDP,  ICMP, sr
import pprint

# in traceroute we can choose tcp-syn, udp, icmp methods to discover route msg.
# tcp-syn has the best result, so we choose tcp-syn as the default method.

# ans, uans = sr(IP(dst=target, ttl=(1, 10)) / ICMP()) # tcmp method, use ping-reply method, dst-host may not reply
# ans, uans = sr(IP(dst=target, ttl=(1, 30)) / TCP(dport=80, flags="S")) # tcp-syn method, equal to trace_route method
# ans, unans = traceroute(target, l4=UDP(sport=80)) # udp method,dst-host may not reply


def trace_route(target, verbose=0, show=True, store=True):
    ans, uans = traceroute(target=target,
                           dport=80,
                           minttl=1,
                           maxttl=30,
                           sport=RandShort(),
                           timeout=5,
                           verbose=verbose)

    route_dict = ans.get_trace()

    dst = list(route_dict.keys())[0]
    src = route_dict[dst][1][0]

    log.info("trace route from " + src + " to " + dst)

    if show:
        log.info("route info: ")
        log.info(route_dict[dst])
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(route_dict)

    if store:
        file_name = src + "-" + dst
        with open("./RawTopoData/" + file_name + ".txt", 'w') as f:
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
        trace_route(ip, method='TCP', verbose=0, show=True, store=False)
