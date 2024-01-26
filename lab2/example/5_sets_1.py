myset = {"apple", "banana", "cherry"}

# A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Duplicates will be ignored

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# True and 1 considered the same value

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}

myset = {"apple", "banana", "cherry"}
print(type(myset))

# <class 'set'>

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)