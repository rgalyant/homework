from random import randint

l1 = [randint(0, 10) for _ in range(20)]
l2 = [randint(0, 10) for _ in range(20)]

print('List 1:', l1)
print('List 2:', l2)

c = len(set([n if l1.count(n) == 1 else None for n in l1] + [None]).symmetric_difference(set([n if l2.count(n) == 1 else None for n in l2] + [None])))

print('Uniques:', c)