data = []
word = ''
for i in range(int(input())):
    data.append(input())
number = int(input())
number -= 1
for i in range(len(data)):
    if len(lst[i]) >= number:
        word += data[i][number]
    else:
        word += ' '
print(word)
