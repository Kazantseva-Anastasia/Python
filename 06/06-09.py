hol_set = set()
pr_set = set()
count = 0
m = int(input())
for i in range(m):
    hol = input()
    hol_set.add(hol)
n = int(input())
for i in range(n):
    recipe = input()
    a = int(input())
    for k in range(a):
        pr = input()
        pr_set.add(pr)
    for elem in hol_set:
        if elem in hol_set:
            count += 1
    if count == len(pr_set):
        print(recipe)
        count = 0
        
        