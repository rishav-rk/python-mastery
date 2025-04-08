# Create a dictionary with 5 key-value pairs representing students and their marks. Perform the following operations:
# a. Print students who scored above 80
# b. Add a new student and update an existing student's marks.
# c. Remove a student with the lowest marks.

data = {
    "Rohan": 99, 
    "Rakesh": 90,
    "Akash": 75,
    "Nikita": 70,
    "Aakriti": 78
}

# ? Scored above 80
print("Students scored above 80 - ", end=" ")
for key in data:
    if data[key] > 80:
        print(key, end=", ")

print("""\nEnter
      1. Add new student
      2. Update existing student""")

choice = int(input("Enter your choice: "))
name = str()
marks = int()
if choice == 1:
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    print(name, ":", type(marks))
    data.update({name:marks})
    print("Updated Record: ", data)
elif choice == 2:
    name = input("Enter student name: ")
    if data.get(name):
        marks = int(input("Enter student marks: "))
        data.update({name:marks})
        print("Updated Record: ", data)
    else:
        print("Record Not Found | Check the spelling")
else:
    print("Invalid choice❌")

data = dict(sorted(data.items(), key=lambda item: -item[1]))
print("Student record with lowest marks", data.popitem(), " is removed successfully")
print("Updated Record: ", data)