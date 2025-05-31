def f(a, sis):
    bibl = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = ''
    while a > 0:
        s = bibl[a % sis] + s
        a //= sis
    return s, sis


print(f(346654, 36))
print(int('346654', 36), 36)