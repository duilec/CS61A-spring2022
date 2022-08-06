
""" lambda as a func """
# >>> z = 3
# >>> lambda x: lambda y: lambda: z
# <function <lambda> at 0x7f7fa30b7310>
# >>> (lambda x: lambda y: lambda: z)(1)(1)()
# 3
# >>> (lambda x: lambda y: lambda: z)(1)(1)(1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: <lambda>() takes 0 positional arguments but 1 was given

""" passing arguments in order  """
# >>> higher_order_lambda = lambda f: lambda x: f(x)
# >>> g = lambda x: x * x
# >>> higher_order_lambda(2)(g)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <lambda>
# TypeError: 'int' object is not callable
# >>> higher_order_lambda(g)(2)
# 4

# def cake():
#     print('beets')
#     def pie():
#        print('sweets')
#        return 'cake'
#     return pie

""" you can try to Comments(#) "*** YOUR CODE HERE ***" """
# Error: expected
#     ['Expr', 'Return']
# but got
#     ['Expr', 'Expr', 'Return']

from turtle import Turtle
from parsons.local_server import next_problem


def match_k(k):
    """ Return a function that checks if digits k apart match

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def check(n):
        if k == 1 and n == 1:
            return True
        temp = n
        cnt = 0
        while temp:
            temp //= 10
            cnt += 1
        if k > 1:
            cnt /= 2
        else:
            cnt -= 1
        while n:
            fisrt = n % 10
            second = (n // (10**k)) % 10
            n //= 10
            if fisrt == second:
                cnt -= 1
                if cnt == 0:
                    return True
        return False
    return check

# solution use different situation as condition of returnning
    def check(x):
        while x // (10 ** k):
            if (x % 10) != (x // (10 ** k)) % 10:
                return False
            x //= 10
        return True
    return check
                
