dish_set = set()
day_set = set()
m = int(input())
for i in range(m):
    dish = input()
    dish_set.add(dish)
n = int(input())
for i in range(n):
    t = int(input())
    for k in range(t):
        day = input()
        day_set.add(day)
dish_set = dish_set - day_set
for elem in dish_set:
    print(elem)
