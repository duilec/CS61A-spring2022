from cProfile import label
from os import name


class Rational:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self): # str for print without 「''」
        return f'{self.numerator}/{self.denominator}'

    def __repr__(self): # repr for direct reprsent without 「''」
        return f'Rational({self.numerator},{self.denominator})'

# a = Rational(1, 2)
# str(a)
# # '1/2'
# repr(a)
# # 'Rational(1,2)'
# print(a)
# # 1/2
# a
# # Rational(1,2) 

class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self): # repr for direct reprsent without 「''」
         return self.x

    def __str__(self): # str for print without 「''」
         return self.x * 2

class B:
    def __init__(self):
         print('boo!')
         self.a = []

    def add_a(self, a):
         self.a.append(a)

    def __repr__(self):
         print(len(self.a))
         ret = ''
         for a in self.a:
             ret += str(a)
         return ret

class Tree:

    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
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
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines
    
    def get_label(self):
        return self.label

def height(t):
     """Return the height of a tree.

     >>> t = Tree(3, [Tree(5, [Tree(1)]), Tree(2)])
     >>> height(t)
     2
     >>> t = Tree(3, [Tree(1), Tree(2, [Tree(5, [Tree(6)]), Tree(1)])])
     >>> height(t)
     3
     """
     "*** YOUR CODE HERE ***"
     if t.is_leaf():
          return 0 # each leaf can't add 1 height
     else:
          return 1 + max([height(b) for b in t.branches]) # each branche(include root) will add 1 height
     

def max_path_sum(t):
     """Return the maximum path sum of the tree.

     >>> t = Tree(1, [Tree(5, [Tree(1), Tree(3)]), Tree(10)])
     >>> max_path_sum(t)
     11
     """
     "*** YOUR CODE HERE ***"
     if t.is_leaf():
          return t.label # each leaf can add t.label
     else:
          return t.label + max([max_path_sum(b) for b in t.branches]) # each branche(include root) will add t.label

def find_path(t, x):
     """
     >>> t = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(15)])
     >>> find_path(t, 5)
     [2, 7, 6, 5]
     >>> find_path(t, 10)  # returns None
     """
     if t.label == x: # find to x
          return [t.label]
     for b in t.branches: # use iterable to find x
          path = find_path(b, x) 
          if path: # if not find that like a function with doing nothing so returns 'None' 
               return [t.label] + path

# t = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(15)])
# print(find_path(t, 5))

def do_noting():
    """a function with doing nothing so returns 'None' """

# print(do_noting())

def prune_small(t, n):
    """Prune the tree mutatively, keeping only the n branches
    of each node with the smallest label.

    >>> t1 = Tree(6)
    >>> prune_small(t1, 2)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_small(t2, 1)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_small(t3, 2)
    >>> t3
    Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])
    """
    # while True:
    #     if t.is_leaf():
    #         break
    #     largest = max([b.label for b in t.branches])
    #     # print(largest)
    #     t.branches = [b for b in t.branches if b.label != largest]
    #     # print("len", len(t.branches))
    #     if len(t.branches) <= n:
    #         break
    # # print("he")
    # for b in t.branches:
    #     prune_small(t, n)

    while len(t.branches) > n:
        largest = max([b.label for b in t.branches])
        t.branches = [b for b in t.branches if b.label != largest]
    for b in t.branches:
        prune_small(b, n) # use 'b' not use t !!!


# t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]), Tree(5, [Tree(3), Tree(4)])])
# # Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])
# prune_small(t3, 2)
# print(t3)

# def rp(t):
#     return len(t.branches)

# print(rp(t3))