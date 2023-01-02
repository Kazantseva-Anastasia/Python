people = []
smart_people = []
for i in range(int(input())):
    people.append(input())
for i in range(len(people)):
    if int(people[i][-1]) > 3:
        smart_people.append(people[i])
print()
for man in smart_people:
    print(man)
