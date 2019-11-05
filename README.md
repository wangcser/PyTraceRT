# PyTraceRT

本项目基于 traceroute 原理通过给定的一组 IP（或者域名）探测节点之间网络可能呈现的拓扑结构。

### To Do List:
- [x] 基础：实现基本的 traceroute 功能
- [ ] 进阶：实现高可用的 traceroute 功能，包括 TCP-SYN，UDP，ICMP 三种 traceroute 方法
- [x] 基础：找到一种处理多源路由路径信息的方法，得到 topo 的数学表示
- [ ] 进阶：证明该 topo 计算方法的正确性，并对其进行优化
- [x] 基础：绘制基础的 topo 图，进行简单标注，并给出详细的 topo 数据
- [ ] 进阶：调整图像，解决布局问题（使用地理位置信息是一个非常棒的解决方案）
- [x] 基础：调整并优化项目结构
- [x] 基础：实现一个日志模块
- [ ] 优化：对核心模块进行测试，补充简单的边界情况
- [ ] 优化：在入口处定义清晰运作流程，考虑到多点测试的和多源数据融合的问题
- [ ] 基础：提供基于 CLI 的软件交互方式和基于 exe 的封装方式
- [ ] 优化：优化交付软件的体积
- [ ] 优化：实现一个 GUI 界面，方便用户使用
- [ ] 基础：完成软件的使用文档，介绍原理和使用方法以及如何对结果进行分析
- [ ] 优化：完成 README 文档和设计文档，介绍工具的设计和运作机制

## Functions to be discussed

- 是否需要一个 GUI 界面

## Use Case

## Manual

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