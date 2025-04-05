user_input = input("Enter space-separated values : ")
integer_list = [int(item) for item in user_input.split()]

unique_items = [ item for item in integer_list if integer_list.count(item) == 1]
unique_items.sort()
if len(unique_items) != 0:
    print("Second largest element = ", unique_items[len(unique_items) - 2])
    print(unique_items)
else:
    print("No unique elements present")