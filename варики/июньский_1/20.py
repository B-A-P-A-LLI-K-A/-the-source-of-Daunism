def f(s, h):
    if s >= 471:
        return h == 3
    elif h > 3:
        return 0
    else:
        if h % 2 == 1:
            return f(s + 4, h + 1) and f(s + 7, h + 1) and f(s * 4, h + 1)
        else:
            return f(s + 4, h + 1) or f(s + 7, h + 1) or f(s * 4, h + 1)


k = []
for i in range(1, 471):
    if f(i, 0):
        k.append(i)
print(min(k), max(k))