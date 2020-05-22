def find_unique(arr):
    comparator = arr[(len(arr)-1)/2]
    max = len(arr) -1

    for i in range(0, len(arr)):
        if arr[i] != comparator and arr[max - i] != comparator:
            unique = comparator
        elif arr[i] != comparator and arr[max - i] == comparator:
            unique = arr[i]
        elif arr[i] == comparator and arr[max - i] != comparator:
            unique = arr[max-i]

    return unique


print find_unique([1, 1, 1, 2, 1, 1])
print find_unique([0, 0, 0.55, 0, 0])
print find_unique([3, 10, 3, 3, 3])
print find_unique([8, 7, 7, 7, 7, 7])
print find_unique([6, 6, 6, 6, 6, 9])

