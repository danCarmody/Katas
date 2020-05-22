def calculate_years(principal, interest, tax, desired):
    years = 0

    if principal >= desired:
        return 0
    else:
        while principal < desired:
            years += 1
            i_sum = principal * interest
            t_diff = i_sum - (i_sum*tax)
            principal += t_diff
        return years


print (calculate_years(1000, 0.05, 0.18, 1100))
print (calculate_years(1000, 0.01625, 0.18, 1200))
print (calculate_years(1000, 0.05, 0.18, 1000))
