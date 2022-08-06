def trampoline(f, *args):
    v = f(*args)
    while callable(v):
        v = v() # assigns next func(factorial_thunked(n-1, k*n)), func is callable
    return v # until n == 0, ret k, v = k, number is not callable 

def factorial_thunked(n, k):
    if n == 0:
        return k # number is not callable 
    else:
        # this is a thunk
        return lambda: factorial_thunked(n-1, k*n) # lambda is a func and func is callable
