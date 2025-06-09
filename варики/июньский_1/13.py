from ipaddress import ip_network
k = 0
for i in range(1, 33):
    n = ip_network(f'192.214.116.184/{i}', 0)
    if bin(int(n[0]))[2:].count('1') % 5 == 0 and bin(int(n[0]))[2:].count('1') != 0:
        k += 1
        print(n[0], i)
print(k)