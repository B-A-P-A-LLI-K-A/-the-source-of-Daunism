import re
print(max([len(i.group()) for i in re.finditer(r'\d*[+*](\d+[+*])*\d*', open('24').readline())]))