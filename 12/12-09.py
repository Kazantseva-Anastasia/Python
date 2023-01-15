a = input()
text = input().split()
for word in text:
    if a.upper() in word or a.lower() in word:
        print(word)
        
        