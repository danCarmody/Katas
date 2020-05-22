def sort_array(source_array):
    sorted_array = sorted([it for it in source_array if it%2!=0], reverse=True)
    for i in range(0, len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = sorted_array.pop()

    return source_array


print sort_array([5, 3, 2, 8, 1, 4])
print sort_array([5, 3, 1, 8, 0])
print sort_array([4, 3, 2, 1, 9])
print sort_array([])
