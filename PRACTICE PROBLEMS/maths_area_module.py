# Create a Python module that contains a function to calculate the area and perimeter of a rectangle, square and circle. Import this module in a separate script and use it.

# Area and Perimeter Sqaure
def area_square(side):
    return side ** 2
def perimeter_sqaure(side):
    return 4 * side

# Area and Perimeter Rectangle
def area_rect(length, breadth):
    return length * breadth
def perimeter_rect(length, breadth):
    return 2 * (length + breadth)

# Area and Perimeter circle
def area_circle(radius):
    return round((22 * radius * radius)/7, 4)
def perimeter_circle(radius):
    return round((2 * 22 * radius)/7, 4)