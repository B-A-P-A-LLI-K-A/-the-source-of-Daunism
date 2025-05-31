s = 3 * 60 + 55
spt = []
while s > 0:
    print(s)
    n = input()
    k = input()
    spt.append([n, k])
    if (int(n.split(':')[0]) * 60 + int(n.split(':')[1])) <= (int(k.split(':')[0]) * 60 + int(k.split(':')[1])):
        s += int(n.split(':')[0]) * 60 + int(n.split(':')[1])
        s -= int(k.split(':')[0]) * 60 + int(k.split(':')[1])
    else:
        s += int(n.split(':')[0]) * 60 + int(n.split(':')[1]) - 24 * 60
        s -= int(k.split(':')[0]) * 60 + int(k.split(':')[1])
if s < 0:
    print(f'Задержка на {abs(s)} минут')
print(spt)