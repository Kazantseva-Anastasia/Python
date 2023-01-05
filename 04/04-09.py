n = int(input())
for i in range(n):
    s = (abs(i-n) - 1) * ' '
    stars = (2*i+1) * '*'
    print (s, stars, s, stars, sep+'')

