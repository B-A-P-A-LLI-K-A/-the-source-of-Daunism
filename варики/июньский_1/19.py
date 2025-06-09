def f(s, h):
    if s >= 471:
        return (h + 1) % 2
    elif h > 2:
        return 0
    else:
        if h % 2 == 0:
            return f(s + 4, h + 1) and f(s + 7, h + 1) and f(s * 4, h + 1)
        else:
            return f(s + 4, h + 1) or f(s + 7, h + 1) or f(s * 4, h + 1)


k = 0
for i in range(1, 471):
    if f(i, 0):
        k += 1
print(k)