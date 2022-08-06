def digit_pos_match(n, k):
    """
    >>> digit_pos_match(980, 0) # .Case 1
    True
    >>> digit_pos_match(980, 2) # .Case 2
    False
    >>> digit_pos_match(98276, 2) # .Case 3
    True
    >>> digit_pos_match(98276, 3) # .Case 4
    False
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        if n % 10 == 0:
            return True
        else:
            return False
    i = k
    while i:
        n //= 10
        i -= 1
    if n % 10 == k:
        return True
    else:
        return False
    