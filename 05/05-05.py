a = 1
number = -1
stop = True
while stop:
    text = input()
    while (('Кот' in text) or ('кот' in text)) and (number == -1):
        if ('Кот' in text) or ('кот' in text):
            number = a
            break
    if ('Кот' in text) or ('кот' in text):
        print(number)
        break
    if text == 'СТОП':
        print(number)
        stop = False
        