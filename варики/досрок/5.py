for u in range(1, 1000):
    n = bin(u)[2:]
    if n.count('1') % 2 == 0:
        n = '10' + n[2:] + '0'
    else:
        n = '11' + n[2:] + '1'
    if int(n, 2) > 480:
        print(u)
        break