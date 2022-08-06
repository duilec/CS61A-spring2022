class Tree:

    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches) # has list of child

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

def count_leaves(t):
    """Returns the number of leaf nodes in T."""
    if t.is_leaf():
        return 1
    else:
        leaves_under = 0
        for b in t.branches:
            leaves_under += count_leaves(b)
        return leaves_under

def print_tree(t, indent=0):
    """Prints the labels of T with depth-based indent.
    >>> t = Tree(3, [Tree(1), Tree(2, [Tree(1), Tree(1)])])
    >>> print(t)
    3
      1
      2
        1
        1
    """
    for _ in range(indent):
        print(" ", end="")
    print(t.label)
    for b in t.branches:
        print_tree(b, indent + 2)



t = Tree(3, [
            Tree(1),
            Tree(2, [
                    Tree(1),
                    Tree(1)
                    ])
            ])

# print_tree(t, indent=0)

# t.label                  # 3
# print(t.label)
# t.is_leaf()              # False
# print(t.is_leaf())
# t.branches[0].is_leaf()  # True
# print(t.branches[0].is_leaf())

def count_leaves(t):
    """Returns the number of leaf nodes in T."""
    if t.is_leaf():
        return 1
    else:
        leaves_under = 0
        for b in t.branches:
            leaves_under += count_leaves(b)
        return leaves_under

def leaves(t):
    """Return a list containing the leaf labels of T.
    >>> t = Tree(20, [Tree(12, [Tree(9, [Tree(7), Tree(2)]), Tree(3)]), Tree(8, [Tree(4), Tree(4)])])
    >>> leaves(t)
    [7, 2, 3, 4, 4]
    """
    if t.is_leaf():
        return [t.label]
    else:
        leaves_list = []
        for b in t.branches:
            leaves_list += leaves(b)
        return leaves_list
# TypeError: 'list' object is not callable becasue biult_in func_name has conflict with varible_name

def leaves_v2(t):
    if t.is_leaf():
        return [t.label]
    else:
        leaves_list = [leaves_v2(b) for b in t.branches]
        return sum(leaves_list, []) # summation with '[]'

t2 = Tree(20, [Tree(12, [Tree(9, [Tree(7), Tree(2)]), Tree(3)]), Tree(8, [Tree(4), Tree(4)])])
# print(leaves(t2))
# print(leaves_v2(t2))

def count_paths(t, total):
    """Return the number of paths from the root to any node in T
    for which the labels along the path sum to TOTAL.

    >>> t = Tree(3, [Tree(-1), Tree(1, [Tree(2, [Tree(1)]), Tree(3)]), Tree(1, [Tree(-1)])])
    >>> count_paths(t, 3)
    2
    >>> count_paths(t, 4)
    2
    >>> count_paths(t, 5)
    0
    >>> count_paths(t, 6)
    1
    >>> count_paths(t, 7)
    2
    """
    if total == t.label:
        find_a_path = 1 # you can't directly ret, because we woult to count path 
    else:
        find_a_path = 0
    # you can use a varible to add (it is a tip of recursion)
    return find_a_path + sum(count_paths(b , total - t.label) for b in t.branches)
    
t3 = Tree(3, [Tree(-1), Tree(1, [Tree(2, [Tree(1)]), Tree(3)]), Tree(1, [Tree(-1)])])

# print(count_paths(t3, 7))

def prune(t, n):
    """Prune all sub-trees whose label is n.
    >>> t = Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2, [Tree(1), Tree(1, [Tree(0), Tree(1)])])])
    >>> prune(t, 1)
    >>> t
    Tree(3, [Tree(2)])
    """
    t.branches = [ b for b in t.branches if b.label != n] # build a new branches by cutting 'b.label != n'
    for b in t.branches: # continue to build a new_new breanches by cutting 'b.label != n'
        prune(b, n)

t4 = Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2, [Tree(1), Tree(1, [Tree(0), Tree(1)])])])

prune(t4, 1)

# print(t4)