def sequence_sum(begin_number, end_number, step):
    seq_sum = 0

    if begin_number > end_number:
        return seq_sum

    else:
        for i in range(begin_number, end_number+1, step):
            seq_sum += i
        return seq_sum


print sequence_sum(2, 6, 2)
print sequence_sum(1, 5, 1)
print sequence_sum(6, 3, 1)
print sequence_sum(0, 10, 2)
print sequence_sum(1, 15, 3)

