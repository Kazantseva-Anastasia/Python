my_set = set()
new_set = set()
count = 0
n = int(input())
for i in range(n):
    name = input()
    if name not in my_set:
        my_set.add(name)
    else:
        count += 1
        if name not in new_set:
            new_set.add(name)
count += len(new_set)
print(count)
