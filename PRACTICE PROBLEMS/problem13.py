# Create a Python module that contains a function to calculate the area and perimeter of a rectangle, square and circle. Import this module in a separate script and use it.
# ! (math_area_module.py)

import maths_area_module as mtharea

side = float(input("Enter side of sqaure: "))
print("Area of sqaure: ", mtharea.area_square(side), " | Perimeter: ", mtharea.perimeter_sqaure(side))

length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
print("Area of rectangle: ", mtharea.area_rect(length, breadth), " | Perimeter: ", mtharea.perimeter_rect(length, breadth))

radius = float(input("Enter radius: "))
print("Area of circle: ", mtharea.area_circle(radius), " | Perimeter: ", mtharea.perimeter_circle(radius))
