class SmartFridge:
    """"
    >>> fridgey = SmartFridge()
    >>> fridgey.add_item('Mayo', 1)
    'I now have 1 Mayo'
    >>> fridgey.add_item('Mayo', 2)
    'I now have 3 Mayo'
    >>> fridgey.use_item('Mayo', 2.5)
    'I have 0.5 Mayo left'
    >>> fridgey.use_item('Mayo', 0.5)
    'Uh oh, buy more Mayo!'
    """

    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
        if item in self.items: # item in items?
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        # Mayo is a string so we must use str()
        print("'I now have "+ str(self.items[item]) + " " + item + "'")

    def use_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
        self.items[item] -= quantity
        if self.items[item] == 0:
            print("'Uh oh, buy more " + item + "!'")
        else:
            print("'I have "+ str(self.items[item]) + " " + item + " left'")
