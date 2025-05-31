from ipaddress import ip_network
n = ip_network('143.168.72.213/28', 0)
for i in n:
    print(i)