text = input().strip().lower()
num = 0
a = ''
for i in range(len(text)):
    if text.count(text[i]) > num:
        num = text.count(text[i])
        a = text[i]
    elif text.count(text[i]) == num:
        if text[i] < a:
            lt = text[i]
print(a)
