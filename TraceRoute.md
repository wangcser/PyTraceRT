# 多种 Trace Route 方案对比
本项目测试了三种 traceroute 方法，现在对其效果总结如下。
TraceRoute 的本质在于在源节点到目的节点的报文上，通过在 IP 层设置不同的 TTL，利用 ICMP 协议对 TTL 超时的不同处理方式来获取沿途的路由信息。因此，通过选择不同的报文就能得到不同的 traceRoute 方法。

## ICMP TraceRoute

使用 ICMP 协议封装的 TraceRoute，IP 层之上是 ICMP 协议

采用 ICMP PING 方法进行测试，由于目的主机可能不会响应 PING，因此最后一个报文会不断重传，且得不到目的主机的响应，因此效果不好

## TCP TraceRoute

使用 TCP-SYN 过程封装的 TraceRoute，IP 层之上是 TCP 协议

该方法适用性最好

## UDP TraceRoute

使用 UDP 协议封装的 TraceRoute，IP 层之上是 UDP 协议

由于目的主机可能不会响应 UDP 报文，因此依然存在收不到最后一个报文的问题

