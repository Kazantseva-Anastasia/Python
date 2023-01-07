data = []
data1 = []
for i in range(int(input())):
    data.append(int(input()))
for i in range(len(data)):
    if i != (len(data) - 1):
        data1.append(data[i] + data[i + 1])
for number in data1:
    print(number)