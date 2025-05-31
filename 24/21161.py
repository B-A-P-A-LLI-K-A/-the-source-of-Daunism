import re
print(max([len(i) for i in re.findall(f'[ABC][abc]*[ ](?:[ABCabc][abc]*[ ])*[ABCabc][abc]*[.]', open('21161').readline())]))