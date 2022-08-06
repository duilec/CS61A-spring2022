def f(x):
    return g(x - 1)
    
def g(y):
    left = h(y)
    right = h(1 // y)
    return abs(left - right)
    
def h(z):
    return z * z
    
print(f(12))