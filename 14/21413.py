for x in '0123456789ABCDEFGHIJ':
    f = int(f'82934{x}2', 21) + int(f'2924{x}{x}7', 21) + int(f'67564{x}8', 21)
    if f % 20 == 0:
        print(f // 20)