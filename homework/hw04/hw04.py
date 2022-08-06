from calendar import prcal


def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    if lst1 == []:
        return lst2
    elif lst2 == []:
        return lst1
    else:
        new_lst1 = []
        insert_index = len(lst1)
        for index in range(len(lst1)):
            if lst2[0] < lst1[index]:
                insert_index = index
                break
        
        for index in range(len(lst1)):
            if index == insert_index:
                new_lst1 += [lst2[0]]
            new_lst1 += [lst1[index]]
        
        if insert_index == len(lst1):
            new_lst1 += lst2
        
        return merge(new_lst1, lst2[1:])


class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2021
    >>> dime = mint.create(Dime)
    >>> dime.year
    2021
    >>> Mint.present_year = 2101  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2021
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2101
    >>> Mint.present_year = 2176     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2021 # Mint.present_year = 2101  # Time passes(this is assignment )

    def __init__(self):
        self.update()

    def create(self, coin):
        "*** YOUR CODE HERE ***"
        # if coin == Nickel:
        #     return Nickel(self.year) # we must use 'return' to call this function
        # elif coin == Dime:
        #     return Dime(self.year) # The mint has not updated its stamp yet, so we use 'self.year', not use 'present.year'
        return coin(self.year) # we can see coin as a class

    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = self.present_year # self.year is private by '__init__'


class Coin:
    cents = None  # will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year # self.year is private by '__init__'
        
    def worth(self):
        "*** YOUR CODE HERE ***"
        if Mint.present_year == self.year: # the condition is new coin
            return self.cents
        else: # the condition is old coin
            return self.cents + (Mint.present_year - self.year - 50)

class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'"
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'"
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'"
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'"
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'"
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'"
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'"

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'"
    """
    "*** YOUR CODE HERE ***"
    stocks = 0
    balance = 0

    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price
    
    def vend(self):
        if (self.stocks == 0):
            print(f"'Nothing left to vend. Please restock.'" + f'"')
        elif (self.balance < self.product_price):
            print(f"'You must add ${self.product_price - self.balance} more funds.'" + f'"')
        elif (self.balance == self.product_price):
            print(f"'Here is your {self.product_name}.'" + f'"')
            self.balance -= self.product_price
            self.stocks -= 1
        else:
            print(f"'Here is your {self.product_name} and ${self.balance - self.product_price} change.'" + f'"')
            self.balance = 0
            self.stocks -= 1

    def add_funds(self, funds):
        self.balance += funds
        if (self.stocks == 0):
            print(f"'Nothing left to vend. Please restock. Here is your ${self.balance}.'" + f'"')
            self.balance = 0
        else:
            print(f"'Current balance: ${self.balance}'")

    def restock(self, stock):
        self.stocks += stock
        print(f"'Current {self.product_name} stock: {self.stocks}'")