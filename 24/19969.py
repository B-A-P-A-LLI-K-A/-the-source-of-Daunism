import re
print(max(len(i) for i in re.findall(r'([a-z]+@[a-z]+[.][a-z]+)', open('19969').readline())))