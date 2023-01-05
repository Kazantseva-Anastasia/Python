a = int(input())
text = ''
for i in range(a):
    n = input()
    if i == a-1:
        text += n
    else:
        text += n + ' '
if 'Кот' or 'кот' in text:
    print('МЯУ')
else:
    print('НЕТ')
