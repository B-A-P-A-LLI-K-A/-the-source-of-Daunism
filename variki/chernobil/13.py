from ipaddress import *
n = ip_network('201.54.170.68/21', 0)
for i in n:
    print(i)