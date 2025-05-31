import re
sp = []
for i in re.findall(r'([1-9][0-9]{3}[.][0-9]+&[1-9][0-9]{3}[.][0-9]+)', open('18597.txt').readline()):
    sp.append(len(i))
print(max(sp))