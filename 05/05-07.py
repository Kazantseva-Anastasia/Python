text = int(input())
ev = 'Евразия'
os = 'Остазия'
a = ''
for i in range(text):
    q = input()
    if q == 'С кем война?':
        print(ev)
    if q == 'С кем мир?':
        print(os)
    if q == 'Меняем':
        a = ev
        ev = os
        os = a
        