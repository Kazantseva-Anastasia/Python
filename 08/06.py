full_text = ''
m = int(input())
n = int(input())
for i in range(n):
    text = input()
    if len(text) > m:
        text = text[0:m - 3] + '...'
    full_text = full_text + text + '\n'
print(full_text)
