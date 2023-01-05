t = int(input())
a = 'МЯУ'
b = 'НЕТ'
text = ''
for i in range(t):
    text1 = input()
    if ('Кот' in text1) or ('кот' in text1):
        text = a
    if ('Пёс' in text1) or ('пёс' in text1):
        text = b
print(text)
