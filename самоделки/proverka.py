from ipaddress import ip_network
sp = ['12', '13', '20', '21', '29', '30', '31', '32']
for i in sp:
    n = ip_network(f'192.214.116.184/{i}', 0)
    print(bin(int(n[0]))[2:].count('1'))