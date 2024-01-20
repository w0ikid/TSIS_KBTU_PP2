# Global variables

# Variables that are created outside of a function (as in all of the examples above) are known as global variables.

# x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc()

# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)

# Example
# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)