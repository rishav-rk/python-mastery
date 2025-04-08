# Create a Python package called math_operations containing two modules:
# a. arithmetic.py: For basic arithmetic operations
# b. advanced.py: For exponentiation and logarithm calculations
# c. Write a script to import and test these modules

# main.py
from math_operations import arithmetic, advanced

# Using arithmetic module
print("Add:", arithmetic.add(10, 5))
print("Subtract:", arithmetic.subtract(10, 5))
print("Multiply:", arithmetic.multiply(10, 5))
print("Divide:", arithmetic.divide(10, 5))

# Using advanced module
print("Power:", advanced.power(2, 3))
print("Logarithm (base 2):", advanced.logarithm(10, 2))
