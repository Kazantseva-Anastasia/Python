a = input().split()
b = list()
for i in range(len(a)):
    if a[i].isdigit():
        b.append(a[i])
    elif a[i] == '+':
        c = int(b.pop(-2)) + int(b.pop(-1))
        b.append(c)
    elif a[i] == '-':
        c = int(b.pop(-2)) - int(b.pop(-1))
        b.append(c)
    elif a[i] == '*':
        c = int(b.pop(-2)) * int(b.pop(-1))
        b.append(c)
    else:
        c = int(b.pop(-2)) / int(b.pop(-1))
        b.append(c)
print(b[0])
