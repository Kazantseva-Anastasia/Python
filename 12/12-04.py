numbers = input().split()
m, k = input().split()
n = 0
numbers = numbers[int(m):int(k) + 1]
for i in range(len(numbers)):
    n += (int(numbers[i]) * int(numbers[i]))
print(n)
