from itertools import *
k = 0
for i in product('012345678', repeat = 5):
    s = ''.join(i)
    if s[0] != '0':
        if s.count('0') == 1:
            if s[4] != '0':
                if int(s[s.index('0') - 1]) % 2 != 0 and int(s[s.index('0') + 1]) % 2 != 0:
                    k += 1
            else:
                if int(s[s.index('0') - 1]) % 2 != 0:
                    k += 1
print(k)