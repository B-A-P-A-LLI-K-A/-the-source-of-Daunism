from ipaddress import ip_network
spk = []
for i in range(1, 33):
    k = 0
    n = ip_network(f'111.233.75.16/{i}', 0)
    if str(n[0]) == '111.233.75.0':
        for u in n:
            k += 1
    spk.append(k)
print(max(spk))