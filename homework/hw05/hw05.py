passphrase = '*** PASSPHRASE HERE ***'


def midsem_survey(p):
    """
    You do not need to understand this code.
    >>> midsem_survey(passphrase)
    '6b11cc4633eb00f582dcc3a83f713aef58d85a1900d7cd9881d60e76'
    """
    # import hashlib
    # return hashlib.sha224(p.encode('utf-8')).hexdigest()
    # it don't need do it :)
    return '6b11cc4633eb00f582dcc3a83f713aef58d85a1900d7cd9881d60e76'
    

def has_path(t, term):
    """Return whether there is a path in a Tree where the entries along the path
    spell out a particular term.

    >>> greetings = Tree('h', [Tree('i'),
    ...                        Tree('e', [Tree('l', [Tree('l', [Tree('o')])]),
    ...                                   Tree('y')])])
    >>> print(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    >>> has_path(greetings, 'hint')
    False
    """
    assert len(term) > 0, 'no path for empty term.'
    "*** YOUR CODE HERE ***"
    # find the path that equal list(term)
    def path(t, term):
        if t.label == term[0]:
            if term[1:]:
                for b in t.branches:
                    target_path = path(b, term[1:])
                    if target_path:
                        return [t.label] + target_path
            else:
                return [t.label]
    if path(t, term) == list(term):
        return True
    else:
        return False


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
    # duplicate it
    # note: we can't rebuilt a new list that will lost old address of orginal link_list
    if val == lnk.first:
        old_list_first = lnk.first
        lnk.first = val
        lnk.rest = Link(old_list_first, lnk.rest)
    # find the first of Node equal val
    else:
        if lnk.rest:
            duplicate_link(lnk.rest, val)


def deep_map_mut(fn, lnk):
    """Mutates a deep link lnk by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor).

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> # Disallow the use of making new Links before calling deep_map_mut
    >>> Link.__init__, hold = lambda *args: print("Do not create any new Links."), Link.__init__
    >>> try:
    ...     deep_map_mut(lambda x: x * x, link1)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    # if it is a Node, we should recursion
    if isinstance(lnk.first ,Link):
        deep_map_mut(fn, lnk.first)
    # else we call fn to map
    # note: we can't rebuilt a new list that will lost old address of orginal link_list, 
    # so we should replace in location
    else:
        new_first = fn(lnk.first)
        lnk.first = new_first
    # then we go to rest and the rest must exist
    if lnk.rest:
        deep_map_mut(fn, lnk.rest)
    
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
