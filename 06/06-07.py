my_set = set()
n_set = set()
m = int(input())
for i in range(m):
    n = int(input())
    for k in range(n):
        name = input()
        if i == 0:
            my_set.add(name)
        else:
            n_set.add(name)
    if i > 0:
        my_set = my_set & n_set
        n_set.clear()
for elem in my_set:
    print(elem)
