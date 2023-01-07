data = []
money_data = []
for i in range(int(input())):
    data.append(int(input()))
for cash in data:
    print(cash)
money_data = data
for i in range(len(money_data)):
    money_data[i] = money_data[i] * 3
print()
for money in money_data:
    print(money)
