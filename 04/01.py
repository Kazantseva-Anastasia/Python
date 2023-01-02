t = float(input())
days = 0
weeks = 0
while t < 22:
    days += 1
    t = float(input())
    if days == 7:
        weeks += 1
        days = 0
print(weeks)
