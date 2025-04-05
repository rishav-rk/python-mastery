# Write a function that processes student records stored as a list of dictionaries. Each dictionaries contains:
# 1. "name" : Student's name
# 2. "marks" : Tuple of three subject marks

# The function should return a dictionary where:
# 1. Key = Student name
# 2. Value = Their average marks rounded to 2 decimal places.

def get_student_name_and_average(students):

    result_dict = dict()

    for student in students:
        # rounding digits upto two decimal
        # ? in student variable we get dictionary so accessing items using bracket notation
        result_dict[student["name"]] = round((sum(student["marks"]) / 3),2)

    return result_dict

students = [
    {"name": "Alice", "marks": (80, 90, 80)},
    {"name": "Bob", "marks": (75, 95, 85)},
    {"name": "Charlie", "marks": (60, 80, 80)}
]

print(get_student_name_and_average(students))
print(students)