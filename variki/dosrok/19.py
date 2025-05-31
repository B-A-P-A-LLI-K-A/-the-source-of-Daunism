def f(s, h):
    if s <= 87 and h == 2:
        return 1
    if (s <= 87 and h != 2) or h > 2:
        return 0
    else:
        if h % 2 == 0:
            return f(s - 2, h + 1) and f(s // 2, h + 1)
        else:
            return f(s - 2, h + 1) or f(s // 2, h + 1)


for i in range(89, 200):
    if f(i, 0):
        print(i)
        break