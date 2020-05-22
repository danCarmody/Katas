def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    print (array1, array2)
    for i in range(0, len(array1)):
        if array1.count(array1[i]) != array2.count(array1[i]*array1[i]):
            return False
    return True


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

a3 = []
a4 = [1]

a5 = [0, 1]
a6 = [2, 3]


print comp(a1, a2)
print comp(a3, a4)
print comp(a5, a6)
