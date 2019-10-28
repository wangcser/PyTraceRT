import pandas as pd

dfbd = pd.read_csv("trbaidu.csv", header=None, sep='\\s+', names=["hop", "ip", "as"])
dfqq = pd.read_csv("trtencent.csv", header=None, sep='\\s+', names=["hop", "ip", "as"])

ipset1 = dfbd['ip'].drop_duplicates().to_list()
ipset2 = dfqq['ip'].drop_duplicates().to_list()

result = list(set(ipset1).union(set(ipset2)))

print(result)