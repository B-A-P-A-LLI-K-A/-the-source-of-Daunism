from ipaddress import *
n = ip_network('218.194.82.148/26', 0)
for i in n:
    print(i)