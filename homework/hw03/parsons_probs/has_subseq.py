def has_subseq(n, seq):
    """
    Complete has_subseq, a function which takes in a number n and a "sequence"
    of digits seq and returns whether n contains seq as a subsequence, which
    does not have to be consecutive.

    >>> has_subseq(123, 12)
    True
    >>> has_subseq(141, 11)
    True
    >>> has_subseq(144, 12)
    False
    >>> has_subseq(144, 1441)
    False
    >>> has_subseq(1343412, 134)
    True
    """
    "*** YOUR CODE HERE ***"
    if n < seq:
        return False
    elif n < 10:
        return n == seq
    elif n % 10 == seq % 10:
        return True and has_subseq(n // 10, seq // 10)
    else: 
        return has_subseq(n // 10, seq)
    

    # if num < 10:
    #     return int(num == prev_digit)
    # last = num % 10
    # rest = num // 10
    # add_val = int(prev_digit == last or rest % 10 == last)
    # return add_val + neighbor_digits(num // 10, last)    