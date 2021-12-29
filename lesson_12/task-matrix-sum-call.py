from random import randint
from task_matrix_sum_func import print_matrix

m = None # cols
while True:
    m = input('Enter M (cols):')
    if m.isnumeric():
        m = int(m)
        if m > 0:
            break

n = None # rows
while True:
    n = input('Enter N (rows):')
    if n.isnumeric():
        n = int(n)
        if n > 0:
            break

matrix = [[randint(1, 50) for _ in range(m)] for _ in range(n)] # rows

print_matrix(matrix, m, n)