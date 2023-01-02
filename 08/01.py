long_word = ''
short_word = ''
long_set = set()
short_set = set()
k = 0
word = input()
while word != 'стоп':
    if k == 0:
        short_word = word
        long_word = word
        k += 1
    if len(word) < len(short_word):
        short_word = word
    if len(word) > len(long_word):
        long_word = word
    word = input()
for i in range(len(short_word)):
    short_set.add(short_word[i])
for i in range(len(long_word)):
    long_set.add(long_word[i])
mix_set = short_set & long_set
if mix_set == short_set:
    print('Yes')
else:
    print('No')
