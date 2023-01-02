fridge_set = set()
ing_set = set()
count = 0
m = int(input())
for i in range(m):
    fridge = input()
    fridge_set.add(fridge)
n = int(input())
for i in range(n):
    recipe = input()
    t = int(input())
    for k in range(t):
        ing = input()
        ing_set.add(ing)
    for elem in ing_set:
        if elem in fridge_set:
            count += 1
    if count == len(ing_set):
        print(recipe)
        count = 0
