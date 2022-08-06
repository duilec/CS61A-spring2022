def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list.
    >>> my_map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    """
    "*** YOUR CODE HERE ***"
    return [fn(val) for val in seq]

# print(my_map(lambda x: x*x, [1, 2, 3]))

def my_filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.
    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])  # new list has only even-valued elements
    [2, 4]
    """
    "*** YOUR CODE HERE ***"
    return [val for val in seq if pred(val) == True] # the condition in rear

# print(my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])) 

def my_reduce(combiner, seq):
    """Combines elements in seq using combiner.
    seq will have at least one element.
    >>> my_reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 1 + 2 + 3 + 4
    10
    >>> my_reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 1 * 2 * 3 * 4
    24
    >>> my_reduce(lambda x, y: x * y, [4])
    4
    >>> my_reduce(lambda x, y: x + 2 * y, [1, 2, 3]) # (1 + 2 * 2) + 2 * 3
    11
    """
    "*** YOUR CODE HERE ***"
    if len(seq) == 1:
        return seq[0]
    elif len(seq) == 2:
        return combiner(seq[0], seq[1])
    else:
        return combiner(combiner(seq[0], seq[1]), my_reduce(combiner, seq[2:]))

# print(my_reduce(lambda x, y: x + 2 * y, [1, 2, 3]))

class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0


class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.
    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.press(2) # No button at this position
    ''
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """
    def __init__(self, *args):
        self.buttons = {}
        for index in range(len(args)):
            self.buttons[index] = args[index] # A Keyboard takes in an arbitrary amount of buttons ==> map

    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output."""
        if info < len(self.buttons):
            self.buttons[info].times_pressed += 1
            return self.buttons[info].key
        else:
            return

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output."""
        ouput = []
        for num in typing_input:
            # self.buttons[num].times_pressed += 1
            # ouput += self.buttons[num].key # num is the key of dictionary
            # below this is simple
            ouput += self.press(num)
        return ouput


b1 = Button(0, "H")
b2 = Button(1, "I")
k = Keyboard(b1, b2)
print(k.buttons[0].key)

print(k.press(1))

print(k.press(2))

print(k.typing([1, 0]))

print(k.typing([0, 1]))

print(b1.times_pressed)

print(b2.times_pressed)