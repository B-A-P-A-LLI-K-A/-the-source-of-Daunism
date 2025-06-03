def f(s, h):
    if s >= 54:
        if h == 2:
            return 1
        else:
            return 0
    elif h > 2:
        return 0
    else:
        if h % 2 == 0:
            return f(s + 2, h + 1) and f(s * 2, h + 1)
        else:
            return f(s + 2, h + 1) or f(s * 2, h + 1)


spi = []
for i in range(1, 54):
    if f(i, 0):
        spi.append(i)
print(min(spi))