# Write a Python function that takes a list of integers as input and returns a new list where:
# 1. Even-indexed elements are doubled.
# 2. Odd-indexed elements are halved
# 3. The entire list is then reversed
def func(usr_in):
    integer_list = [int(item) for item in usr_in.split()]
    length_list = len(integer_list)
    for i in range(length_list):
        if i % 2 == 0:
            integer_list[i] *= 2
        else:
            integer_list[i] /= 2
    integer_list.reverse()
    return integer_list


user_input = input("Enter space-separated integer values : ")   
print(func(user_input))