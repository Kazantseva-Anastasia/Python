flag = 'Нет'
numbers = []
for i in range(int(input())):
    num = int(input())
    numbers.append(num)
a = int(input())
for i in range(0, len(numbers) - 1):
    for k in range(1, len(numbers)):
        if numbers[i] * numbers[k] == a:
            flag = 'Да'
print(flag)
