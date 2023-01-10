n = []
for i in range(int(input())):
    n.append(input())
k = int(input())
if k > 1:
    for i in range(k, len(n), k - 1):
        if i <= len(n):
            del n[i - 1]
else:
    n.clear()
for sol in n:
    print(sol)
    