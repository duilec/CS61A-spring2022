from cmath import exp
import sys

from pair import *
from scheme_utils import *
from ucb import main, trace

import scheme_forms

##############
# Eval/Apply #
##############


def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # Evaluate atoms
    if scheme_symbolp(expr): # we also can get "builtin procedure" by symbol
        return env.lookup(expr)
    elif self_evaluating(expr): 
        return expr
    # All non-atomic expressions are lists (combinations)
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))
    first, rest = expr.first, expr.rest
    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS: # evaluate with special forms
        return scheme_forms.SPECIAL_FORMS[first](rest, env)
    # you can use "first in env.bindings and isinstance(env.bindings.get(first), MacroProcedure)"
    # instead of "isinstance(scheme_eval(first, env), MacroProcedure)"
    # check: "first" is symbol pointer?
    # if we don't check, promble 3 and 4 will error
    # because they call scheme_eval(first, env) in isinstance(scheme_eval(first, env), MacroProcedure)
    # and not execute builtin procedure(part of "else") or other func
    if scheme_symbolp(first) and isinstance(scheme_eval(first, env), MacroProcedure):
        formals = scheme_eval(first, env).formals
        body_expr = scheme_eval(first, env).body.first # note: remove the outermost bracket
        # bind values to formals in order to delay evaluate
        while formals != nil:
            env.bindings[formals.first] = rest.first
            formals, rest = formals.rest, rest.rest
        
        
        body_expr_with_agrs = scheme_eval(body_expr, env) # body expr with real agruments to finally evaluate
        return scheme_eval(body_expr_with_agrs, env)
    else:
        # BEGIN PROBLEM 3
        "*** YOUR CODE HERE ***"
        # executing builtin procedure
        def scheme_eval_with_one_agr(expr):
            return scheme_eval(expr, env=env)
        proceduce = scheme_eval(first, env)
        agrs = rest.map(scheme_eval_with_one_agr)
        return scheme_apply(proceduce, agrs, env)
        # END PROBLEM 3


def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        py_lst = []
        while args != nil:
            py_lst.append(args.first)
            args = args.rest
        if procedure.expect_env is True:
            py_lst.append(env)
        try:
            return procedure.py_func(*py_lst)
        except TypeError:
            raise SchemeError('incorrect number of arguments')
        # END PROBLEM 2
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        "*** YOUR CODE HERE ***"
        # need use old procedure.env
        new_env = procedure.env.make_child_frame(procedure.formals, args)
        lambda_expr = procedure.body
        return eval_all(lambda_expr, new_env)
        # END PROBLEM 9
    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        "*** YOUR CODE HERE ***"
        # don't need use old procedure.env
        # note: pass parent values to current frame, so we get dynamic scoping and we can use values of parent
        # new_env: the parent of the new call frame is the environment in which that call expression was evaluated.
        new_env = env.make_child_frame(procedure.formals, args)
        lambda_expr = procedure.body
        return eval_all(lambda_expr, new_env)
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)


def eval_all(expressions, env):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), create_global_frame())
    1
    >>> eval_all(read_line("(1 2)"), create_global_frame())
    2
    >>> x = eval_all(read_line("((print 1) 2)"), create_global_frame())
    1
    >>> x
    2
    >>> eval_all(read_line("((define x 2) x)"), create_global_frame())
    2
    """
    # BEGIN PROBLEM 6
    # return scheme_eval(expressions.first, env)  # replace this with lines of your own code
    # if expr is nil, ret None(equals 'undefined' in Scheme)
    # note: expr.first maybe is sub_expr(scheme list)
    val = None
    while expressions != nil:
        # tail call that the last expr of body in defined function(most of all)
        # consider begin, let, define(lambda) and cond
        if expressions.rest is nil:
            val = scheme_eval(expressions.first, env, True) # tail call: ret Unevalated
        else:
            val = scheme_eval(expressions.first, env, False) # ret evalated not in tail context
        expressions = expressions.rest
    return val
    # END PROBLEM 6


##################
# Tail Recursion #
##################

class Unevaluated:
    """An expression and an environment in which it is to be evaluated."""

    def __init__(self, expr, env):
        """Expression EXPR to be evaluated in Frame ENV."""
        self.expr = expr
        self.env = env


def complete_apply(procedure, args, env):
    validate_procedure(procedure)
    val = scheme_apply(procedure, args, env)
    if isinstance(val, Unevaluated):
        return scheme_eval(val.expr, val.env)
    else:
        return val


def optimize_tail_calls(unoptimized_scheme_eval):
    """Return a properly tail recursive version of an eval function."""
    def optimized_eval(expr, env, tail=False):
        """Evaluate Scheme expression EXPR in Frame ENV. If TAIL,
        return an Unevaluated containing an expression for further evaluation.
        """
        if tail and not scheme_symbolp(expr) and not self_evaluating(expr):
            return Unevaluated(expr, env)

        # result must be a Unevaluated
        result = Unevaluated(expr, env)
        # BEGIN PROBLEM EC
        "*** YOUR CODE HERE ***"
        # unoptimized_scheme_eval may calls scheme_eval(expr, env, False) or scheme_eval(expr, env, True) recursivly
        while isinstance(result, Unevaluated):
            # next Unevaluated(non-atom expr that is tail of recursion)
            result = unoptimized_scheme_eval(result.expr, result.env) 
        return result # until it can be evaluated(atom expr)
        # END PROBLEM EC
    return optimized_eval

################################################################
# Uncomment the following line to apply tail call optimization #
################################################################

# note: we passes the agrs(expr, env, _=None/True/False) to optimize_tail_calls 
# because we use orginal scheme_eval(expr, env, _=None/True/False)
# After uncommenting this line
# we using scheme_eval()  equalsusing optimize_tail_calls()
# but unoptimized_scheme_eval is **orginal** scheme_eval()
scheme_eval = optimize_tail_calls(scheme_eval)