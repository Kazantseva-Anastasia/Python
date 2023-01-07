import string
text = string.ascii_lowercase
a = 0
name = input()
for i in range(10):
    text += str(i)
text += '_'
for i in range(len(name)):
    if name[i] not in text:
        print('Неверный символ:', name[i])
        break
    a += 1
    if a == len(name):
        print('OK')
