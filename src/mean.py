def mean(number):
    digits = [int(digit) for digit in str(number)]
    mean_value = sum(digits) / len(digits)
    return mean_value