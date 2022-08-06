def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"
    # if num == 0:
    #     return 0
    # elif num % 10 == prev_digit % 10 and num % 10 == (prev_digit // 100) % 10:
    #     return 1 + neighbor_digits(num // 10, num)
    # elif num % 10 == (prev_digit // 10) % 10:
    #     return 1 + neighbor_digits(num // 10, num)
    # elif num % 10 != (num // 10) % 10:
    #     return neighbor_digits(num // 10, num)
    # else:
    #     return neighbor_digits(num, num)

    if num < 10:
        return int(num == prev_digit)
    last = num % 10
    rest = num // 10
    add_val = int(prev_digit == last or rest % 10 == last)
    return add_val + neighbor_digits(num // 10, last)    

print(neighbor_digits(112))