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
def r(u):
    p = []
    for w in u:
        k = 0
        for y in range(2, int(w ** 0.5) + 1):
            if w % y == 0:
                k = 1
                break
        if k == 0:
            p.append(w)
    return p
for i in range(1, 10 ** 7 + 1):
    if fullmatch(f'34[0123456789]8[0123456789]*9', str(i)):
        x = r(f(i))
        if len(x) > 4:
            print(i, max(x))