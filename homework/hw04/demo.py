class Parent:
    def f(sel):
        print("Parent.f")

    def g(s):
        s.f()

class Child(Parent):
    def f(me):
        print("Child.f")

a_parent = Parent()
a_parent.g()

a_child = Child()
a_child.g() # use f() by itself firstly