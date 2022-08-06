class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def remove_all(link, value):
    """Remove all the nodes containing value in link. Assume that the
    first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    "*** YOUR CODE HERE ***"
    # remove_helper(link, prev_link=None, value)
    def remove_helper(link, prev_link, value):
        if link == Link.empty:
            return
        if link.first == value:
            if link.rest:
                link.first = link.rest.first
                link.rest = link.rest.rest
                return remove_helper(link, prev_link, value)
            else:
                # we need prev_link when 'link.first == value' but 'link.rest is Link.empty'
                prev_link.rest = Link.empty 
                return
        return remove_helper(link.rest, link, value)
    remove_helper(link, None, value)

# l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))   
# print(l1)
# # <0 2 2 3 1 2 3>
# remove_all(l1, 2)
# print(l1)
# # <0 3 1 3>
# remove_all(l1, 3)
# print(l1)
# # <0 1>
# remove_all(l1, 3)
# print(l1)
# # <0 1>

def filter_iter(iterable, f):
    """
    Implement a generator function called filter_iter(iterable, f) 
    that only yields elements of iterable for which f returns True.

    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    "*** YOUR CODE HERE ***"
    for num in iterable: 
        if f(num):
            yield num

# is_even = lambda x: x % 2 == 0
# print(list(filter_iter(range(5), is_even))) # a list of the values yielded from the call to filter_iter
# # [0, 2, 4]
# all_odd = (2*y-1 for y in range(5))
# print(list(filter_iter(all_odd, is_even)))
# # []
# naturals = (n for n in range(1, 100))
# s = filter_iter(naturals, is_even)
# print(next(s))
# # 2
# print(next(s))
# # 4

def hailstone(n):
    """Yields the elements of the hailstone sequence starting at n.
       At the end of the sequence, yield 1 infinitely.

    >>> hail_gen = hailstone(10)
    >>> [next(hail_gen) for _ in range(10)]
    [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
    >>> next(hail_gen)
    1
    """
    "*** YOUR CODE HERE ***"
    
    while n > 1:
        yield n
        if n % 2 == 0:
            n //= 2 
        else:
            n = n * 3 + 1
        yield from hailstone(n)
    # At the end of the sequence, yield 1 infinitely.  
    while True:
        yield 1
    
# hail_gen = hailstone(10)
# print([next(hail_gen) for _ in range(110)])
# # [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
# print(next(hail_gen))
# # 1

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    if n < 2: # end of primes_gen(n - 1)
        return
    # if it is prime
    # note: any([]) => False
    if n == 2 or any([True for i in range(2, n) if n % i == 0]) is False:
        yield n
    yield from primes_gen(n - 1)

pg = primes_gen(7)
print(list(pg))
# [7, 5, 3, 2]