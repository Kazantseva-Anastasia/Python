flag = True
s = 0
count = 0
a = 0
num = int(input())
while num != 0:
    s += num
    a += 1
    if s == 10 and flag:
        flag = False
        count = a
    num = int(input())
print(count)
