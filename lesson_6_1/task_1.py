from random import randint

l = [randint(0, 10) for _ in range(20)]
k = randint(0, len(l) - 1)

print('K:', k)
print(f'List (before): <id: {id(l)}> {l}')

if 0 <= k < len(l):
    for i in range(k + 1, len(l)):
        l[i - 1] = l[i]
    l.pop()

print(f'List (after) : <id: {id(l)}> {l}')