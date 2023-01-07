text = ''
n = int(input())
for i in range(n):
    text1 = input()
    if text1[0:2] != '%%' and text1[0:4] != '####':
        text = text + text1 + '\n'
    elif text1[0:2] == '%%':
        text1 = text1[3:]
        text = text + text1 + '\n'
print(text)
