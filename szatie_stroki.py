s = str(input())
k = ''
l = 1
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        l += 1
    else:
        if l != 1:
            k = k + str(l) + s[i - 1]
        else:
            k = k + s[i - 1]
        l = 1
    if i == len(s) - 1:
        if l != 1:
            k = k + str(l) + s[i]
        else:
            k = k + s[i]
print(k)