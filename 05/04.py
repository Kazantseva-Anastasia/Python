n = int(input())
for i in range(n):
    st = input()
    if ('кот' or 'Кот') in st:
        print('Meow')
        break
else:
    print('No')
