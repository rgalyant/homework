from random import randint

L = [randint(0, 10) for _ in range(20)]
k = randint(0, len(L) - 1)

print('K:', k)
print(f'List (before): <id: {id(L)}> {L}')

L[k:] = L[k:][1:]

print(f'List (after) : <id: {id(L)}> {L}')