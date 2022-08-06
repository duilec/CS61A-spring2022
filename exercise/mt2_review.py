import re


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

def ordered(s):
    """Is Link s ordered?

    >>> ordered(Link(1, Link(3, Link(4))))
    True
    >>> ordered(Link(1, Link(4, Link(3))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))))
    False
    """
    if s == Link.empty:
        return True
    if s.rest and s.first > s.rest.first:
        return False
    return ordered(s.rest)

# print(ordered(Link(1, Link(3, Link(4)))))
# True

def sol_ordered(s):
    """Is Link s ordered?

    >>> ordered(Link(1, Link(3, Link(4))))
    True
    >>> ordered(Link(1, Link(4, Link(3))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))))
    False
    """
    if s is Link.empty or s.rest is Link.empty:
        return True
    elif s.first > s.rest.first:
        return False
    else:
        return ordered(s.rest)

def ordered(s, key=lambda x: x):
    """Is Link s ordered?

    >>> ordered(Link(1, Link(3, Link(4))))
    True
    >>> ordered(Link(1, Link(4, Link(3))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))), key=abs)
    True
    >>> ordered(Link(-4, Link(-1, Link(3))))
    True
    >>> ordered(Link(-4, Link(-1, Link(3))), key=abs)
    False
    """
    if s == Link.empty:
        return True
    if s.rest and key(s.first) > key(s.rest.first):
        return False
    return ordered(s.rest,key)

def merge(s, t):
    """Return a sorted Link containing the elements of sorted s & t.

    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge(a, b)
    Link(1, Link(1, Link(4, Link(5))))
    >>> a
    Link(1, Link(5))
    >>> b
    Link(1, Link(4))
    """
    if s == Link.empty:
        return t
    if t == Link.empty:
        return s
    if s.first > t.first:
        return Link(t.first, Link(s.first, merge(s.rest, t.rest)))
    else:
        return Link(s.first, Link(t.first, merge(s.rest, t.rest)))

def sol_merge(s, t):
    """Return a sorted Link containing the elements of sorted s & t.

    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge(a, b)
    Link(1, Link(1, Link(4, Link(5))))
    >>> a
    Link(1, Link(5))
    >>> b
    Link(1, Link(4))
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.first, merge(s.rest, t))
    else:
        return Link(t.first, merge(s, t.rest))

def merge_in_place(s, t):
    """Return a sorted Link containing the elements of sorted s & t.

    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge_in_place(a, b)
    Link(1, Link(1, Link(4, Link(5))))
    >>> a
    Link(1, Link(1, Link(4, Link(5))))
    >>> b
    Link(1, Link(4, Link(5)))
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        s.rest = merge_in_place(s.rest, t) # s.first as the first, so s.rest link to 'merge_in_place(s.rest, t)
        return s # ret s as answer or the rest of upper level
    else:
        t.rest = merge_in_place(s, t.rest) # t.first as the first, so t.rest link to 'merge_in_place(t.rest, s)
        return t # ret s as answer or the rest of upper level

def min_abs_indices(s):
    """Indices of all elements in list s that have the smallest absolute value.

    >>> min_abs_indices([-4, -3, -2, 3, 2, 4])
    [2, 4]
    >>> min_abs_indices([1, 2, 3, 4, 5])
    [0]
    """
    smallest_val = abs(s[0])
    index = []
    # find the smallest value
    for val in s:
        if abs(val) < smallest_val:
            smallest_val = abs(val)
    # get index of the smallest value
    i = 0
    for val in s:
        if abs(val) == smallest_val:
            smallest_val = abs(val)
            index += [i]
        i += 1
    return index

def sol_min_abs_indices(s):
    """Indices of all elements in list s that have the smallest absolute value.

    >>> min_abs_indices([-4, -3, -2, 3, 2, 4])
    [2, 4]
    >>> min_abs_indices([1, 2, 3, 4, 5])
    [0]
    """
    min_abs = min(map(abs, s))
    return [i for i in range(len(s)) if abs(s[i]) == min_abs]

