import string
text = string.ascii_lowercase
k = 0
name = input()
for i in range(10):
    text += str(i)
text += '_'
for i in range(len(name)):
    if name[i] not in text:
        print('Неверный символ:', name[i])
        break
    k += 1
    if k == len(name):
        print('OK')
