def f(s, h):
    if s <= 10:
        if h == 2:
            return 1
        else:
            return 0
    elif h > 2:
        return 0
    else:
        if h % 2 == 0:
            return f(s - 1, h + 1) or f(s - 3, h + 1) or f(s // 3, h + 1)
        else:
            return f(s - 1, h + 1) or f(s - 3, h + 1) or f(s // 3, h + 1)


for i in range(500, 10, -1):
    if f(i, 0):
        print(i)
        break