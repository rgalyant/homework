from random import randint


def primes(a, b):
    if a + b < 2:
        return

    a = max(a, 2)
    b = max(a, b)
    pr = []
    for i in range(a, b + 1):
        if not any(map(lambda n: i % n == 0, pr)):
            pr.append(i)
            yield i


print('Primes:', list(primes(1, 100)))