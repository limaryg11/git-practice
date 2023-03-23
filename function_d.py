def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    largest_num = numbers[0]

    for i in range(len(numbers)):
        if largest_num < numbers[i]:
            largest_num = numbers[i]
    return largest_num
print(max_value([1, 12, 2, 42, 8, 3]))
