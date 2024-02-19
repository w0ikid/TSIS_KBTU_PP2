import re

f = open("test.txt", "r")
txt = f.read()

# 1 ex
def find_ab(text) -> str:
    if re.search("ab*", txt):
        return "Match found"
    else:
        return "Match doesnt found"

# 2 ex
def find_abb(text) -> str:
    if re.search("ab{2,3}", text):
        return "Match found"
    else:
        return "Match doenst found"


# 3 ex
def find_sequences_lowercase_underscore(text):
    return re.findall("[a-z]+_[a-z]+", text)


# 4 ex
def find_seq_upper_lower(text):
    return re.findall("[A-Z]+[a-z]+", text)

# 5 ex
def find_a_endb(text) -> str:
    if (re.search("a.*b$", text)):
        return "Match found"
    else:
        return "Match doesnt found"

# 6 ex
def replace_characters(text):
    return re.sub("[ ,.]", ";", text)

# 7 ex
def snake_to_camel(text):
    parts = text.split('_')
    
    other_parts_capitalized = [part.capitalize() for part in parts]
    
    camel_case = ''.join(other_parts_capitalized)
    
    return camel_case

# 8 ex
def split_upper(text):
    text_split = re.findall("[A-Z][a-z]*", text)
    return ' '.join(text_split)
print(split_upper(txt))

# 9 ex
def add_space_before_capital (text) -> str:

    listOfStrings = re.findall("[A-Z][^A-Z]*", text)
    answer = f"{listOfStrings[0]}"
    for i in listOfStrings[1::]:
        answer += ' ' + i

    return answer
# 10 ex
def camel_to_snake(text) -> str:
    listOfStrings = re.findall("[A-Z][^A-Z]*", text)
    answer = f"{listOfStrings[0].lower()}"
    for i in listOfStrings[1::]:
        answer += '_' + i.lower()
    return answer
