text = input()
while type(text) == str:
    if text == '':
        continue
    else:
        print(text)
        text = input()
