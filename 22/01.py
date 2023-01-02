from random import sample
from pprint import pprint


def make_bingo():
    a = [sample(range(1, 75), 5) for i in range(5)]
    a[2][2] = 0
    for i in range(len(a)):
        a[i] = tuple(a[i])
    return tuple(a)


res = make_bingo()
pprint(res)
