# Write a Python function that takes a list of numbers as input and returns the second largest number without using built in sorting functions
import random
def find_second_largest(list_of_numbers):
    copy_of_list = set(list_of_numbers.copy())
    copy_of_list.remove(max(list_of_numbers))
    return max(copy_of_list)

# list_of_numbers = [random.randint(1,100) for _ in range(10)]
list_of_numbers = [1, 3, 4, 5, 3, 2, 10, 10, 3, 9]
print(list_of_numbers)
print(find_second_largest(list_of_numbers))