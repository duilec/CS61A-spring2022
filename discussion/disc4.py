def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n == 0 or n == 1:
        return 1
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

    # more good:
    # if n == 0:
    #     return 1
    # elif n < 0:
    #     return 0
    # else:
    #     return count_stair_ways(n - 1) + count_stair_ways(n - 2)

def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return sum(count_k(n - (i + 1), k) for i in range(k))
    
    # my old solution is wrong in base condition, not in execute statement

    # reference solution
    # if n == 0:
    #     return 1
    # elif n < 0:
    #     return 0
    # else:
    #     total = 0
    #     i = 1
    #     while i <= k:
    #         total += count_k(n - i, k)
    #         i += 1
    #     return total


# print(count_k(4, 4))


def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [ index * s[index] for index in range(len(s))[::2] ]

x = [1, 2, 3, 4, 5, 6]
print(even_weighted(x))

def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if len(s) == 0:
        return 1

    step_size = 2
    max_mul = 0
    current_mul = 1
    while step_size < len(s):
        for value in s[::step_size]:
            current_mul *= value 
        max_mul = max(current_mul, max_mul)
        step_size += 1
        current_mul = 1
    return max_mul

print(max_product([]))