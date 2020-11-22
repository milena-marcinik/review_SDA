def fib(number):
    old, new = 0, 1
    for _ in range(number):
        old, new = new, old + new
    return old