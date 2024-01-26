# Remove lists

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# delete item index

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# pop without number delete the last item in the list

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)



thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)