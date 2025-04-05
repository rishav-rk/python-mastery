# Given a list of tuples where each tuple contains a student's name and their marks, sort the list based on:
# 1. Marks in descending order
# 2. If marks are the same sort alphabetically by name

student_record = [("Alice", 85), ("Dave", 90), ("Bob", 95), ("Charlie", 85)]
sorted_student_record = sorted(student_record, key=lambda item: (-item[1], item[0]))
print(sorted_student_record)