def tree(root_label, branches=[]):
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [root_label] + list(branches)
def label(tree):
        return tree[0]
def branches(tree):
        return tree[1:]
def is_tree(tree):
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
def is_leaf(tree):
        return not branches(tree)


def fib_tree(n):
        if n == 0 or n == 1:
            return tree(n)
        else:
            left, right = fib_tree(n-2), fib_tree(n-1)
            fib_n = label(left) + label(right)
            return tree(fib_n, [left, right])

# print(fib_tree(5))

def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m."""

    """The labels at the leaves of a partition tree express 
    whether the path from the root of the tree to the leaf 
    represents a successful partition of n."""

    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])

# print(partition_tree(3, 2))
# [2, [2, [False], [1, [True], [False]]], [1, [1, [1, [True], [False]], [False]], [False]]]
[2, [True], [1, [1, [True], [False]], [False]]]

def print_parts(tree, partition=[]):
    """Printing the partitions from a partition tree is another tree-recursive process 
    that traverses the tree, constructing each partition as a list. 
    Whenever a True leaf is reached, the partition is printed."""

    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)

# print_parts(partition_tree(6, 4))

def right_binarize(tree):
    """Construct a right-branching binary tree."""

    """A binary tree is either a leaf or a sequence of at most two binary trees. 
    A common tree transformation called binarization computes a binary tree from an original tree 
    by grouping together adjacent branches."""
    
    if is_leaf(tree):
        return tree
    if len(tree) > 2:
        tree = [tree[0], tree[1:]]
    return [right_binarize(b) for b in tree]

print(right_binarize([1, 2, 3, 4, 5, 6, 7]))
[1, [2, [3, [4, [5, [6, 7]]]]]]

