number = int(input())
n = number + 1
c = 0
for i in range(1, n):
    if (number % i) == 0:
        if i == number:
            print(i, end='')
        else:
            print(i, end='')
        c += 1
if c > 2:
    print('\nНЕТ')
elif number == 1:
    print('\nНЕТ')
else:
    print('\nПРОСТОЕ')
