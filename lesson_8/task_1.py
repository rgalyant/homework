from random import randint

L = [randint(0, 10) for _ in range(10)]
s = set(L)

print('List:', L)
print('Set:', s)
print('Count:', len(s))

# One liner:
print('Count (one-liner):', len(set(L)))
