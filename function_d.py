def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
<<<<<<< HEAD
    largest_num = numbers[0]
=======
    print("largest number in the list!!!")
>>>>>>> e2f80a77d57e0f91340ad41861e6f068d332fb4c

    for i in range(len(numbers)):
        if largest_num < numbers[i]:
            largest_num = numbers[i]
    return largest_num
print(max_value([1, 12, 2, 42, 8, 3]))
