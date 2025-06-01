import re
print(max([len(i.group()) for i in re.finditer('(0|[2345][02345]*)([+*](0|[2345][02345]*))*', open('24').readline())]))