data = []
sch_data = []
for i in range(int(input())):
    data.append(input())
for i in range(int(input())):
    sch_data.append(input())
for i in range(len(data)):
    for a in range(len(sch_data)):
        if a != (len(sch_data) - 1):
            if sch_data[a] in data[i] and sch_data[a + 1] in data[i]:
                print(data[i])