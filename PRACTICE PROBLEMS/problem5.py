# Create a Python program that takes two complex numbers as input and perform addition, subtraction, multiplication and division on them. Display the real and imaginary parts seprately.

# ? How many complex numbers are to be feeded
n = 2
list_of_complex_numbers = []

for i in range(n):
    real = float(input("Real: "))
    imag = float(input("Imaginary: "))

    compx = complex(real, imag)
    list_of_complex_numbers.append(compx)

add = list_of_complex_numbers[0] + list_of_complex_numbers[1]
sub = list_of_complex_numbers[0] - list_of_complex_numbers[1]
mul = list_of_complex_numbers[0] * list_of_complex_numbers[1]
div = list_of_complex_numbers[0] / list_of_complex_numbers[1]

print('Addtion - ', add)
print('Subtraction - ', sub)
print('Multiplication - ', mul)
print('Division - ', div)




