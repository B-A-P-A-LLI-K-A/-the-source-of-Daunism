sp = [int(i) for i in open('17')]
k = []
for i in range(len(sp) - 1):
    if sum([sp[i + p] % 77 for p in range(2)]) == min(sp):
        k.append(sum([sp[i + p] for p in range(2)]))
print(len(k), max(k))