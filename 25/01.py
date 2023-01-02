import pymorphy2


def clear(text):
    return "".join(filter(lambda c: c.isalpha() or c == '-', text))


morph = pymorphy2.MorphAnalyzer()
legal = ["видеть", "увидеть", "глядеть", "примечать", "узреть"]
text = input().split()

res = list()
for word in text:
    word = clear(word)
    parse = morph.parse(word)
    if not parse:
        continue
    parse = parse[0]
    if parse.normal_form in legal:
        res.append(parse)

print(len(res))
