from random import randint

L = [randint(0, 10) for i in range(randint(10, 20))]
n = randint(0, 10)

print('List:', L)
print('Number:', n)

def func(ls, nb):
    for i, el in enumerate(ls):
        for el2 in ls[i + 1:]:
            if el + el2 == nb:
                return True
    return False

print('Func:', func(L, n))