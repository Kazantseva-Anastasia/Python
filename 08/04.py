a = int(input())
for i in range(a, 0, -1):
    for k in range(a, 0, -1):
        if k == 1:
            print(chr(65 + a - k), end='')
            print(i)
        else:
            print(chr(65 + a - k), end='')
            print(i, end=' ')
