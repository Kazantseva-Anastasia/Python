f_text = ''
number = int(input())
text = input()
for i in range(len(text)):
    z = ord(text[i])
    if ((z >= 1072) and (z <= 1103)) or ((z >= 1040) and (z <= 1071)):
        if z == 1101:
            z = 1072
        elif z == 1101:
            z = 1073
        elif z == 1103:
            z = 1074
        elif z == 1069:
            z = 1040
        elif z == 1070:
            z = 1041
        elif z == 1071:
            z = 1042
        else:
            z += num
        f_text += chr(z)
    else:
        f_text += text[i]
print(f_text)
