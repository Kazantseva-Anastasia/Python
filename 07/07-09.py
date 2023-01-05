text = input()
number = int(input())
if len(text) >= number:
    print(text[number-1])
else:
    print('Ошибка')
    