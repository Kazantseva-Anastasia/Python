text = input().split()
my_str = ''
for i in range(len(text)):
    if i == 0:
        my_str = '["' + text[i] + '", '
    elif i == len(text) - 1:
        my_str += '"' + text[i] + '"]'
    else:
        my_str += '"' + text[i] + '", '
print(my_str)
