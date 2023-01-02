count = 0
s = 0
text = input()
for i in range(len(text)):
    if text[i] == 'о':
        count += 1
    else:
        if count > s:
            s = count
        count = 0
print(s)
