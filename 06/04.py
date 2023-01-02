my_set = set()
n = int(input())
m = int(input())
s = n + m
for i in range(s):
    name = input()
    if name not in my_set:
        my_set.add(name)
    else:
        my_set.discard(name)
if my_set:
    print(len(my_set))
else:
    print('No')
