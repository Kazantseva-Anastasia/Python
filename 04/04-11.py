n = int(input())
s = 0
for i in range(n):
    curr = int(input())
    if i == 0:
        print(0)
    else:
        if curr > (s/i):
            print('>')
        elif curr < (s/i):
            print('<')
        else:
            print(0)
