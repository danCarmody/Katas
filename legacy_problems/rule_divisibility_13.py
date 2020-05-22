def thirt(n):
    PATTERN = [1, 10, 9, 12, 3, 4]
    track = 0
    list_num = [int(i) for i in str(n)][::-1]
    for i in range(0, len(list_num)):
        temp = PATTERN.pop(0)
        track += list_num[i] * temp
        PATTERN.append(temp)

    if track != n:
        return thirt(track)
    else:
        return n


print thirt(8529)
print thirt(85299258)
print thirt(5634)
print thirt(5634)
print thirt(1111111111)
print thirt(987654321)
