def make_keeper(n):
    def func(cond):
        while n:
            if cond(n):
                print(n)
            n -= 1
    return func(n)
    
def is_even(x): 
    return x % 2 == 0

make_keeper(5)(is_even)