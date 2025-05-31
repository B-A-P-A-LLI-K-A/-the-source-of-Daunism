for n in range(1, 10000):
    q = bin(n)[2:]
    if sum([int(i) for i in q]) % 2 == 0:
        q = '10' + q[2:] + '0'
    else:
        q = '11' + q[2:] + '1'
    r = int(q, 2)
    if r > 19:
        print(n)
        break