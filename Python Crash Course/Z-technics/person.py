class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)

x = Person('John', 'Doe')
x.printname()

# Student will inherit properties and methods of Person
class Student(Person):
    pass

x = Student('Mike', 'Olsen')
x.printname()

class Student(Person):
    def __init__(self, fname, lname):   # when add the __init__() function, the child
        super().__init__(fname, lname)  # class will no longer inherit the parent's
        self.graduationyear = 2029      # __init__() function. The child's __init__()
                                        # function overrides the inheritance of the
x = Student('Tony', 'Cha')              # parent's __init__() function. To keep the
print(x.graduationyear)                 # inheritance of the parent's __init__() function,
print(f"{x.firstname} {x.lastname}")    # add a call to the parent's __init__() function.

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.lastname, self.lastname, "to the class of", self.graduationyear)

x = Student('David', 'Bowie', 2039)
print(x.graduationyear)
print(f"{x.firstname} {x.lastname}")
x.welcome()

class Parent:
    def first(self):
        print("parent's function")
class Child(Parent):
    def second(self):
        print("Child's function")
ob = Child()
ob.first()
ob.second()

class Parent:
    def __init__(self, fname, fage):
        self.firstname = fname
        self.age = fage
    def view(self):
        print(self.firstname, self.age)
class Child(Parent):
    def __init__(self, fname, fage):
        Parent.__init__(self, fname, fage)
        self.lastname = "edureka"
    def view(self):
        print("\ncourse name", self.firstname, "first name", self.age, " year ageo.", self.lastname, " has courses to master python")
ob = Child("Python" , '28')
ob.view()
