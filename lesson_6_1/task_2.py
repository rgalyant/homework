from random import randint

l = [randint(0, 10) for _ in range(20)]
k = randint(0, len(l) - 1)
c = 'Hillel'

print('K:', k)
print(f'List (before): <id: {id(l)}> {l}')

l[k:] = [c] + l[k:]

print(f'List (after) : <id: {id(l)}> {l}')





