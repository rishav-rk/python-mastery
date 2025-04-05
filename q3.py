user_input = input("Enter comman-separated values : ")

integer_tuple = tuple(int(item) for item in user_input.split(","))

duplicates = {item:integer_tuple.count(item) for item in integer_tuple if integer_tuple.count(item) > 1}

print(duplicates if len(duplicates) else "No duplicates found")