import re


def address_oneline(text):
    """
    Finds and returns if there are expressions in text that represent the first line
    of a US mailing address.

    >>> address_oneline("110 Sproul Hall, Berkeley, CA 94720")
    True
    >>> address_oneline("What's at 39177 Farwell Dr? Is there a 39177 Nearwell Dr?")
    True
    >>> address_oneline("I just landed at 780 N McDonnell Rd, and I need to get to 1880-ish University Avenue. Help!")
    True
    >>> address_oneline("123 Le Roy Ave")
    True
    >>> address_oneline("110 Unabbreviated Boulevard")
    False
    >>> address_oneline("790 lowercase St")
    False
    """
    block_number = r'[\d]{3,5}'
    cardinal_dir = r'\b([NEWS]\s)?\b'  # whitespace is important!
    street = r'([A-Z][a-z\s]+)+'
    type_abbr = r'\b([A-Z][a-z\s]{1,4})\b'
    street_name = f"{cardinal_dir}{street}{type_abbr}"
    return bool(re.search(f"{block_number}\s{street_name}", text)) # has a "\s" in two name


def prune_min(t):
    """Prune the tree mutatively.

    >>> t1 = Tree(6)
    >>> prune_min(t1)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_min(t2)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(3, [Tree(1), Tree(2)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_min(t3)
    >>> t3
    Tree(6, [Tree(3, [Tree(1)])])
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return
    else:
        if t.branches[0].label > t.branches[1].label:
            max_b = t.branches[0]
            min_b = t.branches[1]
        else:
            max_b = t.branches[1]
            min_b = t.branches[0]
        t.branches.remove(max_b)
        prune_min(min_b)
        
def add_trees(t1, t2):
    """
    >>> numbers = Tree(1,
    ...                [Tree(2,
    ...                      [Tree(3),
    ...                       Tree(4)]),
    ...                 Tree(5,
    ...                      [Tree(6,
    ...                            [Tree(7)]),
    ...                       Tree(8)])])
    >>> print(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print(add_trees(Tree(2), Tree(3, [Tree(4), Tree(5)])))
    5
      4
      5
    >>> print(add_trees(Tree(2, [Tree(3)]), Tree(2, [Tree(3), Tree(4)])))
    4
      6
      4
    >>> print(add_trees(Tree(2, [Tree(3, [Tree(4), Tree(5)])]), \
    Tree(2, [Tree(3, [Tree(4)]), Tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    if t1.is_leaf() and t2.is_leaf(): # not any branches
        return Tree(t1.label + t2.label)
    elif t1.is_leaf(): # has branches of t2
        return Tree(t1.label + t2.label, t2.branches)
    elif t2.is_leaf(): # has branches of t1
        return Tree(t1.label + t2.label, t1.branches)
    
    # get trees(t1.branches, t2.branches) of same position ,then recursivly add trees to bulid new branches
    # question: I don't know why I can't directly use "for b1, b2 in t1_same_bs, t2_same_bs" but index is useful
    same_add_bs = []
    zip_two_tree = zip(t1.branches, t2.branches)
    t1_same_bs, t2_same_bs = zip(*zip_two_tree)
    for i in range(len(t1_same_bs)):
        same_add_bs.append(add_trees(t1_same_bs[i], t2_same_bs[i]))
    
    # remainder branches may is empty, t1.branches remain or t2.branches remain
    remainder_bs = [] 
    if len(t1.branches) > len(t2.branches):
        remainder_bs = t1.branches[len(t1_same_bs):]
    elif len(t1.branches) < len(t2.branches):
        remainder_bs = t2.branches[len(t2_same_bs):]
    
    # add twe label and use new branches to build a new Tree
    t = Tree(t1.label + t2.label, same_add_bs + remainder_bs)
    return t

def make_test_random():
    """A deterministic random function that cycles between
    [0.0, 0.1, 0.2, ..., 0.9] for testing purposes.

    >>> random = make_test_random()
    >>> random()
    0.0
    >>> random()
    0.1
    >>> random2 = make_test_random()
    >>> random2()
    0.0
    """
    rands = [x / 10 for x in range(10)]

    def random():
        rand = rands[0]
        rands.append(rands.pop(0))
        return rand
    return random


random = make_test_random()

# Phase 1: The Player Class


class Player:
    """
    >>> random = make_test_random()
    >>> p1 = Player('Hill')
    >>> p2 = Player('Don')
    >>> p1.popularity
    100
    >>> p1.debate(p2)  # random() should return 0.0
    >>> p1.popularity
    150
    >>> p2.popularity
    100
    >>> p2.votes
    0
    >>> p2.speech(p1)
    >>> p2.votes
    10
    >>> p2.popularity
    110
    >>> p1.popularity
    135

    """

    def __init__(self, name):
        self.name = name
        self.votes = 0
        self.popularity = 100

    def debate(self, other):
        "*** YOUR CODE HERE ***"
        probability = max(0.1, self.popularity / (self.popularity + other.popularity))
        if random() < probability:
            self.popularity += 50
        else:
            self.popularity -= 50
        if self.popularity < 0:
            self.popularity = 0

    def speech(self, other):
        "*** YOUR CODE HERE ***"
        gain = self.popularity // 10
        other_lost = other.popularity // 10
        self.votes += gain
        self.popularity += gain
        other.popularity -= other_lost
    def choose(self, other):
        return self.speech(other) # note: has a agru of other player!!!


# Phase 2: The Game Class
class Game:
    """
    >>> p1, p2 = Player('Hill'), Player('Don')
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True

    """

    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.turn = 0

    def play(self):
        while not self.game_over():
            "*** YOUR CODE HERE ***"
            self.p1.choose(self.p2)
            self.p2.choose(self.p1)
            self.turn += 2
            # print("self.p1.votes: "+str(self.p1.votes))
            # print("self.p2.votes: "+str(self.p2.votes))
        return self.winner()

    def game_over(self):
        return max(self.p1.votes, self.p2.votes) >= 50 or self.turn >= 10

    def winner(self):
        "*** YOUR CODE HERE ***"
        if self.p1.votes == self.p2.votes:
            return None
        else:
            if self.p1.votes > self.p2.votes:
                return self.p1
            else:
                return self.p2


# Phase 3: New Players
class AggressivePlayer(Player):
    """
    >>> random = make_test_random()
    >>> p1, p2 = AggressivePlayer('Don'), Player('Hill')
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True

    """

    def choose(self, other):
        "*** YOUR CODE HERE ***"
        if self.popularity <= other.popularity:
            return self.debate(other)
        else:
            return self.speech(other)


class CautiousPlayer(Player):
    """
    >>> random = make_test_random()
    >>> p1, p2 = CautiousPlayer('Hill'), AggressivePlayer('Don')
    >>> p1.popularity = 0
    >>> p1.choose(p2) == p1.debate
    True
    >>> p1.popularity = 1
    >>> p1.choose(p2) == p1.debate
    False

    """

    def choose(self, other):
        "*** YOUR CODE HERE ***"
        if self.popularity == 0:
            return self.debate # testing without argu of "other"!!! so "self.debate(other)" is right
        else:
            return self.speech(other)

def intersection(lst_of_lsts):
    """Returns a list of distinct elements that appear in every list in
    lst_of_lsts.

    >>> lsts1 = [[1, 2, 3], [1, 3, 5]]
    >>> intersection(lsts1)
    [1, 3]
    >>> lsts2 = [[1, 4, 2, 6], [7, 2, 4], [4, 4]]
    >>> intersection(lsts2)
    [4]
    >>> lsts3 = [[1, 2, 3], [4, 5], [7, 8, 9, 10]]
    >>> intersection(lsts3)         # No number appears in all lists
    []
    >>> lsts4 = [[3, 3], [1, 2, 3, 3], [3, 4, 3, 5]]
    >>> intersection(lsts4)         # Return list of distinct elements
    [3]
    """
    elements = []
    "*** YOUR CODE HERE ***"
    equal_count = 0
    equal_goal = len(lst_of_lsts) - 1
    for sub_lst0_val in lst_of_lsts[0]:
        for sub_lst in lst_of_lsts[1:]:    
            for sub_lstx_val in sub_lst:
                if sub_lst0_val == sub_lstx_val:
                    equal_count += 1
                    break # avoid repeated val in sub_lstx (eg.sub_lstx = [4, 4])
        if equal_count == equal_goal and sub_lst0_val not in elements:
            elements.append(sub_lst0_val)
            equal_count = 0 # remeber: we should reset equal_count ecah turn
    return elements

    # reference
    # use "in" and "condition"
    elements = []
    for elem in lst_of_lsts[0]:
        condition = elem not in elements
        for lst in lst_of_lsts[1:]:
            if elem not in lst:
                condition = False
        if condition:
            elements = elements + [elem]
    return elements 

def deck(suits, ranks):
    """Creates a deck of cards (a list of 2-element lists) with the given
    suits and ranks. Each element in the returned list should be of the form
    [suit, rank].

    >>> deck(['S', 'C'], [1, 2, 3])
    [['S', 1], ['S', 2], ['S', 3], ['C', 1], ['C', 2], ['C', 3]]
    >>> deck(['S', 'C'], [3, 2, 1])
    [['S', 3], ['S', 2], ['S', 1], ['C', 3], ['C', 2], ['C', 1]]
    >>> deck([], [3, 2, 1])
    []
    >>> deck(['S', 'C'], [])
    []
    """
    "*** YOUR CODE HERE ***"
    lst = []
    if suits is [] or ranks is []:
        return lst
    for suit in suits:
        for rank in ranks:
            lst.append([suit, rank])
    return lst

    # reference
    # use "[]" and "for in "
    # if lst is empty, python will end the loop 
    return [[suit, rank] for suit in suits
                        for rank in ranks]  

def pascal_row(s):
    """
    >>> a = Link.empty
    >>> for _ in range(5):
    ...     a = pascal_row(a)
    ...     print(a)
    <1>
    <1 1>
    <1 2 1>
    <1 3 3 1>
    <1 4 6 4 1>
    """
    "*** YOUR CODE HERE ***"
    # my solution: use recursion
    def built_row(save_val, s):
        if s is Link.empty:
            return Link(1)       
        return Link(save_val + s.first, built_row(s.first, s.rest))
    
    if s is Link.empty:
        return Link(1)
    return Link(1, built_row(s.first, s.rest))

    # reference
    # use "while"
    if s is Link.empty:
        return Link(1)
    start = Link(1)
    last, current = start, s
    while current.rest is not Link.empty:
        last.rest = Link(current.first + current.rest.first)
        last, current = last.rest, current.rest
    last.rest = Link(1)
    return start

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
