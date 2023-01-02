full_text = ''
n = int(input())
for i in range(n):
    text = input()
    if 'не ' in text[0:3] or 'Не' in text[0:3]:
        text = text[3:]
    full_text = full_text + text + '\n'
print(full_text)
