lst = [int(elem) for elem in input().split()]
k, m = input().split()
print(sum(lst[int(k):int(m) + 1]))