def largest_adj_sum(s):
    """Largest sum of two adjacent elements in a list s.

    >>> largest_adj_sum([-4, -3, -2, 3, 2, 4])
    6
    >>> largest_adj_sum([-4, 3, -2, -3, 2, -4])
    1
    """
    two_adjacent_sum_list = []
    # construct the list of two adjacent sum
    for i in range(len(s)):
        if i + 1 < len(s): # note: we can't out of len(s)
            two_adjacent_sum_list += [s[i] + s[i+1]]
    # find the largest sum in the list of two adjacent sum
    largest_sum = two_adjacent_sum_list[0]
    for val in two_adjacent_sum_list:
        if val > largest_sum:
            largest_sum = val
    return largest_sum

def sol_largest_adj_sum(s):
    """Largest sum of two adjacent elements in a list s.

    >>> largest_adj_sum([-4, -3, -2, 3, 2, 4])
    6
    >>> largest_adj_sum([-4, 3, -2, -3, 2, -4])
    1
    """
    return max([x + y for x, y in zip(s[:-1], s[1:])])
    # OR
    return max([s[i] + s[i + 1] for i in range(len(s) - 1)])
    # OR
    return max(map(lambda i: s[i] + s[i + 1], range(len(s) - 1)))

def all_have_an_equal(s):
    """Does every element equal some other element in s?

    >>> all_have_an_equal([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal([4, 3, 2, 3, 2, 4])
    True
    """
    equal_list = []
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                equal_list += [s[i]]
    if len(equal_list) == len(s):
        return True
    else:
        return False

def sol_all_have_an_equal(s):
    """Does every element equal some other element in s?

    >>> all_have_an_equal([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal([4, 3, 2, 3, 2, 4])
    True
    """
    return min([sum([1 for y in s if x == y]) for x in s]) > 1
    # OR
    return all([s[i] in s[:i] + s[i+1:] for i in range(len(s))])
    # OR
    return all(map(lambda x: s.count(x) > 1, s))

