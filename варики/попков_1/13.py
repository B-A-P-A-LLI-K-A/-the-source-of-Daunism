from ipaddress import ip_network
k = 0
n = ip_network('192.168.248.176/28', 0)
for i in n:
    if bin(int(i))[2:].count('0') == bin(int(i))[2:].count('1'):
        k += 1
print(k)