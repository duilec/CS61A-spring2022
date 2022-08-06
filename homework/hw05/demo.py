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


def chain(t):
    def chain_path(t):
        if t.is_leaf():
            return [t.label]
        for b in t.branches:
            if b.label == t.label:
                path = chain_path(b)
                # if all labels of node are same(i.e. the path exist), we return True
                if path:
                    return [t.label] + path
    if chain_path(t):
        return True
    else:
        return False

# all_fives = Tree(5, [Tree(5), Tree(5, [Tree(5)])])
# print(chain(all_fives))
# # True
# t1 = Tree(1, [Tree(3, [Tree(4)]), Tree(1)])
# print(chain(t1))
# # True
# t2 = Tree(1, [Tree(3, [Tree(4)]), Tree(5)])
# print(chain(t2))
# # False

def duplicate_link(lnk, val):
    """Mutates `lnk` such that if there is a linked list
    node that has a first equal to value, that node will
    be duplicated. Note that you should be mutating the
    original link list.

    >>> x = Link(5, Link(4, Link(3)))
    >>> duplicate_link(x, 5)
    >>> x
    Link(5, Link(5, Link(4, Link(3))))
    >>> y = Link(2, Link(4, Link(6, Link(8))))
    >>> duplicate_link(y, 10)
    >>> y
    Link(2, Link(4, Link(6, Link(8))))
    """
    "*** YOUR CODE HERE ***"
    # print("he")
    if val == lnk.first:
        old_list_first = lnk.first
        lnk.first = val
        lnk.rest = Link(old_list_first, lnk.rest)
    else:
        if lnk.rest:
            duplicate_link(lnk.rest, val)

x = Link(5, Link(4, Link(3)))
duplicate_link(x, 3)
print(x)
# Link(5, Link(5, Link(4, Link(3))))
y = Link(2, Link(4, Link(6, Link(8))))
duplicate_link(y, 6)
print(y)
# Link(2, Link(4, Link(6, Link(8))))



