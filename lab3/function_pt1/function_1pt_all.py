# 1 ex

def grams_to_ounces(grams):
    return 28.3495231 * grams

# 2 ex

def c_f(num_f):
    return (5 / 9) * (num_f - 32)

# 3 ex

def solve(numheads, numlegs):
    rabbits = (numlegs - 2*numheads) / 2
    chickens = numheads - rabbits
    
    if rabbits >= 0 and chickens >= 0 and int(rabbits) == rabbits and int(chickens) == chickens:
        return int(chickens), int(rabbits)
    else:
        return "No solution"
    
# 4 ex

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(nums):
    return [n for n in nums if is_prime(n)]

# 5 ex

def all_per(str):
    for i in str:
        print(i, end=" ")

# all_per("Nursultan")

# 6 ex

def reverse_string(str):
    str_reverse = ""
    str_list = str.split()

    for i in range(len(str_list), 0, -1):
        str_reverse += str_list[i-1] + " "
    return str_reverse.strip()  # .strip() убирает лишний пробел в конце строки

# print(reverse_string("The best Union"))

# 7 ex

# def has_33(nums):
#     for i in range(1, len(nums)):
#         if nums[i - 1] == 3 and nums[i] == 3:
#             return True
#     return False

# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))

# 8 ex

def spy_game(nums):
    counter = 3
    for i in range(0, len(nums)):
        if counter == 3 or counter == 2:
            if nums[i] == 0:
                counter = counter - 1
        else:
            if nums[i] == 7:
                return True
    return False

# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))

# 9 ex
from cmath import pi

def volume_of_sphere(radius):
    return (4 / 3) * pi * radius**3

# 10 ex

def unique(list_of_elements):
    unique_elements = []
    for i in list_of_elements:
        if i not in unique_elements:
            unique_elements.append(i)
    return unique_elements

# print(unique([1,1,1,2,2,2,3,4,3,4,5]))

# 11 ex

def is_palindrome(str):
    for i in range(0, len(str) // 2):
        if str[i] != str[len(str) - 1 - i]:
            return False
    return True

# print(is_palindrome("madam"))
# print(is_palindrome("internet"))
# print(is_palindrome("abba"))

# 12 ex

def historgram(list_of_numbers):
    for i in list_of_numbers:
        print(i * "*")

# historgram([4])
# historgram([7])

# 13 ex

import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    
    number_to_guess = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    guess_count = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        
        guess_count += 1
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guess_count} guesses!")
            break

guess_the_number()


