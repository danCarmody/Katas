def memoize(fib_val):
    bank = {}
    def sorter(check_val):
        if check_val not in bank:
            bank[check_val] = fib_val(check_val)
        return bank[check_val]
    return sorter

def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci = memoize(fibonacci)


print(fibonacci(50))