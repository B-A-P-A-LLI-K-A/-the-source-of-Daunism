def f(s1, s2, h):
    if (107 <= (s1 + s2) <= 170 and (h == 2 or h == 4)) or (s1 + s2 >= 171 and (h == 3 or h == 5)):
        return 1
    if (107 <= (s1 + s2) <= 170 and (h != 2 or h != 4)) or (s1 + s2 >= 171 and (h != 3 or h != 5)) or h > 5:
        return 0
    else:
        if h % 2 == 1:
            return f(s1 + 10, s2, h + 1) or f(s1 * 2, s2, h + 1) or f(s1, s2 + 10, h + 1) or f(s1, s2 * 2, h + 1)
        else:
            return f(s1 + 10, s2, h + 1) and f(s1 * 2, s2, h + 1) and f(s1, s2 + 10, h + 1) and f(s1, s2 * 2, h + 1)


for i in range(1, 101):
    if f(5, i, 0):
        print(i)
