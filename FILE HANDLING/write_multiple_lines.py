# Create a program that takes multiple lines of user input and writes them to a file (output.txt)
# 1. Ask the user to enter lines until they type "STOP"
# 2. Use writelines() to write all the lines at once

print("Enter text (type 'STOP' to finish: )")

lines = [] 
while True:
    # ? Take input while user writes STOP
    line = input()
    if line == "STOP":
        break
    # ? Appending each line until "STOP" is encountered
    lines.append(line)

# ? joining list items as one multi-line string with a newline
multi_line_string = '\n'.join(lines)
print(multi_line_string)

# ? Writing content to output.txt
try:
    with open("output.txt", "w") as file:
        file.writelines(multi_line_string)

except FileNotFoundError:
    print(f"{file.name} not found")
