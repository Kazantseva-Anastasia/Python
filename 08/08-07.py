n = int(input())
for i in range(n):
    text = input()
    if 'кот' in text:
        for a in range(len(text)):
            if text[a] == 'к' and text[a + 1] == 'о' and text[a + 2] == 'т':
                print(i + 1, a + 1)
                