# Write a Python program that takes a string input and performs the following operations:
# 1. Convert it to uppercase and lowercase
# 2. Count the occurrences of a specific character
# 3. Reverse the string without using built-in functions

user_input = input("Enter the string: ")

print(user_input.upper())
print(user_input.lower())

char = input("Enter the character to count: ")
print(f"char occurred {user_input.count(char)} times.")

reversed_string = user_input[::-1]
print(reversed_string)

