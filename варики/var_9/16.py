from math import prod
sp = [0 for _ in range(2001)]
for _ in range(3):
    sp.append(16)
for i in range(2000, 0, -1):
    sp[i] = 2 * sp[i + 3]
print(prod([int(i) for i in str(sp[50] // sp[110]) if i != '0']))