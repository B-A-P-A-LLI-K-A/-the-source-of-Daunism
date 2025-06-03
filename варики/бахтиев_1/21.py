def f(s, h, sp):
    if s >= 54:
        if h in sp:
            return 1
        else:
            return 0
    elif h > max(sp):
        return 0
    else:
        if h % 2 == 0:
            return f(s + 2, h + 1, sp) and f(s * 2, h + 1, sp)
        else:
            return f(s + 2, h + 1, sp) or f(s * 2, h + 1, sp)


spi = []
for i in range(1, 54):
    if f(i, 0, [2, 4]) and (not(f(i, 0, [2]))):
        spi.append(i)
print(min(spi))