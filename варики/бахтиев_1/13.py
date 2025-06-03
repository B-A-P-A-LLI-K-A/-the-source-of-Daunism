from ipaddress import *
k = 0
n = ip_network('228.172.236.0/20', 0)
for i in n:
    if bin(int(i))[2:].count('1') % 5 != 0:
        k += 1
print(k)