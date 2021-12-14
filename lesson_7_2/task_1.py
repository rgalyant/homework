from random import randint

l = [randint(0, 10) for _ in range(20)]

print('List:', l)

uniques = []
for n in l:
    if (l.count(n) == 1):
        uniques.append(n)

print('Uniques:', tuple(reversed(uniques)))