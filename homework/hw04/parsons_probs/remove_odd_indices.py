def remove_odd_indices(lst, odd):
    """ 
    Remove elements of lst that have odd indices.
    >>> s = [1, 2, 3, 4]
    >>> t = remove_odd_indices(s, True)
    >>> s
    [1, 2, 3, 4]
    >>> t
    [1, 3]
    >>> l = [5, 6, 7, 8]
    >>> m = remove_odd_indices(l, False)
    >>> m
    [6, 8]
    """
    "*** YOUR CODE HERE ***"
    # we must use [lst[index]], don't use lst[index], because 'int' object is not iterable 
    new_lst = []
    if odd:
        for index in range(len(lst)):
            if index % 2 == 0:
                new_lst += [lst[index]] 
    else:
        for index in range(len(lst)):
            if index % 2 != 0:
                new_lst += [lst[index]]
    return new_lst

