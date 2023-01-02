n = int(input())
euro = 'Евразия'
ost = 'Остазия'
s = ''
for i in range(n):
    com = input()
    if com == 'С кем война?':
        print(euro)
    if com == 'С кем мир?':
        print(ost)
    if com == 'Меняем':
        s = euro
        euro = ost
        ost = s
