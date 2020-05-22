def order(sentence):
    str_array = sentence.split()
    sort = False
    count = 1
    # compare and sort iteration
    for i in range(0, len(str_array)):
        for j in range(0, len(str_array)):
            comp_string = str_array[j]
            for k in range(0, len(comp_string)):
                if str(count) == comp_string[k]:
                    sort = True
                    break
            if sort:
                temp = str_array[i]
                str_array[i] = str_array[j]
                str_array[j] = temp

    return str_array


print order("")
print order("is2 Thi1s T4est 3a")
print order("4of Fo1r pe6ople g3ood th5e the2")