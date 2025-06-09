sp = {0 : 0}
for n in range(1, 9):
    sp[n] = n // 3 + n % 3
for n in range(9, 9 ** 9 + 1):
    sp[n] = sp[n // 9] + sp[n % 9]
    if n / 10000000 > 0:
        if n / 10000000 == int(n / 10000000):
            print(n)
k = 0
for i in sp.values():
    if i == 33:
        k += 1
print(k)