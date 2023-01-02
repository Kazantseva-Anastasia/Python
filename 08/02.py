word1 = input()
word2 = input()
k = 0
m = 0
while len(word1) != len(word2):
    print('Заново первое слово')
    word1 = input()
    print('Заново второе слово')
    word2 = input()
for i in range(len(word1)):
    if word1[i] == word2[i]:
        k += 1
    if (word1[i] in word2) and (word1[i] != word2[i]):
        m += 1
print(k)
print(m)
