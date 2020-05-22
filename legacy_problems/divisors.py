def divisiors(num):
    num_divisors = 0
    for i in range(1, num+1):
        if num % i == 0:
            num_divisors += 1
    return num_divisors


print(divisiors(4))
print(divisiors(5))
print(divisiors(12))
print(divisiors(30))
