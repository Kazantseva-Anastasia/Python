m = int(input())
n = int(input())
m_set = set()
n_set = set()
for i in range(m):
    book = input()
    m_set.add(book)
for i in range(n):
    book = input()
    if book in m_set:
        print('Yes')
    else:
        print('No')
