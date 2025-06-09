import re
ch = r'([1-9]\d*[05]|[05])'
print(max([len(i.group()) for i in re.finditer(f'{ch}([+*]{ch})*', open('19970').readline())]))