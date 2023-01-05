flag = True
a = 0
c = 0
b = 0
number = int(input())
while number != 0:
    a += number
    b += 1
    if a == 10 and flag:
        flag = False
        c = b
    number = int(input())
print(c)
