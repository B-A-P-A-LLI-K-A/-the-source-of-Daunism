import re
for i in range(2025, 10 ** 10 + 1, 2025):
    if re.fullmatch('21[0123456789]5846[0123456789]*[0123456789]', str(i)):
        print(i, i // 2025)