text = ((input().upper()).split())
t = ''
for i in range(len(text)):
    t += '-'.join(text[i]) + ' '
t = t[:len(t) - 1]
print(t)
