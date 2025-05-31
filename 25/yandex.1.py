from re import fullmatch
def f(a):
    s = []
    for q in range(2, int(a ** 0.5) + 1):
        if a % q == 0:
            if a / q != q:
                s.append(q)
                s.append(a // q)
            else:
                s.append(q)
    return s
for i in range(1, 10 ** 7 + 1):
    if fullmatch(f'34[0123456789]8[0123456789]*9', str(i)):
        o = [f(u) for u in f(i)]
        if o.count([]) > 4:
            o.reverse()
            print(i, f(i)[len(f(i)) - o.index([]) - 1])