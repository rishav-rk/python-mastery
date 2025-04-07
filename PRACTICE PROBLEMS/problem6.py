# Write a Python program that takes three numbers as input and determines the largest and smallest among them without using built-in max() and min() functions

a = float(input("Enter first no.: "))
b = float(input("Enter second no.: "))
c = float(input("Enter third no.: "))

if a > b and a > c:
    print(a, " is largest")
elif b > c:
    print(b, " is largest")
else:
    print(c, " is largest")

if a < b and a < c:
    print(a, " is smallest")
elif b < c:
    print(b, " is smallest")
else:
    print(c, " is smallest")