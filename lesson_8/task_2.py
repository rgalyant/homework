from random import randint

l1 = [randint(0, 10) for _ in range(10)]
l2 = [randint(0, 10) for _ in range(10)]

print('List 1:', l1)
print('List 2:', l2)
print('Intersect. count:', len(set(l1) & set(l2)))
