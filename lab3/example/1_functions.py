# In Python a function is defined using the def keyword:

def my_function():
    print("Hello from a function")

# calling a function
    
my_function()

# This function expects 2 arguments, and gets 2 arguments:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# This function expects 2 arguments, but gets only 1:

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil")

# Arbitrary arguments
# If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Keyword Arguments

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# Arbitrary Keyword Arguments, **kwargs
# If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value
# If we call the function without argument, it uses the default value:

def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return values

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass

def my_function(x, /):
  print(x)

my_function(3)

# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

def my_function(x):
  print(x)

my_function(x = 3)

# But when adding the , / you will get an error if you try to send a keyword argument:

# def my_function(x, /):
#   print(x)

# my_function(x = 3)

def my_function(*, x):
  print(x)

my_function(x = 3)

def my_function(x):
  print(x)

my_function(3)

# def my_function(*, x):
#   print(x)

# my_function(3)

# error

# Combine Positional-Only and Keyword-Only

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)



# Recursion Example

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
