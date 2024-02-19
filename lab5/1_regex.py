import re

txt = "The rain in Spain"

x = re.search("^The.*Spain$")

# ^ - start with
# . - any character
# * - zero or more occurences
# .* в данном txt это значения имеет ввиду содержит все до 

x = re.findall("ai", txt)
print(x)

# Print a list of all matches: ai ai


x = re.findall("Portugal", txt)
print(x)

# If array is empty return empty array

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

# If it doesnt contain return None

# .split()

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# Где whitespace делит по массиву

# You can control the number of occurrences by specifying the maxsplit parameter:

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# ['The', 'rain in Spain']

# The .sub() function
#Replace all white-space characters with the digit "9":

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#The9rain9in9Spain
#
#Replace the first two occurrences of a white-space character with the digit 9:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
# The9rain9in Spain

# Match object 

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object



#Search for an upper case "S" character in the beginning of a word, and print its position:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

#The string property returns the search string:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

#Search for an upper case "S" character in the beginning of a word, and print the word:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())