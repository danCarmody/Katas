def tower_builder(n_floors):
    tower = []

    for i in range(1, n_floors+1):
        tower.append(((n_floors - i) * " ") + ((2*i - 1) * "*") + ((n_floors - i) * " "))
    return tower


print("\n".join(tower_builder(1)))
print("\n".join(tower_builder(2)))
print("\n".join(tower_builder(3)))

