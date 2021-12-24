from time import time, sleep


def timedeco(func):
    def wrapper(*args, **kwargs):
        time_begin = time()
        result = func(*args, **kwargs)
        print(f"Result: {result}, time {time() - time_begin}s")
        return result

    return wrapper


ls = list(range(10 ** 8))
el = ls[-1]


# print("List:", ls)
# print("Elem:", el)
# print()

@timedeco
def search1(sequence, look_for):
    for i, e in enumerate(sequence):
        if e == look_for:
            return i
    return -1


@timedeco
def search2(sequence, look_for):
    i = -1
    while i < len(sequence):
        i += 1
        if sequence[i] == look_for:
            break
    return i


print("Begin")
search1(ls, el)
search2(ls, el)