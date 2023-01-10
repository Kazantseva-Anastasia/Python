n = int(input())
r = []
for i in range(n):
    text = input()
    if 'лук' not in text:
        r.append(text)
print(', '.join(r))
