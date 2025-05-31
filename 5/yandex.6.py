from math import prod
def f(a):
    s = ''
    while a > 0:
        s = str(a % 6) + s
        a //= 6
    return s


spn = []
for n in range(1, 10000):
    q = f(n)
    if q.count('0') >= 2:
        w = ''
        for i in q:
            if i == '0':
                w += '5'
            else:
                w += i
        q = w
    if int(f(n)[0]) % 2 == 0:
        q = f(n % 6) + q
    else:
        q += f(prod([int(i) for i in q]))
    r = int(q, 6)
    if r < 109:
        spn.append(n)
print(max(spn))