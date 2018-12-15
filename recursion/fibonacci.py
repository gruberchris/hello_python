import sys

def naive_fibonacci(n):
    # runs in O(2^n). Is exponentially slower
    if n == 0:
        return 0

    if n == 1:
        return 1

    return naive_fibonacci(n - 1) + naive_fibonacci(n - 2)

def memo_fibonacci(n, cache = [0, 1]):
    # runs in O(n) implemented using memoization
    if n == 0:
        return 0

    if n == 1:
        return 1

    if n <= len(cache):
        return cache[n - 1]

    fib_number = memo_fibonacci(n - 1, cache) + memo_fibonacci(n - 2, cache)
    cache.append(fib_number)
    return fib_number

if len(sys.argv) == 2:
    n_term_param = int(sys.argv[1])
    print("%d" % memo_fibonacci(n_term_param))