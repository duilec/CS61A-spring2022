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
        return string + str(self.first) + '>' # print will use '<...>'

def range_link(start, end):
    """Return a Link containing consecutive integers
    from START to END, not including END.
    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    return Link(start, range_link(start + 1, end))

def map_link(f, ll):
    """Return a Link that contains f(x) for each x in Link LL.
    >>> square = lambda x: x * x
    >>> map_link(square, range_link(3, 6))
    Link(9, Link(16, Link(25)))
    """
    if ll == (): # we also can use 'll is Link.empty'
        return Link.empty
    return Link(f(ll.first), map_link(f, ll.rest)) 

# square = lambda x: x * x
# print(map_link(square, range_link(3, 6)))

def filter_link(f, ll):
    """Return a Link that contains only the elements x of Link LL
    for which f(x) is a true value.
    >>> is_odd = lambda x: x % 2 == 1
    >>> filter_link(is_odd, range_link(3, 6))
    Link(3, Link(5))
    """
    if ll is Link.empty: # we also can use 'll is Link.empty'
        return Link.empty
    if f(ll.first):
        return Link(ll.first, filter_link(f, ll.rest))
    else:
        return filter_link(f, ll.rest) # it is must use 'return' to filter ll.rest

# is_odd = lambda x: x % 2 == 1
# print(filter_link(is_odd, range_link(3, 100))) 

def insert_front(linked_list, new_val):
    """Inserts NEW_VAL in front of LINKED_LIST,
    returning new linked list.

    >>> ll = Link(1, Link(3, Link(5)))
    >>> insert_front(ll, 0)
    Link(0, Link(1, Link(3, Link(5))))
    """
    return Link(new_val, linked_list)

# ll = Link(1, Link(3, Link(5)))
# print(insert_front(ll, 0))

def add(ordered_list, new_val):
    """Add NEW_VAL to ORDERED_LIST, returning modified ORDERED_LIST.
    >>> s = Link(1, Link(3, Link(5)))
    >>> add(s, 0)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 3)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 4)
    Link(0, Link(1, Link(3, Link(4, Link(5)))))
    >>> add(s, 6)
    Link(0, Link(1, Link(3, Link(4, Link(5, Link(6))))))
    """
    if new_val < ordered_list.first:
        # add to front
        # we can't directly add to front because we built a new list
        # i.e.
        # ordered_list = Link(new_val, ordered_list)
        # then we will lost earily informations about recursion of 'new_val > ordered_list.first'
        # so we need use old list address(ordered_list) to contain earily informations
        old_list_first = ordered_list.first
        ordered_list.first = new_val
        ordered_list.rest = Link(old_list_first, ordered_list.rest)
    elif new_val > ordered_list.first and ordered_list.rest is Link.empty:
        # not find new_val < first and link to end
        ordered_list.rest = Link(new_val)
    elif new_val > ordered_list.first:
        # recursion to find new_val < first and add to rest
        # we can use recurion to 'obj_recursion_link'
        add(ordered_list.rest, new_val)
    return ordered_list

s = Link(1, Link(3, Link(5)))
add(s, 0)
# Link(0, Link(1, Link(3, Link(5))))
# add(s, 3)
# Link(0, Link(1, Link(3, Link(5))))
# add(s, 4)
# Link(0, Link(1, Link(3, Link(4, Link(5)))))
# add(s, 6)
print(s)
# Link(0, Link(1, Link(3, Link(4, Link(5, Link(6))))))

# it can't 
# def rp(ordered_list,new_val):
#     return [link.first for link in ordered_list if link.first > new_val]
# print(rp(s, 3))

# def test(val, ll):
#     return Link(val, ll)

# print(test(0, s))