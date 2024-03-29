# PyTraceRT

本项目基于 traceroute 原理通过给定的一组 IP（或者域名）探测节点之间网络可能呈现的拓扑结构。

### To Do List:
- [x] 基础：实现基本的 traceroute 功能
- [x] 进阶：实现高可用的 traceroute 功能，包括 TCP-SYN，UDP，ICMP 三种 traceroute 方法（使用 TCP-SYN 的方案可用性最好）
- [x] 基础：找到一种处理多源路由路径信息的方法，得到 topo 的数学表示
- [x] 进阶：证明该 topo 计算方法的正确性，并对其进行优化（使用测试拓扑完成验证）
- [x] 基础：绘制基础的 topo 图，进行简单标注，并给出详细的 topo 数据
- [x] 进阶：调整图像，解决布局问题（使用地理位置信息是一个非常棒的解决方案）
- [x] 基础：调整并优化项目结构
- [x] 基础：实现一个日志模块
- [x] 优化：对核心模块进行测试，补充简单的边界情况
- [x] 优化：在入口处定义清晰运作流程，考虑到多点测试的和多源数据融合的问题（实现了多种工功能）
- [x] 基础：提供基于 CLI 的软件交互方式和基于 exe 的封装方式（使用 pyinstaller 将所有文件打包为一个文件打包成功）
- [x] 多平台兼容性测试（windows7，windows10）
- [x] 基础：完成软件的使用文档，介绍原理和使用方法以及如何对结果进行分析
- [x] 优化：完成 README 文档和设计文档，介绍工具的设计和运作机制
- [x] 为程序设计一个图标
- [ ] 优化：优化交付软件的体积【需要重新建立新的 python 环境】

## Manual

>  详见 manual.md

## Design

项目结构

```
main.py -- 入口
traceRoute.py -- 点对点的探测路由信息
calTopo.py -- 通过多个点对的陆游信息计算拓扑图
drawTopo.py -- 通过拓扑图绘制图信息
log.py -- 封装的日志记录模块
test.py -- 核心功能的测试模块
IPResolve.py -- IP 地址解析模块，在项目中未被启用
CLI.py -- CLI 软件
GUI.py -- GUI 软件
RawTopoData/ -- 存储点对点的路由信息（以 list 方式存储）
result/ -- 存储探测结果和程序运行的日志
test_case/ -- 软件的输入数据，存放探测用的 ip 地址集合（以 list 方式写入）
```

## Methods

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
## 2. Marge and Cal route message
1. we have 1 node to others route messages, and many this type messages need to be marged.
2. use graph and matrix methods to marge these route info.
3. 这里使用矩阵法，首先合并所有的 ip 地址，然后使用邻接矩阵标记即可
## 3. Draw topo graph and tag labels
1. use lab to draw related info.

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

## 其他问题

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

### pyinstaller 发布脚本

```python
pyinstaller topoDiscovery.py --onefile -i topo.ico
```

## DEBUG

**以一种访问权限不允许的方式做了一个访问套接字的尝试**

这种错误是两种方面的原因，1：查看使用的端口是福被占用， 解决方法：cmd  ->  netstat -ano即可查看端口是否被占用，如果被占用，则修改端口。2：程序权限不够。解决办法：如果是在VS编程中，则让VS以管理员的方式启动，则不会报Socket错误，生成的应用程序也需要以管理员启动。

**windows native L3 raw socket are only usable as administrator**

>  https://stackoverflow.com/questions/22573894/how-to-workaround-the-limitations-on-raw-sockets-under-windows-7 

After Windows XP Service Pack 1, the ability to send raw sockets has been disabled, however you can still read them.

You can modify the source code example provided by Microsoft in the WDK to enable raw sends again. For more information, check the link.

[PCAUSA - How To Access To NIC Drivers From A Win32 Application](https://web.archive.org/web/20151121110106/http://www.rawether.net:80/product/tour02.htm)

Alternatively, you may use WinPcap to inject packets into the network.

[WinPcap](http://www.winpcap.org/)

**cannot mix incompatible Qt library**

计算机已有的 Qt 库和程序使用的 Qt 库版本不兼容

使用其他非交互式的 matplotlib 后端

打包比较大的问题

需要选择一个纯净的 Python 环境重新打包即可