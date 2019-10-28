from scapy.layers.inet import traceroute

# refer: https://github.com/secdev/scapy/blob/master/scapy/layers/inet.py

trResults, unAnswered = traceroute(target="www.tencent.com",
                                   dport=80,
                                   minttl=1,
                                   maxttl=30,
                                   sport=80,
                                   timeout=5)

trResults.get_trace()