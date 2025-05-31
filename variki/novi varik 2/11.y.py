n = '1' + 90 * '0'
while '1' in n:
    if '10' in n:
        n = n.replace('10', '0001')
    else:
        n = n.replace('1', '000')
print(n.count('0'))