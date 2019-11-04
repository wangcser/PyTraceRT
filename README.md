# PyTraceRT
### ToDo:
1. 目前已经跑通了所有的流程，下一步就在于优化好每一个模块



本项目用于探测并可视化给定局域网的拓扑信息，工作流程如下：

- 从给定的节点组出发，两两检查 route 信息，通过 traceroute 原理获取给定节点之间所有可能的连接情况
- 合并所有的节点表，得到网络表
- 通过网络表绘制局域网的拓扑信息
## 1. TraceRoute
1. 给定源主机和目的节点地址，在源主机上获取到目的地址的 route 信息
2. 由于目的地址会有很多个，因此对于每一个目的地址都会进行一次 traceroute
3. 因此，点对点的 traceroute 模块会是本项目的核心模块
4. 重复上述过程，得到源节点到目的节点组的所有 route 信息，然后持久化并写入日志
5. 值得注意的是，可以通过 scapy 实现多种 traceroute，需要解析其返回的状态码和各种方案的使用，以此来增强程序的健壮性
### Scapy State Code
- SA:SYN-ACK
- RA:RST-ACK

TCP标记和他们的意义如下所列：

* F : FIN - 结束; 结束会话
* S : SYN - 同步; 表示开始会话请求
* R : RST - 复位;中断一个连接
* P : PUSH - 推送; 数据包立即发送
* A : ACK - 应答
* U : URG - 紧急
* E : ECE - 显式拥塞提醒回应
* W : CWR - 拥塞窗口减少

```
icmptypes = 11: "time-exceeded"
```

ICMP 11: Time-Exceeed

## 2. Marge and Cal route message
1. we have 1 node to others route messages, and many this type messages need to be marged.
2. use graph and matrix methods to marge these route info.
3. 这里使用矩阵法，首先合并所有的 ip 地址，然后使用邻接矩阵标记即可
## 3. draw topo graph and tag labels
1. use lab to draw related info.