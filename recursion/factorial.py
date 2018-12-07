def factorial(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)

def do_factorial(n):
    print("%d" % factorial(n))

do_factorial(5)