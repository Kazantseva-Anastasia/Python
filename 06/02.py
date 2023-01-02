my_set = set()
n = int(input())
for i in range(n):
    city = input()
    my_set.add(city)
last_city = input()
if last_city in my_set:
    print('Try another')
else:
    print('OK')
