def find(n):
    multiples = 0

    for nums in range(0, n):
        checker = nums + 1
        if checker % 3 == 0 or checker % 5 == 0:
            multiples += checker

    return multiples


print find(5)
print find(10)
