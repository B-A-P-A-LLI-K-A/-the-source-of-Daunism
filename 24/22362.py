import re
print(open('22362').readline().find(max([i[1] for i in re.finditer('(?=([1-9AB][0-9AB]*[0369]))', open('22362').readline())], key=lambda i: (len(i), -int(i, 12)))))