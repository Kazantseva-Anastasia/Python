print(' '.join([str(int(n) ** 2) for n in input().split() if (int(n) **
                2) % 10 != 9 and int(n) % 2 != 0]))
