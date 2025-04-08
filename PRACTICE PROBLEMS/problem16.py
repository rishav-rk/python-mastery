# Write a Python program that writes 10 random numbers to a file, reopens the file, and prints only the 5th number using seek() function.
import random


try:
    with open("random-numbers.txt", "w") as file:
        for _ in range(10):
            num = random.randint(10, 99)
            file.write(f"{num} ")
    with open("random-numbers.txt", "r") as file:   
        file.seek(12)
        content = file.read(2)
        print("5th number: ", content)

except FileNotFoundError:
    print("File Not Found")