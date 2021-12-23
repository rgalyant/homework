import time

def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print(time.perf_counter_ns() - start_time)
        return res
    return wrapped

@time_of_function
def func(first, second):
    return bin(int(first, 2) + int(second, 2))


print(func("111", "0000"))