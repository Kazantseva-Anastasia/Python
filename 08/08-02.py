word1 = input()
word2 = input()
k = 0
b = 0
while len(word1) != len(word2):
    print("Введите первое слово")
    word1 = input()
    print("Введите второе слово")
    word2 = input()
for i in range(len(word1)):
    if word1[i] == word2[i]:
        k += 1
    if (word1[i] in word2) and (word1[i] != word2[i]):
        b += 1
print(k)
print(b)