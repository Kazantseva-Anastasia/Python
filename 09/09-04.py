data = []
for i in range(int(input())):
    data.append(input())
for i in range(int(input())):
    number = int(input())
    if len(data) >= number:
        print(data[number -1])
