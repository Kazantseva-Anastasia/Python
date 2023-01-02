my_set1 = set()
my_set2 = set()
my_set3 = set()
n = int(input())
m = int(input())
k = int(input())
s = n + m + k
count = 0
for i in range(s):
    name = input()
    if name not in my_set1:
        my_set1.add(name)
    elif name not in my_set2:
        my_set2.add(name)
        count += 1
    else:
        my_set3.add(name)
        count -= 1
print(count)
