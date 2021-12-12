from random import randint

l1 = [randint(0, 10) for _ in range(20)]
l2 = [randint(0, 10) for _ in range(20)]

print('List 1:', l1)
print('List 2:', l2)

c = sum([(l1 + l2).count(n) == 1 for n in (l1 + l2)])

print('Uniques:', c)