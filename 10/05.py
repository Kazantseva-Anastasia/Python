people = []
for i in range(int(input())):
    people.append(input())
k = int(input())
if k > 1:
    for i in range(k, len(people), k - 1):
        if i <= len(people):
            del people[i - 1]
else:
    people.clear()
for man in people:
    print(man)
