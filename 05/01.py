for i in range(int(input()), int(input())+1):
    s = ''
    if i % 3 == 0:
        s += 'Fizz'
    if i % 5 == 0:
        s += 'Buzz'
    if s == '':
        s = i
    print(s)
