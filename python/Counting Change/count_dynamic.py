def count(arr, l, num):
    table=[[0 for x in range(l)] for x in range(num+1)]

    for i in range(l):
        table[0][i] = 1

    for i in range(1, num+1):
        for j in range(l):

            x = table[i - arr[j]][j] if i-arr[j] >= 0 else 0

            y = table[i][j-1] if j>= 1 else 0

            table[i][j] = x + y
            print (table)

    return table[num][l-1]


arr = [1,2,3]
l = len(arr)
num = 4

print(count(arr, l, num))

