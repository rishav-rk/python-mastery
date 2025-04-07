# Write a Python program that iterates through numbers 1 to 50 and does the following:
# 1. Skip multiples of 5 using continue
# 2. Stop the loop when a number divisible by both 7 and 11 is found using break.
# 3. Use pass for even numbers

for i in range(1, 81):
    if i % 5 == 0:
        continue
    elif i % 7 == 0 and i % 11 == 0:
        break
    elif i % 2 == 0:
        pass
    else:
        print(i, end=", ")
