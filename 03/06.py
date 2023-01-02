a = input()
b = input()
while a != b or len(a) < 8 or '123' in a:
    if a != b:
        print('Различаются!')
        a = input()
        b = input()
    elif len(a) < 8:
        print('Короткий!')
        a = input()
        b = input()
    elif '123' in a:
        print('Простой!')
        a = input()
        b = input()
print('OK!')
