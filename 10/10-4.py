numbers = []
for i in range(int(input())):
    numbers.append(input())
for i in range(len(numbers) - 1):
    for a in range(len(numbers) - 1 - i):
        if len(numbers[a]) > len(numbers[a + 1]):
            numbers[a], numbers[a + 1] = numbers[a + 1], numbers[a]
        elif len(numbers[a]) == len(numbers[a + 1]) and numbers[a] > \
                numbers[a + 1]:
            numbers[a], numbers[a + 1] = numbers[a + 1], numbers[a]
for n in numbers:
    print(n)
