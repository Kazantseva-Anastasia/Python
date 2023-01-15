_dict = dict()
for i in range(int(input())):
    val, key = input().split()
    if key in _dict:
        _dict[key].append(val)
    else:
        _dict[key] = [val]

for i in range(int(input())):
    key = input()
    if key in _dict:
        print(*_dict[key])
    else:
        print('Нет в телефонной книге')
