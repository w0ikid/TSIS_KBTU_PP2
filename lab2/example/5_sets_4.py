# remove

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# 

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#


thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)