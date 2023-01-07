text = ''
m = int(input())
n = int(input())
for i in range(n):
    text1 = input()
    if len(text1) > m:
        text = text[0:m - 3] + '...'
    text = text + text1 +'\n'
print(text)
