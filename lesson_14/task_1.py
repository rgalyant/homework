# Sums floats or strings
def sum_float():
    a = input("Enter first value (float or string) : ")
    b = input("Enter second value (float or string): ")

    try:
        return float(a) + float(b)
    except ValueError:
        return a + b

# Sums integers or strings
def sum_int():
    a = input("Enter first value (integer or string) : ")
    b = input("Enter second value (integer or string): ")

    try:
        return int(a) + int(b)
    except ValueError:
        return a + b

# Combination of all above (sums ints or floats or strings)
def sum():
    a = input("Enter first value : ")
    b = input("Enter second value: ")

    try:
        return int(a) + int(b)
    except ValueError:
        try:
            return float(a) + float(b)
        except ValueError:
            return a + b

print(sum_float())
print(sum_int())
print(sum())