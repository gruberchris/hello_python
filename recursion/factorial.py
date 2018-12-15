import sys

def factorial(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)

if len(sys.argv) == 2:
    integer_param = int(sys.argv[1])
    print("%d" % factorial(integer_param))