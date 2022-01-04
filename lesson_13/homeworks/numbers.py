"""
Collection of methods related to numbers.
"""


def primes(a: int, b: int) -> int:
    """
    Generator of prime numbers in range [a, b]
    """
    if a + b < 2:
        return

    a = max(a, 2)
    b = max(a, b)
    pr = []
    for i in range(a, b + 1):
        if not any(map(lambda n: i % n == 0, pr)):
            pr.append(i)
            yield i


def fibonacci(n: int) -> int:
    """
    Generator of Fibonacci numbers up to N (inclusive)
    """
    a = 0
    b = 1

    while b <= n:
        yield a
        a, b = b, a + b


def fibonacci_n(n: int) -> int:
    """
    Generates N Fibonacci numbers
    """
    a = 0
    b = 1

    for _ in range(n):
        yield a
        a, b = b, a + b


def gcd(a: int, b: int) -> int:
    """
    Calculates GCD (Greatest Common Divider) of two integers.
    """

    while b != 0:
        a, b = b, a % b

    return a