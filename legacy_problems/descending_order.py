def descending_order(num):
    sorted_num = 0
    if num < 0:
        return "invalid input"

    elif num == 0:
        return num

    else:
        num_array = [int(i) for i in str(num)]
        for k in range(0, len(num_array)):
            for m in range(0, len(num_array)):
                if num_array[k] > num_array[m]:
                    temp = num_array[m]
                    num_array[m] = num_array[k]
                    num_array[k] = temp
        sorted_num.join(num_array)
        return sorted_num


print descending_order(21445)
print descending_order(145263)
print descending_order(1254859723)
print descending_order(0)
print descending_order(-1)



