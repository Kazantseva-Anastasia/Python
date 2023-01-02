n = int(input())
s = str(n)
while (s[0] != '1') and (n < 1000000000):
    k = int(s[0])
    n *= k
    s = str(n)
print(n)
