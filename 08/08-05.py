text = ''
n = int(input())
for i in range(n):
    text1 = input()
    if 'Не' in text1[0:3] or 'не' in text1[0:3]:
        text1 = text1[3:]
    text = text + text1 + '\n'
print(text)
