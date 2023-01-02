final_text = ''
num = int(input())
text = input()
for i in range(len(text)):
    zam = ord(text[i])
    if ((zam >= 1072) and (zam <= 1103)) or ((zam >= 1040) and (zam <= 1071)):
        if zam == 1101:
            zam = 1072
        elif zam == 1101:
            zam = 1073
        elif zam == 1103:
            zam = 1074
        elif zam == 1069:
            zam = 1040
        elif zam == 1070:
            zam = 1041
        elif zam == 1071:
            zam = 1042
        else:
            zam += num
        final_text += chr(zam)
    else:
        final_text += text[i]
print(final_text)
