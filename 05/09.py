n = int(input())
meow = 'Meow'
woof = 'No'
text = ''
for i in range(n):
    st = input()
    if ('cat' in st) or ('Cat' in st):
        text = meow
    if ('dog' in st) or ('Dog' in st):
        text = woof
print(text)
