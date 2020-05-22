def dirReduc(arr):
    reduced = False
    index = 0

    while index < len(arr)-1:
        if arr[index] == "NORTH" and arr[index+1] == "SOUTH":
            arr.pop(index) and arr.pop(index+1)
            break
        if arr[index] == "WEST" and arr[index+1] == "EAST":
            arr.pop(index) and arr.pop(index+1)
            break
        if arr[index] == "SOUTH" and arr[index+1] == "NORTH":
            arr.pop(index) and arr.pop(index+1)
            break
        if arr[index] == "EAST" and arr[index+1] == "WEST":
            arr.pop(index) and arr.pop(index+1)
            break
        index += 1


    return arr


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))