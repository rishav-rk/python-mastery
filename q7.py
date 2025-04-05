# Write a function that finds and returns all duplicate elements from a given list of numbers, ensuring that the function runs in O(n) time complexity

def find_duplicates(usr_in):
    s = set()
    duplicates_list = []
    number_list = [int(item) for item in usr_in.split()]
    for element in number_list:
        if element in s:
            duplicates_list.append(element)
        else:
            s.add(element)
    return duplicates_list

user_input = input("Enter space-separated numbers : ")
print(find_duplicates(user_input))