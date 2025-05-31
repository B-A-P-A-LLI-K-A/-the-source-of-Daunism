from ipaddress import ip_network
n = ip_network('98.81.154.195/14', 0)
for i in n:
    print(i)