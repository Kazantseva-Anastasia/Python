white_l = []
search_l = []
for i in range(int(input())):
    white_l.append(input())
for i in range(int(input())):
    search = input()
    if search in white_l:
        search_l.append(search)
for text in search_l:
    print(text)
