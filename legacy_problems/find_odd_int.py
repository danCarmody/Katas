def find_it(seq):
    odd_int = 0
    sorted_seq = list(set(seq))

    for i in range(0, len(sorted_seq)):
        if seq.count(sorted_seq[i]) % 2 != 0:
            odd_int = sorted_seq[i]

    return odd_int


print find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
print find_it([11,11,11,22,22,33,33])
print find_it([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3])