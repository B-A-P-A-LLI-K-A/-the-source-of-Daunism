def f(s1, s2, h):
    if (s1 + s2 > 80) and h == 2:
        return 1
    if ((s1 + s2 > 80) and h != 2) or h > 2:
        return 0
    else:
        if h % 2 == 0:
            return f(s1 + 1, s2, h + 1) or f(s1 * 2, s2, h + 1) or f(s1, s2 + 1, h + 1) or f(s1, s2 * 2, h + 1)
        else:
            return f(s1 + 1, s2, h + 1) or f(s1 * 2, s2, h + 1) or f(s1, s2 + 1, h + 1) or f(s1, s2 * 2, h + 1)


for i in range(1, 74):
    if f(7, i, 0):
        print(i)