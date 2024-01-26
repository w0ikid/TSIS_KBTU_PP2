# Unpack tuples

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# asterisk

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# Assign the rest of the values as a list called "red":
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

