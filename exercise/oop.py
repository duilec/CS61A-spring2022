"""
This class represents a player in a video game.
It tracks their name and health.
"""
class Player:
    """
    >>> player = Player("Mario")
    >>> player.name
    'Mario'
    >>> player.health
    100
    >>> player.damage(10)
    >>> player.health
    90
    >>> player.boost(5)
    >>> player.health
    95
    """
    def __init__(self, name):
        self.name = name
        self.health = 100

    def damage(self, value):
        self.health -= value

    def boost(self, value):
        self.health += value\

player = Player("Mario")
print(player.name)


"""
Clothing is a class that represents pieces of clothing in a closet. 
It tracks the color, category, and clean/dirty state.
"""
class Clothing:
    """
    >>> blue_shirt = Clothing("shirt", "blue")
    >>> blue_shirt.category
    'shirt'
    >>> blue_shirt.color
    'blue'
    >>> blue_shirt.is_clean
    True
    >>> blue_shirt.wear()
    >>> blue_shirt.is_clean
    False
    >>> blue_shirt.clean()
    >>> blue_shirt.is_clean
    True
    """
    def __init__(self, category, color):
        self.category = category
        self.color = color
        self.is_clean = True
    
    def wear(self):
        self.is_clean = False
    
    def clean(self):
        self.is_clean = True

"""
This class represents grades for students in a class.
"""
class StudentGrade:
    """
    >>> grade1 = StudentGrade("Arfur Artery", 300)
    >>> grade1.is_failing()
    False
    >>> grade2 = StudentGrade("MoMo OhNo", 158)
    >>> grade2.is_failing()
    True
    >>> grade1.failing_grade
    159
    >>> grade2.failing_grade
    159
    >>> StudentGrade.failing_grade
    159
    >>>
    """
    failing_grade = 159
    def __init__(self, student_name, num_points):
        self.student_name = student_name
        self.num_points = num_points

    def is_failing(self):
        return self.num_points < self.failing_grade