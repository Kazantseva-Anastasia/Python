def matrix(n=1, m=0, a=0):
    _str = []
    _list = []
    if m == 0:
        m = n
    for i in range(n):
        for j in range(m):
            _str.append(a)
        _list.append(_str)
        _str = []
    return _list


rows = matrix(4)
for row in rows:
    print(*row)
