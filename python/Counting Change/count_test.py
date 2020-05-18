def count(s, m, n):
     # Base Case #1 (if n reaches zero, whole amount, possible solution):
    if (n == 0):
        return 1

    # Base Case #2 (if n is less than zero, no solution exists):
    if (n < 0):
        return 0

    # Base Case #3 (If there are no coins and some value to compare to, no solution):
    if (m<=0 and n>=1):
        return 0

    return count(s,m-1, n) + count(s,m, n-s[m-1])


print(count([1,2,], 2, 4))
print(count([5,2,3], 3, 10))
print(count([5,7], 2, 11 ))
