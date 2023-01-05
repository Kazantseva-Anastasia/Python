my_set = set()
n = int(input())
m = int(input())
a = n + m
for i in range(a):
    name = input()
    if name not in my_set:
        my_set.add(name)
    else:
        my_set.discard(name)
if my_set:
    print(len(my_set))
else:
    print('NO')
    