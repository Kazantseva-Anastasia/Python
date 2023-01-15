n = int(input())
_dict = dict()
for i in range(n):
    s = input().split()
    if s[2] in _dict:
        _dict[s[2]] += ' ' + str(s[0])
    else:
        _dict[s[2]] = s[0]
n = int(input())
for i in range(n):
    s = input()
    print(_dict.get(s, ''))
