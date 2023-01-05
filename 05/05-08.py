c = 0
a = 1
number = -1
text = input()
while text != 'СТОП':
    while (('Кот' in text) or ('кот' in text)) and (number == -1):
        if ('Кот' in text) or ('кот' in text):
            number = a
            break
    if ('Кот' in text) or ('кот' in text):
        c += 1
    a += 1
    text = input()
print(c, number)
