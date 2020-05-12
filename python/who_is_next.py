import math

def who_is_next(names, r):
    combo_names = []
    exponent_found = int(math.sqrt(r))

    for i in range(exponent_found):
        combo_names.extend(names*(2**i))
    return combo_names


names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
print(who_is_next(names, 1))
print(who_is_next(names, 5))
print(who_is_next(names, 10))
print(who_is_next,(names, 52))