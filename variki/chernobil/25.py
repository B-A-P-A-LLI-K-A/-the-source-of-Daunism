def f(a):
    return sum([t for t in range(2, a // 2 + 1) if a % t == 0])


o = 0
for i in range(650001, 700000):
    if str(f(i))[-2:] == '28':
        print(i, f(i))
        o += 1
        if o == 6:
            break