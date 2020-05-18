def descending_order(num):
    ordered_value = [str(i) for i in str(num)]
    ordered_value.sort(reverse=True)
    res = int("".join(ordered_value))
    return res

print(descending_order(0))
print(descending_order(15))
print(descending_order(123456789))
