sp = [int(i) for i in open('17')]
k = []
m = sum(sp) / len(sp)
for i in range(len(sp) - 1):
    if abs(sum([sp[i + u] for u in range(2)])) > m:
        k.append(sum([sp[i + u] for u in range(2)]))
print(len(k), abs(min(k)))