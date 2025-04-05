# Write a function that takes three tuples as input and returns a new tuple containing elements that are common in all three

def __find_common__(t1, t2, t3):

    result = set(t1).intersection(t2, t3)
    # ? as said to return a tuple
    return tuple(result)



# ? User Input
list_of_tuples = list()
for _ in range(3):
    user_input = input("Enter space-separated values for tuple : ")
    temp_tup = tuple(int(item) for item in user_input.split())
    list_of_tuples.append(temp_tup)

# ? Unpacking tuples
t1, t2, t3 = list_of_tuples

print(__find_common__(t1, t2, t3))

