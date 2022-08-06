class Student:

    max_slip_days = 3 # this is a class variable

    def __init__(self, name, staff):
        self.name = name # this is an instance variable
        self.understanding = 0
        staff.add_student(self)
        print("Added", self.name)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:

    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

    def grant_more_slip_days(self, student, days):
        student.max_slip_days = days

# Remember that Python passes the self argument implicitly to methods 
# when calling the method directly on an object.

callahan = Professor("Callahan")
elle = Student("Elle", callahan)

elle.visit_office_hours(callahan)

elle.visit_office_hours(Professor("Paulette"))

print(elle.understanding)

print([name for name in callahan.students])

x = Student("Vivian", Professor("Stromwell")).name

print(x)

print([name for name in callahan.students])

print(elle.max_slip_days)

callahan.grant_more_slip_days(elle, 7)

print(elle.max_slip_days)

# Remember that Python passes the self argument implicitly to methods 
# when calling the method directly on an object just an object not a class.

print( Student.max_slip_days)