text = input().split()
print(' '.join([text[i] for i in range(len(text)) if (i + 1) % 3 == 0]))
