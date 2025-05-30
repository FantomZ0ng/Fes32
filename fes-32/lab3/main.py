from functools import reduce
from timeit import timeit


def fib_rec(n):
    if n <= 1:
        return 1

    return fib_rec(n - 1) + fib_rec(n - 2)


def fact_rec(n):
    if n == 0:
        return 1

    return n * fact_rec(n - 1)


def fib_loop(n):
    a = [1, 1]
    if n <= 1:
        return 1

    while len(a) != n + 1:
        a.append(a[-1] + a[-2])
    return a[-1]


def fact_loop(n):

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def fact_reduce(n):

    return reduce(lambda a, b: a * b, range(1, n + 1))


def benchmark(n, funcs):

    print(f'n = {n}')
    for name, func in funcs:
        time = timeit(lambda: func(n), number=1)
        print(f'func = {name} result = {func(n)}')
        print(f'Execution time {time}')


if __name__ == '__main__':
    funcs_rec = [("fib_rec", fib_rec), ("fact_rec", fact_rec)]
    funcs = [
        ("fib_loop", fib_loop),
        ("fact_loop", fact_loop),
        ("fact_reduce", fact_reduce),
    ]

    # benchmark(10, funcs_rec)
    # benchmark(40, funcs_rec)
    # benchmark(10, funcs)
    # benchmark(1000, funcs)
