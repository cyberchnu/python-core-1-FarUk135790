def sum_even_nums_in_range(start, stop):
    return sum([num for num in range(start, stop + 1) if num % 2 == 0])
result = sum_even_nums_in_range(1, 10)
print(result)