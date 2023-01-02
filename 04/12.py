n = int(input())
s = 0
for i in range(n):
    num = int(input())
    if i % 2 == 1:
        num = num - 2 * num
    s += num
print(s)
