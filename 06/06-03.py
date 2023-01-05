en = set()
nem = set()
n = int(input())
m = int(input())
for i in range(n):
    name = input()
    en.add(name)
for i in range(m):
    name = input()
    nem.add(name)
a = en ^ nem
if a:
    print(len(a))
else:
    print('NO')
    