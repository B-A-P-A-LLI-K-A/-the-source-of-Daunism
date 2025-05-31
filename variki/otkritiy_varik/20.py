def f(s, h):
    if s >= 67:
        if h == 3:
            return 1
        else:
            return 0
    elif h > 3:
        return 0
    else:
        if h % 2 == 1:
            return f(s + 1, h + 1) and f(s + 4, h + 1) and f(s * 3, h + 1)
        else:
            return f(s + 1, h + 1) or f(s + 4, h + 1) or f(s * 3, h + 1)


for i in range(1, 67):
    if f(i, 0):
        print(i)