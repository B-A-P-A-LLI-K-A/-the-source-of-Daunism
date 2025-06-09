import ipaddress
s = 0
for k in range(16, 32):
    n = ipaddress.ip_network(f'205.154.212.20/{k}', 0)
    for i in n:
        if str(i) == '205.154.192.0':
            print(k)