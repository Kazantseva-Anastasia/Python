word = True
s = -1
count = 1
while word:
    a = str(input())
    while (('кот' in a) or ('Кот' in a)) and (s == -1):
        if ('кот' in a) or ('Кот' in a):
            s = count
            break
    if a == 'СТОП':
        print(s)
        word = False
