def f(s, h):
    if s <= 87 and h == 3:
        return 1
    if (s <= 87 and h != 3) or h > 3:
        return 0
    else:
        if h % 2 == 1:
            return f(s - 2, h + 1) and f(s // 2, h + 1)
        else:
            return f(s - 2, h + 1) or f(s // 2, h + 1)


for i in range(89, 300):
    if f(i, 0):
        print(i)