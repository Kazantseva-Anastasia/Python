eng = set()
deu = set()
n = int(input())
m = int(input())
for i in range(n):
    name = input()
    eng.add(name)
for i in range(m):
    name = input()
    deu.add(name)
s = eng ^ deu
if s:
    print(len(s))
else:
    print('No')
