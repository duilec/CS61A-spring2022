class Pair:
    """Represents the built-in pair data structure in Scheme."""
    def __init__(self, first, rest):
        self.first = first
        if not scheme_valid_cdrp(rest):
            raise SchemeError("cdr can only be a pair, nil, or a promise but was {}".format(rest))
        self.rest = rest

    def map(self, fn):
        """Maps fn to every element in a list, returning a new
        Pair.

        >>> Pair(1, Pair(2, Pair(3, nil))).map(lambda x: x * x)
        Pair(1, Pair(4, Pair(9, nil)))
        """
        assert isinstance(self.rest, Pair) or self.rest is nil, \
            "rest element in pair must be another pair or nil"
        return Pair(fn(self.first), self.rest.map(fn))

    def __repr__(self):
        return 'Pair({}, {})'.format(self.first, self.rest)

class nil:
    """Represents the special empty pair nil in Scheme."""
    def map(self, fn):
        return nil
    def __getitem__(self, i):
         raise IndexError('Index out of range')
    def __repr__(self):
        return 'nil'

nil = nil() # this hides the nil class *forever*


# q5

# from fall20 disc11
def calc_apply(fn, args):
    """Applies a Calculator operation to a list of numbers."""
    return fn(args)


def calc_eval(exp):
    if isinstance(exp, Pair): # Call expressions
        return calc_apply(calc_eval(exp.first), exp.rest.map(calc_eval))
    elif exp in OPERATORS:      # Names
        return OPERATORS[exp]
    else:                       # Numbers
        return exp

def floor_div(expr):
    """
    >>> calc_eval(Pair("//", Pair(10, Pair(10, nil))))
    1
    >>> calc_eval(Pair("//", Pair(20, Pair(2, Pair(5, nil)))))
    2
    >>> calc_eval(Pair("//", Pair(6, Pair(2, nil))))
    3
    """
    "*** YOUR CODE HERE ***"
    dividend = expr.first
    while expr != nil: # test itself(expr)!!!
        divisor = expr.rest.first
        dividend //= divisor
        expr = expr.rest.rest
    return dividend

OPERATORS = { "//": floor_div }
    # sol
    # dividend = expr.first
    # expr = expr.rest
    # while expr != nil: 
    #     divisor = expr.first
    #     dividend //= divisor
    #     expr = expr.rest
    # return dividend


# q6
def calc_eval(exp):
    if isinstance(exp, Pair):
        if exp.first == "and": # and expressions
            return eval_and(exp.rest)
        else:                   # Call expressions
            return calc_apply(calc_eval(exp.first), exp.rest.map(calc_eval))
    elif exp in OPERATORS:      # Names
        return OPERATORS[exp]
    else:                       # Numbers
        return exp

# in scheme
# (and [test] ...)
# Evaluate the tests in order, returning the first false value. 
# If no test is false, return the last test. 
# If no arguments are provided, return #t.
def eval_and(operands):
    """
    >>> calc_eval(Pair("and", Pair(1, nil)))
    1
    >>> calc_eval(Pair("and", Pair(False, Pair("1", nil))))
    False
    """
    "*** YOUR CODE HERE ***"
    if operands == nil:
        return True
    while True:
        if calc_eval(operands.first) == False: # Maybe operands.first is sub-call exprssion
            return False
        if operands.rest == nil:
            return operands.first
        operands = operands.rest

OPERATORS = {}

# solution
# def eval_and(operands):
#     """
#     >>> calc_eval(Pair("and", Pair(1, nil)))
#     1
#     >>> calc_eval(Pair("and", Pair(False, Pair("1", nil))))
#     False
#     """
#     curr, val = operands, True 
#     while curr is not nil:
#         val = calc_eval(curr.first) 
#         if val is False:
#             return False 
#         curr = curr.rest
#     return val

# OPERATORS = {}

# q7
bindings = {}
def calc_eval(exp):
    if isinstance(exp, Pair):
        if exp.first == "and": # and expressions[paste your answer from the earlier]
            return eval_and(exp.rest)
        elif exp.first == "define": # define expressions
            return eval_define(exp.rest)
        else:                   # Call expressions
            return calc_apply(calc_eval(exp.first), exp.rest.map(calc_eval))
    elif exp in bindings: # Looking up variables
        "*** YOUR CODE HERE ***"
        return bindings.get(exp)
    elif exp in OPERATORS:      # Looking up procedures
        return OPERATORS[exp]
    else:                       # Numbers
        return exp

def eval_define(expr):
    """
    >>> calc_eval(Pair("define", Pair("a", Pair(1, nil))))
    'a'
    >>> calc_eval("a")
    1
    """
    "*** YOUR CODE HERE ***"
    added = {expr.first: calc_eval(expr.rest.first)} # Maybe expr.rest.first is sub-call exprssion
    bindings.update(added)
    return expr.first

OPERATORS = {}

