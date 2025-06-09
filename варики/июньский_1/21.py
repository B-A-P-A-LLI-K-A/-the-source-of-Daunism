def f(s, h, sp):
    if s >= 471:
        return h in sp
    elif h > max(sp):
        return 0
    else:
        if h % 2 == 0:
            return f(s + 4, h + 1, sp) and f(s + 7, h + 1, sp) and f(s * 4, h + 1, sp)
        else:
            return f(s + 4, h + 1, sp) or f(s + 7, h + 1, sp) or f(s * 4, h + 1, sp)


k = []
for i in range(1, 471):
    if f(i, 0, [2, 4]) and (not(f(i, 0, [2]))):
        k.append(i)
print(sum(k))