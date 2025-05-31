sp = []
for n in range(4, 10000):
    s = 0
    st = '4' + '1' * n
    while '411' in st or '1111' in st:
        if '411' in st:
            st = st.replace('411', '14')
        if '1111' in st:
            st = st.replace('1111', '1')
    for i in st:
        s += int(i)
    sp.append(s)
print(max(sp))
