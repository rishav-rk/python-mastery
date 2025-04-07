# Define a list of first 20 natural numbers. Perform the following:
# 1. Extract all even numbers using slicing
# 2. Reverse the list using slicing
# 3. Convert the list into a tuple and print its length

list_of_20_natural_numbers = [item + 1 for item in range(20)]

even_numbers = list_of_20_natural_numbers[1::2]
print("Even Numbers - ", even_numbers)

reversed_list = list_of_20_natural_numbers[::-1]
print("Reversed List - ", reversed_list)

tuple_version = tuple(list_of_20_natural_numbers)
print("Length of ", tuple_version, " --> ", len(tuple_version))