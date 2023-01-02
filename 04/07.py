num = int(input())
n = num + 1
count = 0
for i in range(1, n):
    if (num % i) == 0:
        if i == num:
            print(i, end='')
        else:
            print(i, end=' ')
        count += 1
if count > 2:
    print('\nНет')
elif num == 1:
    print('\nНет')
else:
    print('\nПростое')
