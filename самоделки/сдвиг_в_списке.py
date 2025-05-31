s = str(input()).split(' ')
k = int(input())
sp = [0] * len(s)
for i in range(len(s)):
    if i < len(s) - k:
        sp[i + k] = s[i]
    else:
        sp[i + k - len(s)] = s[i]
print(sp)