n = int(input())
s = 0
for i in range(n):
    number = int(input())
    if i % 2 == 1:
        number = number - 2 * num
    s += number
print(s)