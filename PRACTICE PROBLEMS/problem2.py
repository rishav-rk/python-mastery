# Given a list of mixed data types: [23, "hello", 3.14, (1, 2, 3), {5, 6, 7}, {"name" : "John"}, True], write a Python program to identify the data type of each element and print whether it is mutable or immutable

input_list = [23, "hello", 3.14, (1, 2, 3), {5, 6, 7}, {"name" : "John"}, True]

for element in input_list:
    element_type = type(element)
    print(f"Element: {element} | Type: {element_type} | ",end=" ")
    if element_type in (int, bool, float, complex, str, tuple):
        print("Immutable")
    else:
        print("Mutable")
