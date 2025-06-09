for x in '0123456789ABCD':
    s = int(f'4B3{x}1C7', 14) + int(f'5{x}G83F7', 17)
    if s % 15 == 0:
        print(s // 15)