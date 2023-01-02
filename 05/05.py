count = 1
st_num = -1
stop_word = True
while stop_word:
    st = input()
    while (('кот' in st) or ('Кот' in st)) and (st_num == -1):
        if ('кот' in st) or ('Кот' in st):
            st_num = count
            break
    if ('кот' in st) or ('Кот' in st):
        print(st_num)
        break
    if st == 'Стоп':
        print(st_num)
        stop_word = False
    count += 1
