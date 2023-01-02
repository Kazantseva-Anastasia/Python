count = 0
am = 1
st_num = -1
st = input()
while st != 'стоп':
    while (('кот' in st) or ('Кот' in st)) and (st_num == -1):
        if ('кот' in st) or ('Кот' in st):
            st_num = am
            break
    if ('кот' in st) or ('Кот' in st):
        count += 1
    am += 1
    st = input()
print(count, st_num)
