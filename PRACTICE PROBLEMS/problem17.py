# Write a Python script that takes two numbers from the user and performs division. Handle exceptions for zero division, invalid input (non-numeric), and keyboard interrupt gracefully

a = input("Enter Divident: ")
b = input("Enter Divisor: ")

try:
    a = float(a)
    b = float(b)
    result = a / b
    print(round(result, 4))

except ValueError:
    print("Incompatible type of data, check input again!")
except ZeroDivisionError:
    print("Can't Divide by zero!")
except KeyboardInterrupt:
    print("\nProgram halted by user!")
