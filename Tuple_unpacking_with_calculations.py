# Given a list of tuples  where each tuple contains the dimensions (length, width, height) of a box, write a function to return a list of tuples where:
# -- Each tuple contains original dimensions and volume of the box.

def calculate_and_merge_volumes(list_of_tuples):

    result = []
    for tup in list_of_tuples:
        vol = 1
        for num in tup:
            vol *= num
        new_tup = tup + (vol,)
        result.append(new_tup)

    return result

list_of_tuples_input = [(2, 3, 4), (5, 6, 7), (1, 2, 3)]
print(calculate_and_merge_volumes(list_of_tuples_input))