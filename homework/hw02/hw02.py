from heapq import merge
from operator import add, mul
from os import stat
from statistics import multimode

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


HW_SOURCE_FILE = __file__


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        print(1)
        return 1

    length = 1
    print(n)
    while n != 1:
        if n % 2 == 0:
            # use '//' to down round, then we will avoid float numbers
            n //= 2 
            length += 1
            print(n)
        else:
            n = n * 3 + 1
            length += 1
            print(n)
    return length

def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
    mult = 1
    while n != 0:
        mult *= term(n)
        n -= 1
    return mult

    # reference solution with python-style
    # total, k = 1, 1
    # while k <= n:
    #     total, k = term(k) * total, k + 1
    # return total    

def accumulate(merger, start, n, term):
    """Return the result of merging the first n terms in a sequence and start.
    The terms to be merged are term(1), term(2), ..., term(n). merger is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> # ((2 * 1^2 * 2) * 2^2 * 2) * 3^2 * 2
    >>> accumulate(lambda x, y: 2 * x * y, 2, 3, square)
    576
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    "*** YOUR CODE HERE ***"
    def recursion(n):
        if n == 0:
            return start
        else:
            return merger(term(n), recursion(n - 1))
    return recursion(n)
    
    # my solution with c-style
    # first_n = n
    # def recursion(n):
    #     if n == 0:
    #         # accumulate(add, 11, 0, identity) => n == 0 => ret start
    #         return start
    #     if n == first_n:
    #         # n == first_n => merge start
    #         return merger(merger(start, term(n)), recursion(n - 1))
    #     elif n >= 2:
    #         # n != first_n => merge term(n)
    #         return merger(term(n), recursion(n - 1))
    #     else:
    #         # n == 1 => out of recursion, n == 0 not merge
    #         return term(1) 
    # return recursion(n)

    # update of my solution refer to accumulate2
    # def recursion(n):
    #     if n == 0:
    #         return start
    #     else:
    #         return merger(term(n), recursion(n - 1))
    # return recursion(n)

    # reference solution with python-style
    #     # Alternative solution
    # def accumulate_reverse(merger, start, n, term):
    #     total, k = start, n
    #     while k >= 1:
    #         total, k = merger(total, term(k)), k - 1
    #     return total

    # # Recursive solution
    # def accumulate2(merger, start, n, term):
    #     if n == 0:
    #         return start
    #     return merger(term(n), accumulate2(merger, start, n-1, term))

    # # Alternative recursive solution using start to keep track of total
    # def accumulate3(merger, start, n, term):
    #     if n == 0:
    #         return start
    #     return accumulate3(merger, merger(start, term(n)), n-1, term)

def summation_using_accumulate(n, term):
    """Returns the sum: term(1) + ... + term(n), using accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> # You aren't expected to understand the code of this test.
    >>> # Check that the bodies of the functions are just return statements.
    >>> # If this errors, make sure you have removed the "***YOUR CODE HERE***".
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(summation_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    # "*** YOUR CODE HERE ***"
    return accumulate(add, 0, n, term)

def product_using_accumulate(n, term):
    """Returns the product: term(1) * ... * term(n), using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> # You aren't expected to understand the code of this test.
    >>> # Check that the bodies of the functions are just return statements.
    >>> # If this errors, make sure you have removed the "***YOUR CODE HERE***".
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(product_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    # "*** YOUR CODE HERE ***"
    return accumulate(mul, 1, n, term)
