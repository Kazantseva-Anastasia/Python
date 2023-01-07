check = input().split()
my_l = []
my_sum = 0
for i in range(int(check[0])):
    pos = input().split()
    pos[1] = pos[1][1:]
    pos[len(pos) - 1] = pos[len(pos) - 1][1:]
    if (int(pos[0]) * int(pos[1])) != int(pos[2]):
        my_l.append(i + 1)
    my_sum += int(pos[2])
if my_sum != int(check[1]):
    diff = abs(my_sum - int(check[1]))
    print(diff)
    for i in range(len(my_l)):
        if i == len(my_l) - 1:
            print(my_l[i], end='')
        else:
            print(my_l[i], end=' ')
else:
    print(0)
