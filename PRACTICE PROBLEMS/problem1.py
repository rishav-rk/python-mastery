# Write a program that takes two numbers as input and performs all arithmetic operations (addition, subtraction, multiplication, division, modulus, exponentiation, and floor division) on them.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition - ", a + b)
print("Subtraction -  ", a - b)
print("Multiplication - ", a * b)
print("Division - ", round(a / b, 2))
print("Modulus - ", a % b)
print("Exponentiation - ", a ** b)
print("Floor Division ", a // b)