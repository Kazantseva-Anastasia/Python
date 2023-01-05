n = int(input())
a = str(n)
while (a[0] != '1') and (n < 1000000000):
    b = int(a[0])
    n *= b
    a = str(n)
print(n)
