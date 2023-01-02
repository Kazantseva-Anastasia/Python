num = 0
left = 1
right = 1000
ans = False
while not ans:
    num = (left + right) // 2
    print(num)
    a = input()
    if a == '>':
        left = num
        continue
    elif a == '<':
        right = num
        continue
    else:
        print('=')
        ans = True
