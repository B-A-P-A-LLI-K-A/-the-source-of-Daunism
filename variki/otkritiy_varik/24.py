import re
print(max([len(i.group()) for i in re.finditer('[123456789ABCD][0123456789ABCD]*[02468AC]', open('24').readline())]))