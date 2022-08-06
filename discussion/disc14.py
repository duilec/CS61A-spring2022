class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
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


# Q1: Paths List
def paths(x, y):
    """Return a list of ways to reach y from x by repeated
    incrementing or doubling.
    >>> paths(3, 5)
    [[3, 4, 5]]
    >>> sorted(paths(3, 6))
    [[3, 4, 5, 6], [3, 6]]
    >>> sorted(paths(3, 9))
    [[3, 4, 5, 6, 7, 8, 9], [3, 4, 8, 9], [3, 6, 7, 8, 9]]
    >>> paths(3, 3) # No calls is a valid path
    [[3]]
    """
    if x == y:
        return [[x]]
    elif x > y: # add "[]", equals not operator
        return []
    else:
        a = paths(x + 1, y)
        b = paths(x * 2, y)
        # use "sublst" and "a + b" to get sublst of pathA with pathB and add current x
        return [[x] + sublst for sublst in a + b]

# Q2: Reverse
def reverse(lst):
    """Reverses lst using mutation.

    >>> original_list = [5, -1, 29, 0]
    >>> reverse(original_list)
    >>> original_list
    [0, 29, -1, 5]
    >>> odd_list = [42, 72, -8]
    >>> reverse(odd_list)
    >>> odd_list
    [-8, 72, 42]
    """
    "*** YOUR CODE HERE ***"
    start_ind = 0
    end_ind = len(lst) - 1
    # note: "start_ind >= end_ind" is overflow(even_lst) or equals(odd_lst)
    while start_ind < end_ind:
        temp = lst[start_ind]
        lst[start_ind] = lst[end_ind]
        lst[end_ind] = temp
        start_ind += 1
        end_ind -= 1

    # reference
    # use "midpoint" and "x, y = a, b" to replace
    # midpoint = len(lst) // 2 
    # last = len(lst) - 1 
    # for i in range(midpoint): 
    #     lst[i], lst[last - i] = lst[last - i], lst[i]

# Q3: Reverse Other
def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth)
    level have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    def reverse_odd_level(t, level):
        if t.is_leaf():
            return
        else:
            if level % 2 == 0: # t in even level, so t's branches in odd level
                midpoint = len(t.branches) // 2
                last = len(t.branches) - 1 
                for i in range(midpoint):
                    t.branches[i].label, t.branches[last - i].label = t.branches[last - i].label, t.branches[i].label
            for b in t.branches:
                reverse_odd_level(b, level + 1)
    return reverse_odd_level(t, 0) # the first deep is 0

    # reference
    # prepare new branches's labels early and use Boolean not use deep level
    def reverse_helper(t, need_reverse): 
        if t.is_leaf(): 
            return
    new_labs = [child.label for child in t.branches][::-1] 
    for i in range(len(t.branches)): 
        child = t.branches[i] 
        reverse_helper(child, not need_reverse) 
        if need_reverse: 
            child.label = new_labs[i]
    reverse_helper(t, True)

# Q4: Multiply Links
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Implementation Note: you might not need all lines in this skeleton code
    first, next_lst_of_lnks = 1, []
    for sub_lnks in lst_of_lnks:
        # If not all of the Link objects are of equal length, 
        # return a linked list whose length is that of the shortest linked list given. 
        if sub_lnks is Link.empty:
            return Link.empty
        else:
            first *= sub_lnks.first # mulitply first value
            next_lst_of_lnks.append(sub_lnks.rest) # built next "lst_of_lnks"
    rest = multiply_lnks(next_lst_of_lnks)
    return Link(first, rest)

# Q8: Phone Number Validator(Regex)
import re
def phone_number(string):
    """
    >>> phone_number("Song by Logic: 1-800-273-8255")
    True
    >>> phone_number("123 456 7890")
    True
    >>> phone_number("1" * 11) and phone_number("1" * 10) and phone_number("1" * 7)
    True
    >>> phone_number("The secret numbers are 4, 8, 15, 16, 23 and 42 (from the TV show Lost)")
    False
    >>> phone_number("Belphegor's Prime is 1000000000000066600000000000001")
    False
    >>> phone_number(" 1122334455 ")
    True
    >>> phone_number(" 11 22 33 44 55 ")
    False
    >>> phone_number("Tommy Tutone's '80s hit 867-5309 /Jenny")
    True
    >>> phone_number("11111111") # 8 digits isn't valid, has to be 11, 10, or 7
    False
    """
    # note: "^" or "$" in beginning of entire String or in the end of entire String
    # note: "\b"(Word Boundaries) wrapped up a "word" in the text
    return bool(re.search(r"(((\b[\d][-\s]?|\b)([\d]{3,3}[-\s]?))|\b)[\d]{3,3}[-\s]?[\d]{4,4}\b", string))


