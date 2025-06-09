sp = [66 for _ in range(1000)]
for i in range(1000, 200000):
    sp.append(sp[i - 5] + 100)
print(sp[180000] - sp[100000])