def hop():
    """
    Calling hop returns a curried version of the function f(x, y) = y.
    >>> hop()(3)(2) # .Case 1
    2
    >>> hop()(3)(7) # .Case 2
    7
    >>> hop()(4)(7) # .Case 3
    7
    """
    "*** YOUR CODE HERE ***"
    def hop_1(x):
        def hop_2(y):
            return y
        return hop_2
    return hop_1