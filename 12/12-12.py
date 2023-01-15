text = input().lower()
a = 0
for i in range(len(text)):
    if text.count(text[i]) > a:
        a = text.count(text[i])
print(a)
