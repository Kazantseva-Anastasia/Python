my_set = set()
n_set = set()
count = 0
n = int(input())
for i in range(n):
    name = input()
    if name not in my_set:
        my_set.add(name)
    else:
        count += 1
        if name not in n_set:
            n_set.add(name)
count += len(n_set)
print(count)
