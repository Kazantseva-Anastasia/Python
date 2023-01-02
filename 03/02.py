p = input("Введите пароль один: ")
p2 = input("Введите пароль два: ")
if len(p) < 8:
    print('Пароль короткий!')
elif p != p2:
    print('Пароли не совпадают!')
else:
    print('OK')
