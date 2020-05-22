def array_diff(a, b):
    a = [ele for ele in a if ele not in b]

    return a


print array_diff([1, 2], [1])
print array_diff([1, 2], [2])
print array_diff([1, 2, 2, 2], [2])
print array_diff([1, 2, 2, 2], [])
print array_diff([], [1, 2, 2, 2])
print array_diff([4, 4, 4, 3, 2, 2, 1, 5], [1, 2])
