import re
from re import *
s = open('21597').readline()
numb = r'([1-5][0-5]*|0)'
reg = rf'{numb}(\*{numb})*(-{numb})*'
for x in re.finditer(reg, s):
    print(x.group())