def f(a):
    s = ''
    while a > 0:
        s = str(a % 5) + s
        a //= 5
    return s


spn = []
for n in range(1, 10000):
    q = f(n)
    if len(q) % 2 == 0:
        q = q[:len(q) // 2] +'0' + q[len(q) // 2:]
    r = int(q)
    if r <= 250:
        spn.append(n)
print(max(spn))