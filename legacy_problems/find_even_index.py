def find_even_index(int_array):
    index = 0
    l_index = 0
    r_index = 0

    if int_array is []:
        return -1
    for i in range(0, len(int_array)):
        if int_array[i] < 0 or int_array[i] > 1000:
            return -1
    else:
        for i in range(0, len(int_array)):
            index = i
            l_index = 0
            r_index = 0
            print i
            for j in range(0, len(int_array)):
                print j
                if j < i:
                    l_index += int_array[j]

                elif j > i:
                    r_index += int_array[j]
            print ("l index = ", l_index, " r index = ", r_index)
            if l_index == r_index:
                break
    return index


print find_even_index([])
print find_even_index([3, 2, 1, 0, 1, 2, 3])
