n = int(input())
for i in range(n):
    space = (abs(i-n) - 1) * ' '
    star = (2*i+1) * '*'
    print(space, star, space, sep='')
