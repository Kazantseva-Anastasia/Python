my_set = set()
n = int(input())
for i in range(n):
    gor = input()
    my_set.add(gor)
last_gor = input()
if last_gor in my_set:
    print('TRY ANOTHER')
else:
    print('OK')
    