"""
Collection of matrix-related methods from previuos homeworks.
"""


def sort_matrix(matrix: list, m: int) -> list:
    """
    Calculates sums of columns of matrix M x M and sorts its columns by their sums in ascending order.
    Additionaly sorts elements in even columns in descending order and ascending in odd ones.

    Expects array of columns.

    Returns sums of columns.
    """

    sums = [sum(column) for column in matrix]

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

    return sums


def print_matrix(matrix: list, m: int) -> None:
    """
    Print matrix with size M x N and sums of its rows and columns.

    Expects array of rows.
    """
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


def generate_matrix(m: int, n: int) -> list:
    """
    Generate matrix M x N (array of N columns with length M) and fill it
    with random numbers from 1 to 50.
    """
    from random import randint
    return [[randint(1, 50) for _ in range(m)] for _ in range(n)]
