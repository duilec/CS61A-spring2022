def list_o_lists(n):
    """Assuming N >= 0, return the list consisting of N lists:
    [1], [1, 2], [1, 2, 3], ... [1, 2, ... N].
    >>> list_o_lists(0)
    []
    >>> list_o_lists(1)
    [[1]]
    >>> list_o_lists(5)
    [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
    """
    if n == 0:
        return []
    
    lst = list(range(0, n))
    i = 0
    for i in range(0, n):
        sub_lst = list(range(1, i+2))
        lst[i] = sub_lst
    return lst

# print(list_o_lists(5))

def sol_list_o_lists(n):
    """Assuming N >= 0, return the list consisting of N lists:
    [1], [1, 2], [1, 2, 3], ... [1, 2, ... N].
    >>> list_o_lists(0)
    []
    >>> list_o_lists(1)
    [[1]]
    >>> list_o_lists(5)
    [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
    """
    return [list(range(1, i + 1)) for i in range(1, n+1)]

# print(sol_list_o_lists(5))

def sol_palindrome(s):
    """Return whether s is the same sequence backward and forward.

    >>> palindrome([3, 1, 4, 1, 5])
    False
    >>> palindrome([3, 1, 4, 1, 3])
    True
    >>> palindrome('seveneves')
    True
    >>> palindrome('seven eves')
    False
    """
    return all([a == b for a, b in zip(s, reversed(s))])

def palindrome(s):
    """Return whether s is the same sequence backward and forward.

    >>> palindrome([3, 1, 4, 1, 5])
    False
    >>> palindrome([3, 1, 4, 1, 3])
    True
    >>> palindrome('seveneves')
    True
    >>> palindrome('seven eves')
    False
    """

    rev_s = list(reversed(s))
    zip_s_rev = list(zip(s, rev_s))
    return len(s) == len([(elem, rev_elem) for (elem, rev_elem) in zip_s_rev if elem == rev_elem])

print(palindrome([3, 1, 4, 1, 5]))

print(palindrome([3, 1, 4, 1, 3]))

print(palindrome('seveneves'))

print(palindrome('seven eves'))