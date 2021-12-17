from random import randint

l = [randint(0, 10) for i in range(10)]
n = randint(1, 10)

print('List:', l)
print('Number:', n)

print('Mapped list:', list(map(lambda x, y = n: x ** y, l)))
