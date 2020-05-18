def count_change(money, coins):
    size = len(coins)

    table = [[0 for x in range(size)] for x in range(money + 1)]

    for i in range(size):
        table[0][i] = 1

    for i in range(1, money+1):
        for j in range(size):
            x = table[i - coins[j]][j] if i - coins[j] >= 0 else 0
            y = table[i][j-1] if j>=1 else 0

            table[i][j] = x + y
            

    return table[money][size-1]

print(count_change(4,[1,2]))
print(count_change(10, [5,2,3]))
print(count_change(11, [5,7]))