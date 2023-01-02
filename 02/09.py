a = int(input())
b = int(input())
c = int(input())
if a > b:
    if b > c:
        print(a, b, c)
    else:
        if a > c:
            print(a, c, b)
        else:
            print(c, a, b)
else:
    if b > c:
        if a > c:
            print(b, a, c)
        else:
            print(b, c, a)
    else:
        print(c, b, a)
