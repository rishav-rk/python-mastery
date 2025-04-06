# Write a Program that:
# 1. Reads a text file (input.txt) using read() and store its content
# 2. Reverses the content and writes it to a new file (reversed_output.txt)
# 3. Uses the seek() function to read and display that last 10 characters from the reversed file.

# ? When we open file in r -> read mode file must exist
file = open("input.txt","r")
# ? Reading and reversing content
content = file.read()
reversed_content = content[::-1]
print(reversed_content)
file.close()

# ? Writing content to reversed_output.txt file w+ --> for writing and seeking
file = open("reversed_output.txt", "w+")
file.write(reversed_content)

# ? tell() method tells us where the current stream pointer is in the file ---> here , 19 OR end of file
current_position = file.tell()

# ? shifting stream pointer to the 10th character from last
file.seek(current_position - 10)

# ? reading file content from current position of stream pointer (now --> 9) all the way to end
print(file.readline())

file.close()