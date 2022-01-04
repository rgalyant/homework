# Test: homework.triangles
def hw_triangles_test():
    from homeworks import triangles

    triangles.draw_triangle(7)
    print()

    triangles.draw_triangle_filled(7)
    print()

    triangles.draw_compass_arrow(7)
    print()

    triangles.draw_compass_arrow_2(7)
    print()

    del triangles


# Test: homeworks.numbers
def hw_numbers_test():
    import homeworks.numbers as hn

    print("Primes up to 100:", list(hn.primes(0, 100)))
    print("Fibonacci numbers up to 1000:", list(hn.fibonacci(1000)))
    print("First 20 Fibonacci numbers:", list(hn.fibonacci_n(20)))
    print("GCD of 12 and 15:", hn.gcd(12, 15))
    print("GCD of 12 and 17:", hn.gcd(12, 17))

    del hn


# Test: homeworks.matrices
def hw_matrices_test():
    import homeworks

    m = 10
    matrix = homeworks.matrices.generate_matrix(m, m)

    print("\nBefore sort:")
    homeworks.matrices.print_matrix(matrix, m)

    homeworks.matrices.sort_matrix(matrix, m)

    print("\nAfter sort:")
    homeworks.matrices.print_matrix(matrix, m)

    del homeworks


def main():
    hw_triangles_test()
    hw_numbers_test()
    hw_matrices_test()


if __name__ == "__main__":
    main()