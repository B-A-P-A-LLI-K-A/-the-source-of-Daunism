def f(s, h):
    if s > 312 and (h == 2 or h == 4):
        return 1
    if s > 312 and (h != 2 or h != 4) or h > 4:
        return 0
    else:
        if h % 2 == 0:
            return f(s + 2, h + 1) and f(s + 3, h + 1) and f(s * 3, h + 1)
        else:
            return f(s + 2, h + 1) or f(s + 3, h + 1) or f(s * 3, h + 1)


for i in range(1, 313):
    if f(i, 0):
        print(i)
