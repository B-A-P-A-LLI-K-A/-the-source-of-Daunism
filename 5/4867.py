sp = []
for n in range(2, 2022):
    c = sum([int(i) for i in str(n) if int(i) % 2 == 0])
    nc = sum([int(str(n)[i]) for i in range(len(str(n))) if int(i) % 2 == 1])
    r = abs(nc - c)
    if r == 9:
        sp.append(n)
print(min(sp))
