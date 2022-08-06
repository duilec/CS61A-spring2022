def partitions(n, m):
    """List partitions.

    >>> for p in partitions(6, 4): print(p)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n < 0 or m == 0:
        return
    else:
        if n == m:
            yield str(m)
        # you can run it unitl 'n == m', and find all probility of current partitions(n-m, m)
        # node: it is 'yield' not 'return', you can run it after 'n == m'
        for p in partitions(n-m, m): 
            yield str(m) + "+" + p
        yield from partitions(n, m - 1) # you also can run it unitl 'n == m'

def count_partitions(n, m):
    """
    >>> count_partitions(6, 4)
    9
    """
    if n < 0 or m == 0:
        return 0
    else:
        exact_match = 0
        if n == m:
            exact_match = 1
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return exact_match + with_m + without_m
