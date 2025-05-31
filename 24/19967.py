import re
print(max([len(i) for i in re.findall(f'AFD(?:0|[1-9][0-9]*)(?:[*+]0|[*+][1-9][0-9]*)*', open('19967').readline())]))