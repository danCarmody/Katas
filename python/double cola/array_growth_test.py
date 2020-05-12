import math

def array_growth(arr, ex):
    growth_arr = []
    exponent_found = int(math.sqrt(ex))
    counter_exponent = 1

    while counter_exponent <= exponent_found:
        holder_arr = arr
        for i in range(len(holder_arr)):
            holder_arr[i] *= counter_exponent
        growth_arr.append(holder_arr)
        counter_exponent+=1

    return growth_arr, exponent_found


sample_arr = ["a","b","c","d","e"]
print(array_growth(sample_arr, 1))
print(array_growth(sample_arr, 5))
# print(array_growth(sample_arr, 10))
# print(array_growth(sample_arr, 20))
# print(array_growth(sample_arr,52))