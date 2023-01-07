a = int(input())
for i in range(a, 0, -1):
    for b in range(a, 0, -1):
        if b == 1:
            print(chr(65 + a - b), end='')
            print(i)
        else:
            print(chr(65 + a -k), end='')
            print(i, end=' ')
