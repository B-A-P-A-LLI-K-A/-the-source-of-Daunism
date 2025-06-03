import re
for i in range(2025, 10 ** 10 + 1, 2025):
    if re.fullmatch(r'21\d3\d*145\d5', str(i)):
        print(i, i // 2025)