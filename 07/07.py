word = input()
for i in range(len(word)):
    if i == (len(word) - 1):
        print(ord(word[i]))
    else:
        print(ord(word[i]), ',', sep='', end=' ')
