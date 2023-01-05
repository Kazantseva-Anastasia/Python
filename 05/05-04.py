n = int(input())
for i in range(n):
    s = input()
    if ('кот' or 'Кот') in s:
        print('МЯУ')
        break
else:
    print('НЕТ')
    