def sort_matrix(matrix, m, sums):
    # Bubble sort (cols)
    for i in range(m):
        for j in range(i, m):
            if sums[j] < sums[i]:
                sums[j], sums[i] = sums[i], sums[j]
                matrix[j], matrix[i] = matrix[i], matrix[j]

    for cn, col in enumerate(matrix):
        # Bubble sort (rows)
        for i in range(m):
            for j in range(i, m):
                if col[j] < col[i]:
                    col[j], col[i] = col[i], col[j]

        if cn % 2 == 0:
            for i in range(m // 2):
                col[i], col[m - i - 1] = col[m - i - 1], col[i]


def print_matrix(matrix, m, sums):
    print('Matrix:')
    for row in range(m):
        print('\t'.join([str(col[row]) for col in matrix]))
    print('\nSums:')
    print('\t'.join([str(i) for i in sums]))
    print('')


#
# Main "function"
#

from random import randint

m = None
while True:
    m = input('Enter size:')
    if m.isnumeric():
        m = int(m)
        if m > 0:
            break

# Array of cols
matrix = [[randint(1, 50) for _ in range(m)] for _ in range(m)]
sums = [sum(col) for col in matrix]

print('Original:')
print_matrix(matrix, m, sums)

sort_matrix(matrix, m, sums)

print('Sorted:')
print_matrix(matrix, m, sums)