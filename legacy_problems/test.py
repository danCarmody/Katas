def multiply(a,b):
    a*b


def str_combination(str_array, combo_num):
    combo_str = ""
    temp_str = ""
    for i in range(0, combo_num):
        for j in range(1, len(str_array)):

            temp_str += str_array[i]
            print(combo_str)

    return combo_str


str_combination(["apple", "bananas", "pear", "strawberry"], 3)

