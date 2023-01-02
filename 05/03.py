stop_word = True
st_num = -1
count = 1
while stop_word:
    st = str(input())
    while (('кот' in st) or ('Кот' in st)) and (st_num == -1):
        if ('кот' in st) or ('Кот' in st):
            st_num = count
            break
    if st == 'Стоп':
        print(st_num)
        stop_word = False
    count += 1
