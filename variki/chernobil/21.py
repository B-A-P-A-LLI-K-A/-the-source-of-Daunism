def f(s, h, sp):
    if s <= 10:
        if h in sp:
            return 1
        else:
            return 0
    elif h > max(sp):
        return 0
    else:
        if h % 2 == 0:
            return f(s - 1, h + 1, sp) and f(s - 3, h + 1, sp) and f(s // 3, h + 1, sp)
        else:
            return f(s - 1, h + 1, sp) or f(s - 3, h + 1, sp) or f(s // 3, h + 1, sp)


for i in range(11, 500):
    if f(i, 0, [2, 4]) and not(f(i, 0, [2])):
        print(i)
        break