count = 0
a = 0
text = input()
for i in range(len(text)):
    if text[i] == 'о':
        count += 1
    else:
        if count > a:
            a = count
        count = 0
print(a)