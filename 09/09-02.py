data = []
for i in range(int(input())):
    data.append(input())
search = input()
for text in data:
    if search in text:
        print(text)
