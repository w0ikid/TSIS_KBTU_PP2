class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# Create a child pass

class Student(Person):
  pass

# Use the Student class to create an object, and then execute the printname method.

x = Student("Mike", "Olsen")
x.printname()

#  Add __init__() Function

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.


# super()

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)


# add properties

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

# year parameter

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

# add methods

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


