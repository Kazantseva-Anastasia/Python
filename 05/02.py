n = int(input())
text = ''
for i in range(n):
    st = input()
    if i == n-1:
        text += st
    else:
        text += st + ' '
if 'Кот' or 'кот' in text:
    print('Мяу')
else:
    print('Нет')
