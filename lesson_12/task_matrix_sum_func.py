def print_matrix(matrix, m, n):
    cols_sum = [0] * m
    for row in matrix:
        row_sum = 0
        for i, col in enumerate(row):
            print(f'{col}\t', end='')
            row_sum += col
            cols_sum[i] += col
        print(f'\t{row_sum}')
    print()
    print('\t'.join(str(col) for col in cols_sum))
