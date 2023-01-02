list1 = set()
list2 = set()
a = input()
while a != '':
    list1.add(a)
    a = input()
b = input()
while b != '':
    list2.add(b)
    b = input()
sect = list1 & list2
if sect:
    print(sect)
else:
    print('Empty')
