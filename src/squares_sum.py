def squares_sum(n):
    return sum([i ** 2 for i in range(1, n + 1)])


result = squares_sum(5)
print(result)