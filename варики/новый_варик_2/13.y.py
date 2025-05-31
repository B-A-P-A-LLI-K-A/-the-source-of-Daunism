from ipaddress import *
k = 0
net = ip_network('172.16.80.0/21')
for n in net:
    if bin(int(n)).count('1') % 2 == 1:
        k += 1
print(k)