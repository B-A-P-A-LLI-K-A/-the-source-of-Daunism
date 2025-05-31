import re
print(max([len(i) for i in re.findall(f'(?:[1-9, AB][0-9, AB]*[2468A])', open('24').readline())]))