# boolean values

print(10 > 9)
print(10 == 9)
print(10 < 9)

# True False using if

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


print(bool("Hello"))
print(bool(15))

# true values

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# some values are false

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# return 0 or false

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Function can return True and False

def myFunction() :
  return True

print(myFunction())

# Other example

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# check number are integer or not

x = 200
print(isinstance(x, int))