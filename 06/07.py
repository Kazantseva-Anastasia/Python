my_set = set()
new_set = set()
m = int(input())
for i in range(m):
    n = int(input())
    for k in range(n):
        name = input()
        if i == 0:
            my_set.add(name)
        else:
            new_set.add(name)
    if i > 0:
        my_set = my_set & new_set
        new_set.clear()
for elem in my_set:
    print(elem)
