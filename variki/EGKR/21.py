def f(s, h):
    if s >= 132:
        if (h == 4 or h == 2):
            return 1
        else:
            return 0
    elif h > 4:
        return 0
    else:
        if h % 2 == 0:
            return f(s + 3, h + 1) and f(s + 6, h + 1) and f(s * 3, h + 1)
        else:
            return f(s + 3, h + 1) or f(s + 6, h + 1) or f(s * 3, h + 1)


for i in range(1, 132):
    if f(i, 0):
        print(i)