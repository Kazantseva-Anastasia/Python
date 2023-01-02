n = int(input())
for i in range(n):
    text = input()
    if 'кот' in text:
        for k in range(len(text)):
            if text[k] == 'к' and text[k + 1] == 'о' and text[k + 2] == 'т':
                print(i + 1, k + 1)