def digit_dict(s):
    """Map each digit d to the lists of elements in s that end with d.

    >>> digit_dict([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    end_d_dict = {}
    for i in range(10):
        for val in s:
            if val%10 == i:
                if end_d_dict.get(val%10):
                    old_val = end_d_dict.pop(val%10)
                    end_d_dict.update({i: old_val + [val] })
                else:
                    end_d_dict.update({i: [val]})
    return end_d_dict

def sol_digit_dict(s):
    """Map each digit d to the lists of elements in s that end with d.

    >>> digit_dict([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    return {i: [x for x in s if x % 10 == i]
            for i in range(10) if any([x % 10 == i for x in s])}
    # OR
    last_digits = list(map(lambda x: x % 10, s))
    return {i: [x for x in s if x % 10 == i]
            for i in range(10) if i in last_digits}

class Matrix:
    """
    >>> m = Matrix(3, 3, [1, 0, 1, 1, 1, 1, 0, 0, 1])
    >>> m
    Matrix(3, 3, [1, 0, 1, 1, 1, 1, 0, 0, 1])
    >>> print(m)
    1 0 1
    1 1 1
    0 0 1
    >>> m2 = Matrix(3, 2, [124, 56, 254, 0, 100, 225])
    >>> m2
    Matrix(3, 2, [124, 56, 254, 0, 100, 225])
    >>> print(m2)
    124 56 254
    0 100 225
    """
    def __init__(self, w, h, values):
        self.width = w
        self.height = h
        self.values = values

    def __repr__(self): # we can directly use __repr__ (i.e. '>>> m')
        return 'Matrix(' +  str(self.width) + ', ' + str(self.height) + ', ' + str(self.values) + ')'
    
    def __str__(self): # we use __str__  by print (i.e. 'print(m)')
        height = self.height
        width = self.width
        string_matrix = ''
        index = 0
        while height:
            while width:
                string_matrix += str(self.values[index]) + ' '
                width -= 1
                index += 1
            if height != 1:
                string_matrix += '\n'
            height -= 1
            width = self.width
        return string_matrix


# class Matrix:
#     """
#     >>> m2 = Matrix(3, 2, [124, 56, 254, 0, 100, 225])
#     >>> m2
#     Matrix(3, 2, [124, 56, 254, 0, 100, 225])
#     >>> print(m2)
#     124 56 254
#     0 100 225
#     """
#     def __init__(self, w, h, values):
#         self.width = w
#         self.height = h
#         self.values = values

#     def __repr__(self):
#         return f"Matrix({self.width}, {self.height}, {self.values})"

#     def __str__(self):
#         grid_lines = []
#         for h in range(self.height):
#             grid_line = []
#             for w in range(self.width):
#                 grid_line.append(str(self.values[(h * self.width) + w]))
#             grid_lines.append(' '.join(grid_line))
#         return '\n'.join(grid_lines)

class Table(Matrix):
    """
    >>> t = Table(2, 3, ['Ice Cream', 'Popularity'], ['Mint Chip', 2, 'Rocky Road', 1, 'Brownie Batter', 3])
    >>> t.headers
    ['Ice Cream', 'Popularity']
    >>> t
    Table(2, 3, ['Ice Cream', 'Popularity'], ['Mint Chip', 2, 'Rocky Road', 1, 'Brownie Batter', 3])
    >>> print(t)
    Ice Cream | Popularity
    -------------------
    Mint Chip 2
    Rocky Road 1
    Brownie Batter 3
    """

    def __init__(self, w, h, headers, values):
        self.width = w
        self.height = h
        self.headers = headers
        self.values = values

    def __repr__(self):
        return f"Table({self.width}, {self.height}, {self.headers}, {self.values})"
    
    def __str__(self):
        header_line = f"{self.headers[0]} | {self.headers[1]}\n"
        divider = f"-------------------\n"
        body = super().__str__()
        return header_line + divider + body

class Butterfly:
    """ See: https://monarchwatch.org/biology/cycle1.htm
    >>> b = Butterfly()
    >>> b.stage
    'egg'
    >>> b.next_stage()
    >>> b.stage
    'larva'
    >>> b.instar
    1
    >>> for _ in range(4): b.next_instar()
    >>> b.instar
    5
    >>> b.next_stage()
    >>> b.stage
    'pupa'
    >>> b.next_stage()
    >>> b.stage
    'adult'
    """
    stages = ['egg', 'larva', 'pupa', 'adult']
    num_instars = 5
    
    def __init__(self):
        self.stage_iter = iter(Butterfly.stages)
        self.instar = 1
        
    def next_stage(self):
        self.stage = next(self.stage_iter)
        if self.stage == 'larva':
            self.instar_iter = iter(Butterfly.stages)
            return self.instar_iter
    
    def next_instar(self):
        self.instar = next(Butterfly.num_instars)

class Butterfly:
    """ See: https://monarchwatch.org/biology/cycle1.htm
    >>> b = Butterfly()
    >>> b.stage
    'egg'
    >>> b.next_stage()
    >>> b.stage
    'larva'
    >>> b.instar
    1
    >>> for _ in range(4): b.next_instar()
    >>> b.instar
    5
    >>> b.next_stage()
    >>> b.stage
    'pupa'
    >>> b.next_stage()
    >>> b.stage
    'adult'
    """
    stages = ['egg', 'larva', 'pupa', 'adult']
    num_instars = 5
    
    def __init__(self):
        self.stage_iter = iter(self.stages)
        self.next_stage()
        
    def next_stage(self):
        self.stage = next(self.stage_iter, self.stages[-1])
        if self.stage == 'larva':
            self.instar_iter = iter(range(1, self.num_instars + 1))
            self.next_instar()

    def next_instar(self):
        self.instar = next(self.instar_iter, self.num_instars)