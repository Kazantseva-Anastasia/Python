m = int(input())
n = int(input())
m_set = set()
n_set = set()
for i in range(m):
    books = input()
    m_set.add(books)
for i in range(n):
    books = input()
    if books in m_set:
        print('YES')
    else:
        print('NO')
        