numbers = []
for i in range(int(input())):
    numbers.append(input())
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
for num in numbers:
    print(num)
